from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FEATURES = 243
EXPECTED_DEMO_SCENARIOS = 10
EXPECTED_LIMITATIONS_PER_LANGUAGE = 23
FEATURE_FILES = [
    ROOT / 'app' / 'data.js',
    ROOT / 'app' / 'source-features-091-140.js',
    ROOT / 'app' / 'source-features-141-190.js',
    ROOT / 'app' / 'source-features-191-223.js',
    ROOT / 'app' / 'source-features-224-231.js',
    ROOT / 'app' / 'source-features-232-235.js',
    ROOT / 'app' / 'source-features-236-243.js',
]
DUE_DILIGENCE_FILES = [
    ROOT / 'docs' / 'FEATURE_REGISTRY.md',
    ROOT / 'docs' / 'DEMO_SCENARIOS.md',
    ROOT / 'docs' / 'KNOWN_LIMITATIONS.md',
    ROOT / 'docs' / 'SECURITY.md',
    ROOT / 'docs' / 'IP_NOTICE.md',
    ROOT / 'docs' / 'ACQUISITION_TECHNICAL_OVERVIEW.md',
]
required = [
    ROOT / 'index.html',
    ROOT / 'app' / 'styles.css',
    *FEATURE_FILES,
    ROOT / 'app' / 'app.js',
    ROOT / 'docs' / 'ARCHITECTURE.md',
    ROOT / 'docs' / 'EVIDENCE.md',
    ROOT / 'docs' / 'PUBLIC_OVERVIEW.md',
    ROOT / 'docs' / 'SOURCE_RECONCILIATION.md',
    ROOT / 'docs' / 'ALGORITHM_ENGINE_REGISTRY.md',
    ROOT / 'docs' / 'SYSTEM_FAMILIES.md',
    *DUE_DILIGENCE_FILES,
    ROOT / 'README.md',
]

errors = []
for path in required:
    if not path.exists():
        errors.append(f'Missing required file: {path.relative_to(ROOT)}')

if not errors:
    index = (ROOT / 'index.html').read_text(encoding='utf-8')
    app = (ROOT / 'app' / 'app.js').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    algorithms = (ROOT / 'docs' / 'ALGORITHM_ENGINE_REGISTRY.md').read_text(encoding='utf-8')
    systems = (ROOT / 'docs' / 'SYSTEM_FAMILIES.md').read_text(encoding='utf-8')
    acquisition_registry = (ROOT / 'docs' / 'FEATURE_REGISTRY.md').read_text(encoding='utf-8')
    demos = (ROOT / 'docs' / 'DEMO_SCENARIOS.md').read_text(encoding='utf-8')
    limitations = (ROOT / 'docs' / 'KNOWN_LIMITATIONS.md').read_text(encoding='utf-8')
    security = (ROOT / 'docs' / 'SECURITY.md').read_text(encoding='utf-8')
    ip_notice = (ROOT / 'docs' / 'IP_NOTICE.md').read_text(encoding='utf-8')
    acquisition_overview = (ROOT / 'docs' / 'ACQUISITION_TECHNICAL_OVERVIEW.md').read_text(encoding='utf-8')
    feature_text = '\n'.join(path.read_text(encoding='utf-8') for path in FEATURE_FILES)

    feature_ids = re.findall(r"\['F(\d{3})'", feature_text)
    if len(feature_ids) != EXPECTED_FEATURES:
        errors.append(f'Expected {EXPECTED_FEATURES} feature records, found {len(feature_ids)}')
    if len(set(feature_ids)) != len(feature_ids):
        errors.append('Duplicate feature identifiers detected')

    expected_sequence = [f'{i:03d}' for i in range(1, EXPECTED_FEATURES + 1)]
    if feature_ids != expected_sequence:
        errors.append('Feature identifiers are not a continuous F001-F243 sequence')

    acquisition_ids = re.findall(r'^\| F(\d{3}) \|', acquisition_registry, flags=re.MULTILINE)
    if len(acquisition_ids) != EXPECTED_FEATURES:
        errors.append(f'Acquisition registry must contain {EXPECTED_FEATURES} F-ID rows, found {len(acquisition_ids)}')
    if acquisition_ids != expected_sequence:
        errors.append('Acquisition registry rows are not a continuous F001-F243 sequence')

    scenario_ids = re.findall(r'^### D(\d{2}) —', demos, flags=re.MULTILINE)
    expected_scenarios = [f'{i:02d}' for i in range(1, EXPECTED_DEMO_SCENARIOS + 1)]
    if scenario_ids != expected_scenarios:
        errors.append('Demo scenarios must be a continuous D01-D10 sequence')

    limitation_numbers = re.findall(r'^(\d+)\. ', limitations, flags=re.MULTILINE)
    expected_limitation_numbers = [str(i) for i in range(1, EXPECTED_LIMITATIONS_PER_LANGUAGE + 1)] * 2
    if limitation_numbers != expected_limitation_numbers:
        errors.append('Known limitations must contain continuous 1-23 lists in Arabic and English')
    if 'إيرادات' not in limitations or 'revenue' not in limitations.lower():
        errors.append('Known limitations must explicitly disclose the absence of evidenced revenue')

    for asset in (
        'app/styles.css',
        'app/data.js',
        'app/source-features-091-140.js',
        'app/source-features-141-190.js',
        'app/source-features-191-223.js',
        'app/source-features-224-231.js',
        'app/source-features-232-235.js',
        'app/source-features-236-243.js',
        'app/app.js',
    ):
        if asset not in index:
            errors.append(f'index.html does not reference {asset}')

    bilingual_markers = [
        ('Arabic translation object', 'ar:{' in app),
        ('English translation object', 'en:{' in app),
        ('Arabic README content', 'العربية' in readme),
        ('English README content', 'English' in readme),
    ]
    for label, ok in bilingual_markers:
        if not ok:
            errors.append(f'Missing {label}')

    if '29 source-documented named algorithms and engines' not in algorithms:
        errors.append('Algorithm registry does not declare the 29 source-documented named algorithms and engines')
    if '20 canonical system families' not in systems:
        errors.append('System family document does not declare the 20 canonical system families')
    if 'E4' not in security or 'Threat Model' not in security:
        errors.append('Security baseline/threat model markers are missing')
    if 'Chain of Title' not in ip_notice:
        errors.append('IP notice does not include Chain of Title diligence requirements')
    if 'Claim → Canonical F-ID' not in acquisition_overview:
        errors.append('Acquisition technical overview does not declare the evidence-chain model')

    due_diligence_links = [
        'docs/FEATURE_REGISTRY.md',
        'docs/DEMO_SCENARIOS.md',
        'docs/KNOWN_LIMITATIONS.md',
        'docs/SECURITY.md',
        'docs/IP_NOTICE.md',
        'docs/ACQUISITION_TECHNICAL_OVERVIEW.md',
    ]
    for link in due_diligence_links:
        if link not in readme:
            errors.append(f'README does not link required due-diligence document: {link}')

if errors:
    print('SMART Camel AI MVP validation failed:')
    for error in errors:
        print(f' - {error}')
    sys.exit(1)

print('SMART Camel AI MVP validation passed.')
print('Required files: OK')
print(f'Registered feature records: {EXPECTED_FEATURES}')
print('Feature identifier sequence: F001-F243')
print('Acquisition feature registry: F001-F243 complete')
print('Reproducible demo scenarios: D01-D10 complete')
print('Known limitations: 23 Arabic + 23 English items')
print('Due-diligence foundation documents: OK')
print('Algorithm/engine registry declaration: 29 source-documented names')
print('System family declaration: 20 canonical families')
print('Arabic and English presentation markers: OK')