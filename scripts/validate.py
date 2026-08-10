from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FEATURES = 245
EXPECTED_BASE_REGISTRY = 243
EXPECTED_DEMO_SCENARIOS = 10
EXPECTED_LIMITATIONS_PER_LANGUAGE = 23
EXPECTED_EVIDENCE_IDS = 20

FEATURE_FILES = [
    ROOT / 'app' / 'data.js',
    ROOT / 'app' / 'source-features-091-140.js',
    ROOT / 'app' / 'source-features-141-190.js',
    ROOT / 'app' / 'source-features-191-223.js',
    ROOT / 'app' / 'source-features-224-231.js',
    ROOT / 'app' / 'source-features-232-235.js',
    ROOT / 'app' / 'source-features-236-243.js',
    ROOT / 'app' / 'source-features-244-245.js',
]

DUE_DILIGENCE_FILES = [
    ROOT / 'docs' / 'FEATURE_REGISTRY.md',
    ROOT / 'docs' / 'DEMO_SCENARIOS.md',
    ROOT / 'docs' / 'KNOWN_LIMITATIONS.md',
    ROOT / 'docs' / 'SECURITY.md',
    ROOT / 'docs' / 'IP_NOTICE.md',
    ROOT / 'docs' / 'ACQUISITION_TECHNICAL_OVERVIEW.md',
    ROOT / 'docs' / 'EVIDENCE_CATALOG.md',
    ROOT / 'docs' / 'PHASE3_GRADE_A_EVIDENCE.md',
    ROOT / 'docs' / 'STRATEGIC_EVIDENCE_MATRIX.md',
    ROOT / 'docs' / 'PHASE4_245_RECONCILIATION.md',
]

TEST_FILES = [
    ROOT / 'tests' / 'test_core.mjs',
    ROOT / 'tests' / 'test_phase3.mjs',
    ROOT / 'tests' / 'test_evidence_contract.py',
]

required = [
    ROOT / 'index.html',
    ROOT / 'app' / 'styles.css',
    *FEATURE_FILES,
    ROOT / 'app' / 'core.js',
    ROOT / 'app' / 'app.js',
    ROOT / 'docs' / 'ARCHITECTURE.md',
    ROOT / 'docs' / 'EVIDENCE.md',
    ROOT / 'docs' / 'PUBLIC_OVERVIEW.md',
    ROOT / 'docs' / 'SOURCE_RECONCILIATION.md',
    ROOT / 'docs' / 'ALGORITHM_ENGINE_REGISTRY.md',
    ROOT / 'docs' / 'SYSTEM_FAMILIES.md',
    *DUE_DILIGENCE_FILES,
    *TEST_FILES,
    ROOT / '.github' / 'workflows' / 'validate.yml',
    ROOT / 'README.md',
]

errors = []
for path in required:
    if not path.exists():
        errors.append(f'Missing required file: {path.relative_to(ROOT)}')

if not errors:
    index = (ROOT / 'index.html').read_text(encoding='utf-8')
    app = (ROOT / 'app' / 'app.js').read_text(encoding='utf-8')
    core = (ROOT / 'app' / 'core.js').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    algorithms = (ROOT / 'docs' / 'ALGORITHM_ENGINE_REGISTRY.md').read_text(encoding='utf-8')
    systems = (ROOT / 'docs' / 'SYSTEM_FAMILIES.md').read_text(encoding='utf-8')
    acquisition_registry = (ROOT / 'docs' / 'FEATURE_REGISTRY.md').read_text(encoding='utf-8')
    reconciliation = (ROOT / 'docs' / 'PHASE4_245_RECONCILIATION.md').read_text(encoding='utf-8')
    demos = (ROOT / 'docs' / 'DEMO_SCENARIOS.md').read_text(encoding='utf-8')
    limitations = (ROOT / 'docs' / 'KNOWN_LIMITATIONS.md').read_text(encoding='utf-8')
    security = (ROOT / 'docs' / 'SECURITY.md').read_text(encoding='utf-8')
    ip_notice = (ROOT / 'docs' / 'IP_NOTICE.md').read_text(encoding='utf-8')
    acquisition_overview = (ROOT / 'docs' / 'ACQUISITION_TECHNICAL_OVERVIEW.md').read_text(encoding='utf-8')
    evidence_catalog = (ROOT / 'docs' / 'EVIDENCE_CATALOG.md').read_text(encoding='utf-8')
    phase3_evidence = (ROOT / 'docs' / 'PHASE3_GRADE_A_EVIDENCE.md').read_text(encoding='utf-8')
    strategic_matrix = (ROOT / 'docs' / 'STRATEGIC_EVIDENCE_MATRIX.md').read_text(encoding='utf-8')
    workflow = (ROOT / '.github' / 'workflows' / 'validate.yml').read_text(encoding='utf-8')
    feature_text = '\n'.join(path.read_text(encoding='utf-8') for path in FEATURE_FILES)

    feature_ids = re.findall(r"\['F(\d{3})'", feature_text)
    expected_sequence = [f'{i:03d}' for i in range(1, EXPECTED_FEATURES + 1)]
    if len(feature_ids) != EXPECTED_FEATURES:
        errors.append(f'Expected {EXPECTED_FEATURES} feature records, found {len(feature_ids)}')
    if len(set(feature_ids)) != len(feature_ids):
        errors.append('Duplicate feature identifiers detected')
    if feature_ids != expected_sequence:
        errors.append('Feature identifiers are not a continuous F001-F245 sequence')

    base_registry_ids = re.findall(r'^\| F(\d{3}) \|', acquisition_registry, flags=re.MULTILINE)
    if len(base_registry_ids) != EXPECTED_BASE_REGISTRY:
        errors.append(f'Phase 1 acquisition registry must retain {EXPECTED_BASE_REGISTRY} historical F-ID rows')
    if base_registry_ids != [f'{i:03d}' for i in range(1, EXPECTED_BASE_REGISTRY + 1)]:
        errors.append('Phase 1 acquisition registry is not continuous F001-F243')

    addendum_ids = re.findall(r'^\| F(24[45]) \|', reconciliation, flags=re.MULTILINE)
    if addendum_ids != ['244', '245']:
        errors.append('Phase 4 reconciliation must contain F244 and F245 rows')
    combined_registry_ids = base_registry_ids + addendum_ids
    if combined_registry_ids != expected_sequence:
        errors.append('Combined acquisition registry is not continuous F001-F245')

    for marker in (
        'Genetic Breeding with Environmental Impact Analysis',
        'Positive Environmental Impact Evaluation for Camel Breeding',
        '245 distinct source-backed capability records',
    ):
        if marker not in reconciliation:
            errors.append(f'Phase 4 reconciliation missing marker: {marker}')

    scenario_ids = re.findall(r'^### D(\d{2}) —', demos, flags=re.MULTILINE)
    if scenario_ids != [f'{i:02d}' for i in range(1, EXPECTED_DEMO_SCENARIOS + 1)]:
        errors.append('Demo scenarios must be a continuous D01-D10 sequence')

    evidence_ids = (
        re.findall(r'^### EVD-(\d{3}) —', evidence_catalog, flags=re.MULTILINE)
        + re.findall(r'^### EVD-(\d{3}) —', phase3_evidence, flags=re.MULTILINE)
    )
    if evidence_ids != [f'{i:03d}' for i in range(1, EXPECTED_EVIDENCE_IDS + 1)]:
        errors.append('Evidence records must be a continuous EVD-001-EVD-020 sequence')

    if '12 من 12 قدرة استراتيجية = Grade A Evidence' not in strategic_matrix:
        errors.append('Strategic evidence matrix must declare 12/12 Grade A evidence')
    if re.findall(r'\| S\d{2} \| F\d{3} \|[^\n]+\| B \|', strategic_matrix):
        errors.append('Strategic evidence matrix still contains Grade B rows')

    limitation_numbers = re.findall(r'^(\d+)\. ', limitations, flags=re.MULTILINE)
    expected_limitations = [str(i) for i in range(1, EXPECTED_LIMITATIONS_PER_LANGUAGE + 1)] * 2
    if limitation_numbers != expected_limitations:
        errors.append('Known limitations must contain continuous 1-23 lists in Arabic and English')
    if 'إيرادات' not in limitations or 'revenue' not in limitations.lower():
        errors.append('Known limitations must explicitly disclose the absence of evidenced revenue')

    assets = [
        'app/styles.css', 'app/data.js', 'app/source-features-091-140.js',
        'app/source-features-141-190.js', 'app/source-features-191-223.js',
        'app/source-features-224-231.js', 'app/source-features-232-235.js',
        'app/source-features-236-243.js', 'app/source-features-244-245.js',
        'app/core.js', 'app/app.js'
    ]
    for asset in assets:
        if asset not in index:
            errors.append(f'index.html does not reference {asset}')
    if index.find('app/core.js') > index.find('app/app.js'):
        errors.append('app/core.js must load before app/app.js')

    for marker in (
        'core.calculateHealthRisk', 'core.filterFeatures', 'core.countStatuses', 'core.verifyDemoCertificate',
        'core.validateCamelRegistry', 'core.evaluateGeofence', 'core.calculateMazayenScore',
        'core.createAuctionState', 'core.placeDemoBid', 'core.appendAuditEvent'
    ):
        if marker not in app:
            errors.append(f'app.js is not wired to shared core logic: {marker}')

    for marker in (
        'calculateHealthRisk', 'filterFeatures', 'countStatuses', 'verifyDemoCertificate',
        'validateCamelRegistry', 'findCamelById', 'evaluateGeofence', 'calculateMazayenScore',
        'createAuctionState', 'placeDemoBid', 'appendAuditEvent'
    ):
        if marker not in core:
            errors.append(f'core.js missing required function: {marker}')

    if 'ar:{' not in app or 'en:{' not in app:
        errors.append('Bilingual translation objects are incomplete')
    if 'العربية' not in readme or 'English' not in readme:
        errors.append('README must remain bilingual')

    if '29 source-documented named algorithms and engines' not in algorithms:
        errors.append('Algorithm registry does not declare 29 source-documented names')
    if '20 canonical system families' not in systems:
        errors.append('System family document does not declare 20 canonical families')
    if 'E4' not in security or 'Threat Model' not in security:
        errors.append('Security baseline/threat model markers are missing')
    if 'Chain of Title' not in ip_notice:
        errors.append('IP notice does not include Chain of Title requirements')
    if 'Claim → Canonical F-ID' not in acquisition_overview:
        errors.append('Acquisition overview does not declare the evidence-chain model')

    for link in (
        'docs/FEATURE_REGISTRY.md', 'docs/DEMO_SCENARIOS.md', 'docs/KNOWN_LIMITATIONS.md',
        'docs/SECURITY.md', 'docs/IP_NOTICE.md', 'docs/ACQUISITION_TECHNICAL_OVERVIEW.md',
        'docs/EVIDENCE_CATALOG.md', 'docs/PHASE3_GRADE_A_EVIDENCE.md',
        'docs/STRATEGIC_EVIDENCE_MATRIX.md', 'docs/PHASE4_245_RECONCILIATION.md'
    ):
        if link not in readme:
            errors.append(f'README does not link required due-diligence document: {link}')

    for command in ('node tests/test_core.mjs', 'node tests/test_phase3.mjs', 'python tests/test_evidence_contract.py'):
        if command not in readme:
            errors.append(f'README missing test command: {command}')
        if command not in workflow:
            errors.append(f'GitHub Actions missing test command: {command}')

if errors:
    print('SMART Camel AI MVP validation failed:')
    for error in errors:
        print(f' - {error}')
    sys.exit(1)

print('SMART Camel AI MVP validation passed.')
print('Required files: OK')
print('Registered feature records: 245')
print('Feature identifier sequence: F001-F245')
print('Acquisition registry: historical F001-F243 + Phase 4 F244-F245 = 245')
print('Phase 4 source reconciliation: F244-F245 documented')
print('Reproducible demo scenarios: D01-D10 complete')
print('Evidence records: EVD-001-EVD-020 complete')
print('Strategic capability evidence: 12/12 Grade A')
print('Known limitations: 23 Arabic + 23 English items')
print('Shared runtime/test core logic: Phase 2 + Phase 3 OK')
print('Algorithm/engine registry declaration: 29 source-documented names')
print('System family declaration: 20 canonical families')
print('Arabic and English presentation markers: OK')
