from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATALOG = (ROOT / 'docs' / 'EVIDENCE_CATALOG.md').read_text(encoding='utf-8')
README = (ROOT / 'README.md').read_text(encoding='utf-8')
INDEX = (ROOT / 'index.html').read_text(encoding='utf-8')
APP = (ROOT / 'app' / 'app.js').read_text(encoding='utf-8')
CORE = (ROOT / 'app' / 'core.js').read_text(encoding='utf-8')
LIMITATIONS = (ROOT / 'docs' / 'KNOWN_LIMITATIONS.md').read_text(encoding='utf-8')
IP_NOTICE = (ROOT / 'docs' / 'IP_NOTICE.md').read_text(encoding='utf-8')

errors = []

evidence_ids = re.findall(r'^### EVD-(\d{3}) —', CATALOG, flags=re.MULTILINE)
expected_evidence_ids = [f'{i:03d}' for i in range(1, 16)]
if evidence_ids != expected_evidence_ids:
    errors.append(f'Evidence catalog must be continuous EVD-001-EVD-015, found: {evidence_ids}')

required_catalog_markers = [
    'EVD-005 — Explainable health-risk simulation',
    'EVD-007 — Demonstration certificate verification',
    'EVD-013 — Explicit limitation disclosure',
    'EVD-014 — Public/private IP boundary',
    'EVD-015 — Due-diligence package integrity',
    'tests/test_core.mjs',
    'tests/test_evidence_contract.py',
]
for marker in required_catalog_markers:
    if marker not in CATALOG:
        errors.append(f'Evidence catalog missing marker: {marker}')

if 'app/core.js' not in INDEX or INDEX.index('app/core.js') > INDEX.index('app/app.js'):
    errors.append('index.html must load app/core.js before app/app.js')

for marker in ('core.calculateHealthRisk', 'core.filterFeatures', 'core.countStatuses', 'core.verifyDemoCertificate'):
    if marker not in APP:
        errors.append(f'Runtime app is not wired to shared core function: {marker}')

for marker in ('calculateHealthRisk', 'verifyDemoCertificate', 'filterFeatures', 'countStatuses'):
    if marker not in CORE:
        errors.append(f'Core logic missing function: {marker}')

arabic_limitations = re.findall(r'^(\d+)\. \*\*', LIMITATIONS.split('## English')[0], flags=re.MULTILINE)
english_part = LIMITATIONS.split('## English', 1)[1] if '## English' in LIMITATIONS else ''
english_limitations = re.findall(r'^(\d+)\. ', english_part, flags=re.MULTILINE)
expected_limitations = [str(i) for i in range(1, 24)]
if arabic_limitations != expected_limitations:
    errors.append('Arabic limitations must remain a continuous 1-23 sequence')
if english_limitations[:23] != expected_limitations:
    errors.append('English limitations must remain a continuous 1-23 sequence')

if 'Chain of Title' not in IP_NOTICE:
    errors.append('IP notice must retain Chain of Title requirement')

if 'docs/EVIDENCE_CATALOG.md' not in README:
    errors.append('README must link docs/EVIDENCE_CATALOG.md')

if errors:
    print('Evidence contract tests failed:')
    for error in errors:
        print(f' - {error}')
    raise SystemExit(1)

print('SMART Camel AI evidence contract tests passed.')
print('Evidence IDs: EVD-001-EVD-015 continuous')
print('Runtime uses shared testable core logic')
print('Known limitations: 23 Arabic + 23 English preserved')
print('IP and README evidence boundaries verified')
