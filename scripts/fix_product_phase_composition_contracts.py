#!/usr/bin/env python3
from pathlib import Path
import textwrap

root = Path(__file__).resolve().parents[1]
test_path = root / 'contracts/tests/product-development-workflow.test.yaml'
text = test_path.read_text(encoding='utf-8')
marker = '    - id: dashboard-experience-package-before-solution-design'
idx = text.index(marker)
prefix = text[:idx].rstrip()
suffix = textwrap.dedent(text[idx:])
test_path.write_text(prefix + '\n' + suffix.rstrip() + '\n', encoding='utf-8')

coverage = root / 'docs/contract-coverage-discovery.yaml'
text = coverage.read_text(encoding='utf-8')
old = '''  - id: product-development-workflow
    path: skills/product-development-workflow/SKILL.md
    type: workflow
    patterns: []
    version: 3.0.0
'''
new = old.replace('version: 3.0.0', 'version: 3.1.0')
if old not in text:
    raise SystemExit('product-development-workflow coverage entry not found')
coverage.write_text(text.replace(old, new, 1), encoding='utf-8')

(root / '.github/workflows/fix-product-phase-composition-contracts.yml').unlink(missing_ok=True)
Path(__file__).unlink(missing_ok=True)
