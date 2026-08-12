from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FEATURES = 245
EXPECTED_BASE_REGISTRY = 243
EXPECTED_DEMOS = 10
EXPECTED_EVIDENCE = 20
EXPECTED_LIMITATIONS = 23

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

REQUIRED_FILES = [
    ROOT / 'index.html', ROOT / '.nojekyll', ROOT / 'README.md',
    ROOT / 'app' / 'styles.css', ROOT / 'app' / 'core.js', ROOT / 'app' / 'app.js',
    *FEATURE_FILES,
    ROOT / 'docs' / 'FEATURE_REGISTRY.md',
    ROOT / 'docs' / 'DEMO_SCENARIOS.md',
    ROOT / 'docs' / 'KNOWN_LIMITATIONS.md',
    ROOT / 'docs' / 'SECURITY.md',
    ROOT / 'docs' / 'IP_NOTICE.md',
    ROOT / 'docs' / 'ACQUISITION_TECHNICAL_OVERVIEW.md',
    ROOT / 'docs' / 'ACQUISITION_RELEASE_MANIFEST.md',
    ROOT / 'docs' / 'EVIDENCE_CATALOG.md',
    ROOT / 'docs' / 'PHASE3_GRADE_A_EVIDENCE.md',
    ROOT / 'docs' / 'STRATEGIC_EVIDENCE_MATRIX.md',
    ROOT / 'docs' / 'PHASE4_245_RECONCILIATION.md',
    ROOT / 'docs' / 'DEPENDENCY_AND_LICENSE_REVIEW.md',
    ROOT / 'docs' / 'RELEASE_READINESS.md',
    ROOT / 'docs' / 'LIVE_DEMO_DEPLOYMENT.md',
    ROOT / 'docs' / 'LIVE_DEMO_VERIFICATION.md',
    ROOT / 'docs' / 'RELEASE_NOTES_v1.0-acquisition-demo.md',
    ROOT / 'docs' / 'ARCHITECTURE.md', ROOT / 'docs' / 'EVIDENCE.md',
    ROOT / 'docs' / 'PUBLIC_OVERVIEW.md', ROOT / 'docs' / 'SOURCE_RECONCILIATION.md',
    ROOT / 'docs' / 'ALGORITHM_ENGINE_REGISTRY.md', ROOT / 'docs' / 'SYSTEM_FAMILIES.md',
    ROOT / 'tests' / 'test_core.mjs', ROOT / 'tests' / 'test_phase3.mjs',
    ROOT / 'tests' / 'test_phase4.mjs', ROOT / 'tests' / 'test_evidence_contract.py',
    ROOT / 'scripts' / 'security_check.py', ROOT / 'scripts' / 'release_check.py',
    ROOT / '.github' / 'workflows' / 'validate.yml',
]

errors = []
for path in REQUIRED_FILES:
    if not path.exists():
        errors.append(f'Missing required file: {path.relative_to(ROOT)}')

PAGES_WORKFLOW = ROOT / '.github' / 'workflows' / 'pages.yml'
if PAGES_WORKFLOW.exists():
    errors.append('Custom Pages workflow must remain absent; publishing is from main/(root)')

if not errors:
    def read(path):
        return path.read_text(encoding='utf-8')

    index = read(ROOT / 'index.html')
    app = read(ROOT / 'app' / 'app.js')
    core = read(ROOT / 'app' / 'core.js')
    readme = read(ROOT / 'README.md')
    registry = read(ROOT / 'docs' / 'FEATURE_REGISTRY.md')
    reconciliation = read(ROOT / 'docs' / 'PHASE4_245_RECONCILIATION.md')
    demos = read(ROOT / 'docs' / 'DEMO_SCENARIOS.md')
    limitations = read(ROOT / 'docs' / 'KNOWN_LIMITATIONS.md')
    catalog = read(ROOT / 'docs' / 'EVIDENCE_CATALOG.md')
    phase3 = read(ROOT / 'docs' / 'PHASE3_GRADE_A_EVIDENCE.md')
    strategic = read(ROOT / 'docs' / 'STRATEGIC_EVIDENCE_MATRIX.md')
    algorithms = read(ROOT / 'docs' / 'ALGORITHM_ENGINE_REGISTRY.md')
    families = read(ROOT / 'docs' / 'SYSTEM_FAMILIES.md')
    security = read(ROOT / 'docs' / 'SECURITY.md')
    ip_notice = read(ROOT / 'docs' / 'IP_NOTICE.md')
    acquisition = read(ROOT / 'docs' / 'ACQUISITION_TECHNICAL_OVERVIEW.md')
    dependency = read(ROOT / 'docs' / 'DEPENDENCY_AND_LICENSE_REVIEW.md')
    release = read(ROOT / 'docs' / 'RELEASE_READINESS.md')
    verification = read(ROOT / 'docs' / 'LIVE_DEMO_VERIFICATION.md')
    workflow = read(ROOT / '.github' / 'workflows' / 'validate.yml')
    feature_text = '\n'.join(read(path) for path in FEATURE_FILES)

    expected_ids = [f'{i:03d}' for i in range(1, EXPECTED_FEATURES + 1)]
    feature_ids = re.findall(r"\['F(\d{3})'", feature_text)
    if feature_ids != expected_ids:
        errors.append('Feature identifiers must be a continuous F001-F245 sequence')
    if len(set(feature_ids)) != EXPECTED_FEATURES:
        errors.append('Capability IDs must be unique across 245 records')

    base_ids = re.findall(r'^\| F(\d{3}) \|', registry, flags=re.MULTILINE)
    if base_ids != [f'{i:03d}' for i in range(1, EXPECTED_BASE_REGISTRY + 1)]:
        errors.append('Historical acquisition registry must remain continuous F001-F243')
    addendum_ids = re.findall(r'^\| F(24[45]) \|', reconciliation, flags=re.MULTILINE)
    if addendum_ids != ['244', '245']:
        errors.append('Phase 4 reconciliation must contain F244 and F245')
    if base_ids + addendum_ids != expected_ids:
        errors.append('Combined acquisition scope must resolve to F001-F245')

    for marker in (
        'Genetic Breeding with Environmental Impact Analysis',
        'Positive Environmental Impact Evaluation for Camel Breeding',
        '245 distinct source-backed capability records',
    ):
        if marker not in reconciliation:
            errors.append(f'Phase 4 reconciliation missing marker: {marker}')

    demo_ids = re.findall(r'^### D(\d{2}) —', demos, flags=re.MULTILINE)
    if demo_ids != [f'{i:02d}' for i in range(1, EXPECTED_DEMOS + 1)]:
        errors.append('Demo scenarios must be continuous D01-D10')

    evidence_ids = (
        re.findall(r'^### EVD-(\d{3}) —', catalog, flags=re.MULTILINE)
        + re.findall(r'^### EVD-(\d{3}) —', phase3, flags=re.MULTILINE)
    )
    if evidence_ids != [f'{i:03d}' for i in range(1, EXPECTED_EVIDENCE + 1)]:
        errors.append('Evidence IDs must be continuous EVD-001-EVD-020')

    if '12 من 12 قدرة استراتيجية = Grade A Evidence' not in strategic:
        errors.append('Strategic evidence matrix must retain 12/12 Grade A declaration')
    if re.findall(r'\| S\d{2} \| F\d{3} \|[^\n]+\| B \|', strategic):
        errors.append('Strategic evidence matrix must not contain Grade B rows')

    limitation_numbers = re.findall(r'^(\d+)\. ', limitations, flags=re.MULTILINE)
    expected_limits = [str(i) for i in range(1, EXPECTED_LIMITATIONS + 1)] * 2
    if limitation_numbers != expected_limits:
        errors.append('Known limitations must retain 23 Arabic + 23 English items')
    if 'إيرادات' not in limitations or 'revenue' not in limitations.lower():
        errors.append('Known limitations must disclose absence of evidenced revenue')

    for asset in (
        'app/styles.css', 'app/data.js', 'app/source-features-091-140.js',
        'app/source-features-141-190.js', 'app/source-features-191-223.js',
        'app/source-features-224-231.js', 'app/source-features-232-235.js',
        'app/source-features-236-243.js', 'app/source-features-244-245.js',
        'app/core.js', 'app/app.js',
    ):
        if asset not in index:
            errors.append(f'index.html does not reference {asset}')
    if index.find('app/core.js') > index.find('app/app.js'):
        errors.append('app/core.js must load before app/app.js')

    for marker in (
        'core.calculateHealthRisk', 'core.filterFeatures', 'core.countStatuses',
        'core.verifyDemoCertificate', 'core.validateCamelRegistry', 'core.evaluateGeofence',
        'core.calculateMazayenScore', 'core.createAuctionState', 'core.placeDemoBid',
        'core.appendAuditEvent',
    ):
        if marker not in app:
            errors.append(f'app.js is not wired to shared core logic: {marker}')

    for marker in (
        'calculateHealthRisk', 'filterFeatures', 'countStatuses', 'verifyDemoCertificate',
        'validateCamelRegistry', 'findCamelById', 'evaluateGeofence', 'calculateMazayenScore',
        'createAuctionState', 'placeDemoBid', 'appendAuditEvent',
    ):
        if marker not in core:
            errors.append(f'core.js missing required function: {marker}')

    if 'ar:{' not in app or 'en:{' not in app:
        errors.append('Bilingual translation objects are incomplete')
    if 'العربية' not in readme or 'English' not in readme:
        errors.append('README must remain bilingual')

    if '29 source-documented named algorithms and engines' not in algorithms:
        errors.append('Algorithm registry must retain 29 source-documented names')
    if '20 canonical system families' not in families or '245 canonical capabilities' not in families:
        errors.append('System family document must retain 20 families / 245 capabilities')
    if 'scripts/security_check.py' not in security:
        errors.append('Security baseline must document automated public security check')
    if 'Chain of Title' not in ip_notice:
        errors.append('IP notice must retain Chain of Title requirements')
    if 'Claim → Canonical F-ID' not in acquisition:
        errors.append('Acquisition overview must retain evidence-chain model')
    if 'No public `LICENSE` file' not in dependency:
        errors.append('Dependency/license review must retain licensing boundary')

    for gate in range(1, 16):
        if f'G{gate:02d}' not in release:
            errors.append(f'Release readiness missing G{gate:02d}')
    if 'G08 — Live Stable Demo | Ready' not in release:
        errors.append('Release readiness must mark G08 Ready')
    if 'G09 — Fixed Acquisition Release Tag | Ready to publish' not in release:
        errors.append('Release readiness must mark G09 Ready to publish')

    for marker in ('`built`', '`main`', '`/(root)`', 'Public', 'HTTPS'):
        if marker not in verification:
            errors.append(f'Live verification missing marker: {marker}')

    required_links = (
        'docs/FEATURE_REGISTRY.md', 'docs/DEMO_SCENARIOS.md', 'docs/KNOWN_LIMITATIONS.md',
        'docs/SECURITY.md', 'docs/IP_NOTICE.md', 'docs/ACQUISITION_TECHNICAL_OVERVIEW.md',
        'docs/ACQUISITION_RELEASE_MANIFEST.md', 'docs/EVIDENCE_CATALOG.md',
        'docs/PHASE3_GRADE_A_EVIDENCE.md', 'docs/STRATEGIC_EVIDENCE_MATRIX.md',
        'docs/PHASE4_245_RECONCILIATION.md', 'docs/DEPENDENCY_AND_LICENSE_REVIEW.md',
        'docs/RELEASE_READINESS.md', 'docs/LIVE_DEMO_VERIFICATION.md',
        'docs/RELEASE_NOTES_v1.0-acquisition-demo.md',
    )
    for link in required_links:
        if link not in readme:
            errors.append(f'README does not link required diligence document: {link}')

    commands = (
        'python scripts/validate.py', 'node tests/test_core.mjs', 'node tests/test_phase3.mjs',
        'node tests/test_phase4.mjs', 'python tests/test_evidence_contract.py',
        'python scripts/security_check.py', 'python scripts/release_check.py',
    )
    for command in commands:
        if command not in readme:
            errors.append(f'README missing command: {command}')
        if command not in workflow:
            errors.append(f'GitHub Actions missing command: {command}')

if errors:
    print('SMART Camel AI validation failed:')
    for error in errors:
        print(f' - {error}')
    sys.exit(1)

print('SMART Camel AI validation passed.')
print('Canonical scope: F001-F245')
print('Historical registry + Phase 4 reconciliation: complete')
print('Demo scenarios: D01-D10')
print('Evidence: EVD-001-EVD-020')
print('Strategic evidence: 12/12 Grade A')
print('Known limitations: 23 Arabic + 23 English')
print('Live demo G08: Ready')
print('G09: Ready to publish v1.0-acquisition-demo')
print('GitHub Pages: main/(root), custom workflow absent')
print('Security/release CI commands: complete')
