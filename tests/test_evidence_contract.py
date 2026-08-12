from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATALOG = (ROOT / 'docs' / 'EVIDENCE_CATALOG.md').read_text(encoding='utf-8')
PHASE3 = (ROOT / 'docs' / 'PHASE3_GRADE_A_EVIDENCE.md').read_text(encoding='utf-8')
PHASE4 = (ROOT / 'docs' / 'PHASE4_245_RECONCILIATION.md').read_text(encoding='utf-8')
MATRIX = (ROOT / 'docs' / 'STRATEGIC_EVIDENCE_MATRIX.md').read_text(encoding='utf-8')
README = (ROOT / 'README.md').read_text(encoding='utf-8')
INDEX = (ROOT / 'index.html').read_text(encoding='utf-8')
APP = (ROOT / 'app' / 'app.js').read_text(encoding='utf-8')
CORE = (ROOT / 'app' / 'core.js').read_text(encoding='utf-8')
LIMITATIONS = (ROOT / 'docs' / 'KNOWN_LIMITATIONS.md').read_text(encoding='utf-8')
IP_NOTICE = (ROOT / 'docs' / 'IP_NOTICE.md').read_text(encoding='utf-8')
RELEASE = (ROOT / 'docs' / 'RELEASE_READINESS.md').read_text(encoding='utf-8')
DEPENDENCY = (ROOT / 'docs' / 'DEPENDENCY_AND_LICENSE_REVIEW.md').read_text(encoding='utf-8')
SECURITY = (ROOT / 'docs' / 'SECURITY.md').read_text(encoding='utf-8')

errors = []

base_ids = re.findall(r'^### EVD-(\d{3}) —', CATALOG, flags=re.MULTILINE)
phase3_ids = re.findall(r'^### EVD-(\d{3}) —', PHASE3, flags=re.MULTILINE)
evidence_ids = base_ids + phase3_ids
expected_evidence_ids = [f'{i:03d}' for i in range(1, 21)]
if evidence_ids != expected_evidence_ids:
    errors.append(f'Evidence records must be continuous EVD-001-EVD-020, found: {evidence_ids}')

for marker in [
    'EVD-001 — Canonical capability continuity',
    'F001-F245',
    '245 معرفاً',
    'EVD-005 — Explainable health-risk simulation',
    'EVD-007 — Demonstration certificate verification',
    'EVD-013 — Explicit limitation disclosure',
    'EVD-014 — Public/private IP boundary',
    'EVD-015 — Due-diligence package integrity',
    'tests/test_core.mjs',
    'tests/test_phase4.mjs',
    'tests/test_evidence_contract.py',
]:
    if marker not in CATALOG:
        errors.append(f'Evidence catalog missing marker: {marker}')

for marker in [
    'EVD-016 — Camel registry schema and identity lookup',
    'EVD-017 — Deterministic geofence state evaluation',
    'EVD-018 — Testable Mazayen scoring demonstrator',
    'EVD-019 — Auction state transition contract',
    'EVD-020 — Ordered bilingual audit-event contract',
    'tests/test_phase3.mjs',
]:
    if marker not in PHASE3:
        errors.append(f'Phase 3 evidence document missing marker: {marker}')

for marker in [
    'F244',
    'F245',
    '245 distinct source-backed capability records',
    'Genetic Breeding with Environmental Impact Analysis',
    'Positive Environmental Impact Evaluation for Camel Breeding',
]:
    if marker not in PHASE4:
        errors.append(f'Phase 4 reconciliation missing marker: {marker}')

if '12 من 12 قدرة استراتيجية = Grade A Evidence' not in MATRIX:
    errors.append('Strategic evidence matrix must declare 12/12 Grade A evidence')
if re.findall(r'\| S\d{2} \| F\d{3} \|[^\n]+\| B \|', MATRIX):
    errors.append('Strategic evidence matrix still contains Grade B rows')

if 'app/source-features-244-245.js' not in INDEX:
    errors.append('index.html must load app/source-features-244-245.js')
if 'app/core.js' not in INDEX or INDEX.index('app/core.js') > INDEX.index('app/app.js'):
    errors.append('index.html must load app/core.js before app/app.js')

runtime_markers = (
    'core.calculateHealthRisk', 'core.filterFeatures', 'core.countStatuses', 'core.verifyDemoCertificate',
    'core.validateCamelRegistry', 'core.evaluateGeofence', 'core.calculateMazayenScore',
    'core.createAuctionState', 'core.placeDemoBid', 'core.appendAuditEvent'
)
for marker in runtime_markers:
    if marker not in APP:
        errors.append(f'Runtime app is not wired to shared core function: {marker}')

core_markers = (
    'calculateHealthRisk', 'verifyDemoCertificate', 'filterFeatures', 'countStatuses',
    'validateCamelRegistry', 'findCamelById', 'evaluateGeofence', 'calculateMazayenScore',
    'createAuctionState', 'placeDemoBid', 'appendAuditEvent'
)
for marker in core_markers:
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
if 'F001-F245' not in LIMITATIONS:
    errors.append('Known limitations must state the current F001-F245 scope')

if 'Chain of Title' not in IP_NOTICE:
    errors.append('IP notice must retain Chain of Title requirement')
if '245 سجل قدرة معيارية F001-F245' not in IP_NOTICE and '245 canonical capabilities F001-F245' not in IP_NOTICE:
    errors.append('IP notice must state the current 245-capability scope')

if 'G15' not in RELEASE or 'Live Stable Demo | Pending' not in RELEASE:
    errors.append('Release readiness must preserve G01-G15 and live-demo Pending state')
if 'No public `LICENSE` file' not in DEPENDENCY:
    errors.append('Dependency/license review must preserve the public licensing boundary')
if 'scripts/security_check.py' not in SECURITY:
    errors.append('Security baseline must document the Phase 4 automated security scan')

for link in (
    'docs/EVIDENCE_CATALOG.md',
    'docs/PHASE3_GRADE_A_EVIDENCE.md',
    'docs/STRATEGIC_EVIDENCE_MATRIX.md',
    'docs/PHASE4_245_RECONCILIATION.md',
    'docs/RELEASE_READINESS.md',
    'docs/DEPENDENCY_AND_LICENSE_REVIEW.md',
):
    if link not in README:
        errors.append(f'README must link {link}')

for command in (
    'node tests/test_phase4.mjs',
    'python scripts/security_check.py',
    'python scripts/release_check.py',
):
    if command not in README:
        errors.append(f'README must expose release command: {command}')

if errors:
    print('Evidence contract tests failed:')
    for error in errors:
        print(f' - {error}')
    raise SystemExit(1)

print('SMART Camel AI evidence contract tests passed.')
print('Evidence IDs: EVD-001-EVD-020 continuous across Phase 2 and Phase 3')
print('Canonical evidence boundary: F001-F245 preserved')
print('Strategic evidence: 12/12 capabilities Grade A')
print('Phase 4 capability reconciliation: F244-F245 preserved')
print('Known limitations: 23 Arabic + 23 English preserved')
print('IP, security, dependency and release-readiness boundaries verified')
