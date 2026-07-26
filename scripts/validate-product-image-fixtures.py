#!/usr/bin/env python3
"""Validate deterministic Product Image Production PNG fixtures using stdlib only."""

from __future__ import annotations

import argparse
import binascii
import hashlib
import json
import struct
import sys
import zlib
from collections import deque
from pathlib import Path
from typing import Any

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


class ValidationError(RuntimeError):
    pass


class FixtureResolver:
    def __init__(self, manifest_path: Path, bundle_file: str | None):
        self.fixtures_dir = manifest_path.parent
        self.bundle: dict[str, bytes] = {}
        if bundle_file:
            bundle_path = self.fixtures_dir / bundle_file
            document = json.loads(bundle_path.read_text(encoding="utf-8"))
            if document.get("encoding") != "base64":
                raise ValidationError(f"{bundle_path}: unsupported fixture bundle encoding")
            for name, encoded in document.get("files", {}).items():
                self.bundle[name] = __import__("base64").b64decode(encoded, validate=True)

    def load(self, name: str) -> dict[str, Any]:
        file_path = self.fixtures_dir / name
        if file_path.is_file():
            return read_png_bytes(file_path.read_bytes(), file_path.as_posix())
        if name in self.bundle:
            return read_png_bytes(self.bundle[name], f"embedded://{name}")
        raise ValidationError(f"fixture not found: {name}")


def read_png_bytes(data: bytes, display_path: str) -> dict[str, Any]:
    path = display_path
    if not data.startswith(PNG_SIGNATURE):
        raise ValidationError(f"{path}: invalid PNG signature")

    offset = len(PNG_SIGNATURE)
    width = height = bit_depth = color_type = interlace = None
    compressed = bytearray()
    seen_iend = False

    while offset < len(data):
        if offset + 12 > len(data):
            raise ValidationError(f"{path}: truncated PNG chunk")
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        kind = data[offset + 4 : offset + 8]
        payload_start = offset + 8
        payload_end = payload_start + length
        crc_end = payload_end + 4
        if crc_end > len(data):
            raise ValidationError(f"{path}: truncated {kind!r} chunk")
        payload = data[payload_start:payload_end]
        expected_crc = struct.unpack(">I", data[payload_end:crc_end])[0]
        actual_crc = binascii.crc32(kind + payload) & 0xFFFFFFFF
        if expected_crc != actual_crc:
            raise ValidationError(f"{path}: CRC mismatch in {kind.decode('ascii', 'replace')}")

        if kind == b"IHDR":
            if length != 13:
                raise ValidationError(f"{path}: invalid IHDR length")
            width, height, bit_depth, color_type, compression, filter_method, interlace = struct.unpack(
                ">IIBBBBB", payload
            )
            if bit_depth != 8 or color_type != 6:
                raise ValidationError(
                    f"{path}: only 8-bit RGBA PNG is supported, got bit_depth={bit_depth}, color_type={color_type}"
                )
            if compression != 0 or filter_method != 0 or interlace != 0:
                raise ValidationError(f"{path}: unsupported PNG compression/filter/interlace mode")
        elif kind == b"IDAT":
            compressed.extend(payload)
        elif kind == b"IEND":
            seen_iend = True
            break
        offset = crc_end

    if not seen_iend or width is None or height is None:
        raise ValidationError(f"{path}: incomplete PNG structure")

    try:
        raw = zlib.decompress(bytes(compressed))
    except zlib.error as exc:
        raise ValidationError(f"{path}: invalid IDAT stream: {exc}") from exc

    bpp = 4
    stride = width * bpp
    expected_size = height * (stride + 1)
    if len(raw) != expected_size:
        raise ValidationError(
            f"{path}: decompressed size {len(raw)} does not match expected {expected_size}"
        )

    rows: list[bytearray] = []
    previous = bytearray(stride)
    cursor = 0
    for row_index in range(height):
        filter_type = raw[cursor]
        cursor += 1
        scanline = bytearray(raw[cursor : cursor + stride])
        cursor += stride
        reconstructed = unfilter(scanline, previous, filter_type, bpp, display_path, row_index)
        rows.append(reconstructed)
        previous = reconstructed

    pixels = []
    for row in rows:
        pixels.append(
            [tuple(row[index : index + 4]) for index in range(0, len(row), 4)]
        )

    return {
        "path": display_path,
        "width": width,
        "height": height,
        "pixels": pixels,
        "sha256": hashlib.sha256(data).hexdigest(),
        "byte_size": len(data),
    }


def paeth(a: int, b: int, c: int) -> int:
    estimate = a + b - c
    pa = abs(estimate - a)
    pb = abs(estimate - b)
    pc = abs(estimate - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def unfilter(
    scanline: bytearray,
    previous: bytearray,
    filter_type: int,
    bpp: int,
    path: str,
    row_index: int,
) -> bytearray:
    result = bytearray(len(scanline))
    for index, value in enumerate(scanline):
        left = result[index - bpp] if index >= bpp else 0
        up = previous[index]
        upper_left = previous[index - bpp] if index >= bpp else 0
        if filter_type == 0:
            recon = value
        elif filter_type == 1:
            recon = (value + left) & 0xFF
        elif filter_type == 2:
            recon = (value + up) & 0xFF
        elif filter_type == 3:
            recon = (value + ((left + up) // 2)) & 0xFF
        elif filter_type == 4:
            recon = (value + paeth(left, up, upper_left)) & 0xFF
        else:
            raise ValidationError(f"{path}: unsupported filter {filter_type} at row {row_index}")
        result[index] = recon
    return result


def alpha_metrics(image: dict[str, Any]) -> dict[str, Any]:
    pixels = image["pixels"]
    width = image["width"]
    height = image["height"]
    nonzero = []
    partial = 0
    transparent_rgb_nonzero = 0
    opaque = 0
    for y, row in enumerate(pixels):
        for x, (r, g, b, a) in enumerate(row):
            if a > 0:
                nonzero.append((x, y))
            if 0 < a < 255:
                partial += 1
            if a == 0 and (r or g or b):
                transparent_rgb_nonzero += 1
            if a == 255:
                opaque += 1

    bbox = None
    touches_border = False
    if nonzero:
        xs = [point[0] for point in nonzero]
        ys = [point[1] for point in nonzero]
        bbox = [min(xs), min(ys), max(xs) + 1, max(ys) + 1]
        touches_border = (
            bbox[0] == 0 or bbox[1] == 0 or bbox[2] == width or bbox[3] == height
        )

    component_sizes = connected_alpha_components(pixels)
    small_components = [size for size in component_sizes if size <= 4]
    main_component = max(component_sizes, default=0)

    return {
        "nonzero_alpha_pixels": len(nonzero),
        "partial_alpha_pixels": partial,
        "opaque_pixels": opaque,
        "transparent_rgb_nonzero_pixels": transparent_rgb_nonzero,
        "content_bbox": bbox,
        "touches_canvas_border": touches_border,
        "component_count": len(component_sizes),
        "small_component_count": len(small_components),
        "component_sizes": sorted(component_sizes, reverse=True),
        "main_component_pixels": main_component,
    }


def connected_alpha_components(pixels: list[list[tuple[int, int, int, int]]]) -> list[int]:
    height = len(pixels)
    width = len(pixels[0]) if height else 0
    visited: set[tuple[int, int]] = set()
    sizes: list[int] = []
    for y in range(height):
        for x in range(width):
            if pixels[y][x][3] == 0 or (x, y) in visited:
                continue
            queue = deque([(x, y)])
            visited.add((x, y))
            size = 0
            while queue:
                cx, cy = queue.popleft()
                size += 1
                for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
                    if (
                        0 <= nx < width
                        and 0 <= ny < height
                        and pixels[ny][nx][3] > 0
                        and (nx, ny) not in visited
                    ):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            sizes.append(size)
    return sizes


def region_hash(image: dict[str, Any], region: list[int]) -> str:
    x0, y0, x1, y1 = region
    if not (0 <= x0 < x1 <= image["width"] and 0 <= y0 < y1 <= image["height"]):
        raise ValidationError(f"{image['path']}: invalid region {region}")
    payload = bytearray()
    for y in range(y0, y1):
        for x in range(x0, x1):
            payload.extend(image["pixels"][y][x])
    return hashlib.sha256(bytes(payload)).hexdigest()


def alpha_outside_bbox(image: dict[str, Any], bbox: list[int]) -> int:
    x0, y0, x1, y1 = bbox
    count = 0
    for y, row in enumerate(image["pixels"]):
        for x, (_, _, _, a) in enumerate(row):
            if a > 0 and not (x0 <= x < x1 and y0 <= y < y1):
                count += 1
    return count


def composite_expected(
    asset: dict[str, Any], mode: str
) -> list[list[tuple[int, int, int, int]]]:
    width = asset["width"]
    height = asset["height"]
    result = []
    for y in range(height):
        row = []
        for x in range(width):
            if mode == "white":
                br, bg, bb = 255, 255, 255
            elif mode == "declared_gradient":
                br = 35 + int(120 * x / (width - 1))
                bg = 35 + int(60 * y / (height - 1))
                bb = 80
            else:
                raise ValidationError(f"unknown composite background mode: {mode}")
            ar, ag, ab, aa = asset["pixels"][y][x]
            alpha = aa / 255
            row.append(
                (
                    round(ar * alpha + br * (1 - alpha)),
                    round(ag * alpha + bg * (1 - alpha)),
                    round(ab * alpha + bb * (1 - alpha)),
                    255,
                )
            )
        result.append(row)
    return result


def pixels_equal(
    actual: list[list[tuple[int, int, int, int]]],
    expected: list[list[tuple[int, int, int, int]]],
) -> bool:
    return actual == expected


def evaluate_case(case: dict[str, Any], resolver: FixtureResolver) -> dict[str, Any]:
    checks = case.get("checks", {})
    loaded: dict[str, dict[str, Any]] = {}
    file_refs = [
        key
        for key in ("source", "output", "asset", "clean_composite", "ad_composite")
        if key in case
    ]
    for key in file_refs:
        loaded[key] = resolver.load(case[key])

    check_results: list[dict[str, Any]] = []

    def add(name: str, passed: bool, observed: Any, expected: Any) -> None:
        check_results.append(
            {
                "check": name,
                "passed": bool(passed),
                "observed": observed,
                "expected": expected,
            }
        )

    output_key = "output" if "output" in loaded else "asset" if "asset" in loaded else None
    output_metrics = alpha_metrics(loaded[output_key]) if output_key else None

    if checks.get("png_integrity"):
        add("png_integrity", True, "valid", "valid")

    if checks.get("no_border_clipping"):
        assert output_metrics is not None
        add(
            "no_border_clipping",
            not output_metrics["touches_canvas_border"],
            output_metrics["touches_canvas_border"],
            False,
        )

    if checks.get("no_transparent_rgb_spill"):
        assert output_metrics is not None
        observed = output_metrics["transparent_rgb_nonzero_pixels"]
        add("no_transparent_rgb_spill", observed == 0, observed, 0)

    if "max_small_components" in checks:
        assert output_metrics is not None
        observed = output_metrics["small_component_count"]
        expected = int(checks["max_small_components"])
        add("max_small_components", observed <= expected, observed, f"<= {expected}")

    alpha_mode = checks.get("required_alpha_mode")
    if alpha_mode:
        assert output_metrics is not None
        if alpha_mode == "binary":
            observed = output_metrics["partial_alpha_pixels"]
            add("required_alpha_mode_binary", observed == 0, observed, 0)
        elif alpha_mode == "partial":
            observed = output_metrics["partial_alpha_pixels"]
            minimum = int(checks.get("minimum_partial_alpha_pixels", 1))
            add("required_alpha_mode_partial", observed >= minimum, observed, f">= {minimum}")
        else:
            raise ValidationError(f"{case['id']}: unknown alpha mode {alpha_mode}")

    if checks.get("label_must_match_source"):
        source = loaded["source"]
        output = loaded["output"]
        region = checks["label_region"]
        source_hash = region_hash(source, region)
        output_hash = region_hash(output, region)
        add("label_region_fidelity", source_hash == output_hash, output_hash, source_hash)

    if "minimum_effective_resolution" in checks:
        output = loaded[output_key]
        minimum_width, minimum_height = checks["minimum_effective_resolution"]
        observed = [output["width"], output["height"]]
        add(
            "minimum_effective_resolution",
            output["width"] >= minimum_width and output["height"] >= minimum_height,
            observed,
            [minimum_width, minimum_height],
        )

    if "minimum_source_resolution" in checks:
        source = loaded["source"]
        minimum_width, minimum_height = checks["minimum_source_resolution"]
        observed = [source["width"], source["height"]]
        add(
            "minimum_source_resolution",
            source["width"] >= minimum_width and source["height"] >= minimum_height,
            observed,
            [minimum_width, minimum_height],
        )

    if checks.get("required_product_truth"):
        required = set(checks["required_product_truth"])
        missing = set(checks.get("missing_product_truth", []))
        unresolved = sorted(required & missing)
        add("required_product_truth", not unresolved, unresolved, [])

    if checks.get("composites_match_asset_math"):
        asset = loaded["asset"]
        clean_expected = composite_expected(asset, "white")
        ad_expected = composite_expected(asset, "declared_gradient")
        clean_ok = pixels_equal(loaded["clean_composite"]["pixels"], clean_expected)
        ad_ok = pixels_equal(loaded["ad_composite"]["pixels"], ad_expected)
        add(
            "composites_match_asset_math",
            clean_ok and ad_ok,
            {"clean": clean_ok, "ad": ad_ok},
            {"clean": True, "ad": True},
        )

    if checks.get("asset_hash_unchanged"):
        expected_digest = checks.get("expected_asset_sha256")
        observed_digest = loaded["asset"]["sha256"]
        add(
            "asset_hash_unchanged",
            bool(expected_digest) and observed_digest == expected_digest,
            observed_digest,
            expected_digest,
        )

    if checks.get("allow_alpha_outside_product_bbox") is False:
        output = loaded["output"]
        observed = alpha_outside_bbox(output, checks["authorized_product_bbox"])
        add("alpha_outside_authorized_product_bbox", observed == 0, observed, 0)

    if "maximum_upscale_ratio" in checks:
        source = loaded["source"]
        output = loaded["output"]
        ratio = max(output["width"] / source["width"], output["height"] / source["height"])
        maximum = float(checks["maximum_upscale_ratio"])
        add("maximum_upscale_ratio", ratio <= maximum, ratio, f"<= {maximum}")

    failures = [result for result in check_results if not result["passed"]]
    if not failures:
        observed_verdict = "PASS"
    elif case["expected"] == "FAIL_CLOSED":
        observed_verdict = "FAIL_CLOSED"
    else:
        observed_verdict = "FAIL"

    file_evidence = {
        key: {
            "path": case[key],
            "sha256": image["sha256"],
            "width": image["width"],
            "height": image["height"],
            "byte_size": image["byte_size"],
            "alpha_metrics": alpha_metrics(image),
        }
        for key, image in loaded.items()
    }

    return {
        "id": case["id"],
        "category": case["category"],
        "expected_verdict": case["expected"],
        "observed_verdict": observed_verdict,
        "matches_expectation": observed_verdict == case["expected"],
        "checks": check_results,
        "files": file_evidence,
    }


def build_report(manifest_path: Path) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    resolver = FixtureResolver(manifest_path, manifest.get("bundle_file"))
    cases = [evaluate_case(case, resolver) for case in manifest["cases"]]
    matched = sum(1 for case in cases if case["matches_expectation"])
    return {
        "schema_version": 1,
        "suite": "product-image-production-binary-fixtures",
        "evidence_class": manifest["evidence_class"],
        "production_readiness_claim": manifest["production_readiness_claim"],
        "limitations": manifest["limitations"],
        "summary": {
            "total_cases": len(cases),
            "matched_expectations": matched,
            "mismatched_expectations": len(cases) - matched,
            "suite_status": "PASS" if matched == len(cases) else "FAIL",
            "real_product_acceptance": "NOT_VERIFIED",
            "provider_backed_execution": "NOT_VERIFIED",
            "independent_visual_acceptance": "NOT_VERIFIED",
        },
        "cases": cases,
    }


def canonical_json(document: dict[str, Any]) -> str:
    return json.dumps(document, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("validation/product-image-production/fixtures/manifest.json"),
    )
    parser.add_argument("--report", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()

    try:
        report = build_report(args.manifest)
    except (OSError, json.JSONDecodeError, ValidationError, KeyError, ValueError) as exc:
        print(f"product image fixture validation failed: {exc}", file=sys.stderr)
        return 1

    rendered = canonical_json(report)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered, encoding="utf-8")

    if args.compare:
        expected = args.compare.read_text(encoding="utf-8")
        if expected != rendered:
            print(
                f"product image fixture validation failed: report drifted from {args.compare}",
                file=sys.stderr,
            )
            return 1

    print(
        "Product image binary fixture validation: "
        f"{report['summary']['matched_expectations']}/{report['summary']['total_cases']} "
        f"cases matched; suite={report['summary']['suite_status']}; "
        "real-product acceptance=NOT_VERIFIED"
    )
    return 0 if report["summary"]["suite_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
