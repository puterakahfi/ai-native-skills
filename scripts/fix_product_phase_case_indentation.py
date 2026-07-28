#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'contracts/tests/product-development-workflow.test.yaml'
text = path.read_text(encoding='utf-8')
marker = '\n- id: dashboard-experience-package-before-solution-design'
idx = text.index(marker) + 1
prefix = text[:idx]
suffix = text[idx:]
suffix = '\n'.join(('  ' + line) if line else line for line in suffix.splitlines()) + '\n'
path.write_text(prefix + suffix, encoding='utf-8')
(root / '.github/workflows/fix-product-phase-case-indentation.yml').unlink(missing_ok=True)
Path(__file__).unlink(missing_ok=True)
