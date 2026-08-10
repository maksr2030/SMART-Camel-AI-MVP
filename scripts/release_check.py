from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    'readme': ROOT / 'README.md',
    'overview': ROOT / 'docs' / 'PUBLIC_OVERVIEW.md',
    'source': ROOT / 'docs' / 'SOURCE_RECONCILIATION.md',
    'acquisition': ROOT / 'docs' / 'ACQUISITION_TECHNICAL_OVERVIEW.md',
    'evidence': ROOT / 'docs' / 'EVIDENCE.md',
    'families': ROOT / 'docs' / 'SYSTEM_FAMILIES.md',
    'phase4': ROOT / 'docs' / 'PHASE4_245_RECONCILIATION.md',
    'demos': ROOT / 'docs' / 'DEMO_SCENARIOS.md',
    'limitations': ROOT / 'docs' / 'KNOWN_LIMITATIONS.md',
    'ip': ROOT / 'docs' / 'IP_NOTICE.md',
    'catalog': ROOT / 'docs' / 'EVIDENCE_CATALOG.md',
    'algorithms': ROOT / 'docs' / 'ALGORITHM_ENGINE_REGISTRY.md',
    'architecture': ROOT / 'docs' / 'ARCHITECTURE.md',
    'security': ROOT / 'docs' / 'SECURITY.md',
    'release': ROOT / 'docs' / 'RELEASE_READINESS.md',
    'dependency': ROOT / 'docs' / 'DEPENDENCY_AND_LICENSE_REVIEW.md',
    'workflow': ROOT / '.github' / 'workflows' / 'validate.yml',
}

CURRENT_RELEASE_ABSENCE = (
    ROOT / 'package.json',
    ROOT / 'package-lock.json',
    ROOT / 'yarn.lock',
    ROOT / 'pnpm-lock.yaml',
    ROOT / 'requirements.txt',
    ROOT / 'pyproject.toml',
    ROOT / 'Pipfile',
    ROOT / 'poetry.lock',
    ROOT / 'LICENSE',
    ROOT / 'LICENSE.md',
    ROOT / 'LICENSE.txt',
)

errors = []
texts = {}
for key, path in FILES.items():
    if not path.exists():
        errors.append(f'Missing release-readiness file: {path.relative_to(ROOT)}')
        continue
    texts[key] = path.read_text(encoding='utf-8')

for path in CURRENT_RELEASE_ABSENCE:
    if path.exists():
        errors.append(
            f'Current acquisition-release boundary expects {path.name} to remain absent; '
            'update dependency/license diligence before introducing it'
        )

CURRENT_SCOPE_DOCS = (
    'readme', 'overview', 'source', 'acquisition', 'evidence', 'families', 'phase4',
    'demos', 'limitations', 'ip', 'catalog', 'algorithms', 'architecture'
)
for key in CURRENT_SCOPE_DOCS:
    text = texts.get(key, '')
    if '245' not in text or 'F245' not in text:
        errors.append(f'{FILES[key].relative_to(ROOT)} must state the current 245/F245 scope')

for marker in (
    'F244',
    'F245',
    'Genetic Breeding with Environmental Impact Analysis',
    'Positive Environmental Impact Evaluation for Camel Breeding',
):
    if marker not in texts.get('phase4', ''):
        errors.append(f'Phase 4 reconciliation missing: {marker}')

if '29 source-documented named algorithms and engines' not in texts.get('algorithms', ''):
    errors.append('Algorithm registry must retain the normalized 29-name declaration')
if '20 canonical system families' not in texts.get('families', ''):
    errors.append('System-family document must retain the 20-family declaration')
if 'scripts/security_check.py' not in texts.get('security', ''):
    errors.append('Security baseline must document the Phase 4 automated security check')
if 'No public `LICENSE` file' not in texts.get('dependency', ''):
    errors.append('Dependency/license review must preserve the public licensing boundary')
for marker in ('`package.json`', '`requirements.txt`', '`pyproject.toml`', '`LICENSE.md`', '`LICENSE.txt`'):
    if marker not in texts.get('dependency', ''):
        errors.append(f'Dependency/license review must document current absence of {marker}')

release_text = texts.get('release', '')
for gate in range(1, 16):
    token = f'G{gate:02d}'
    if token not in release_text:
        errors.append(f'Release readiness matrix missing gate {token}')

if 'Live Stable Demo | Pending' not in release_text:
    errors.append('Release readiness must keep live stable demo as Pending until independently verified')
if 'Fixed Acquisition Release Tag | Pending' not in release_text:
    errors.append('Release readiness must keep acquisition tag as Pending until live demo + CI verification')

workflow = texts.get('workflow', '')
for command in (
    'python scripts/validate.py',
    'node tests/test_core.mjs',
    'node tests/test_phase3.mjs',
    'node tests/test_phase4.mjs',
    'python tests/test_evidence_contract.py',
    'python scripts/security_check.py',
    'python scripts/release_check.py',
):
    if command not in workflow:
        errors.append(f'GitHub Actions missing release command: {command}')

readme = texts.get('readme', '')
for command in (
    'python scripts/security_check.py',
    'python scripts/release_check.py',
):
    if command not in readme:
        errors.append(f'README missing release command: {command}')

# Protect current-scope documents from accidentally reverting to a 243-only current scope.
# Historical/baseline mentions are allowed when explicitly labelled historical.
stale_current_patterns = [
    re.compile(r'current[^\n]{0,80}\b243\b', re.IGNORECASE),
    re.compile(r'الحالي[^\n]{0,80}\b243\b'),
]
for key in CURRENT_SCOPE_DOCS:
    text = texts.get(key, '')
    for pattern in stale_current_patterns:
        match = pattern.search(text)
        if match and 'historical' not in match.group(0).lower() and 'تاريخ' not in match.group(0):
            errors.append(f'{FILES[key].relative_to(ROOT)} may still present 243 as the current scope: {match.group(0)!r}')
            break

if errors:
    print('SMART Camel AI acquisition release check failed:')
    for error in errors:
        print(f' - {error}')
    sys.exit(1)

print('SMART Camel AI acquisition release check passed.')
print('Current public/DD scope markers: F001-F245 consistent')
print('Phase 4 reconciliation markers: F244-F245 present')
print('Algorithms/system families: 29 / 20 preserved')
print('Verified no-manifest/no-lockfile/no-public-license boundary: preserved')
print('Security and licensing boundaries: present')
print('Release readiness gates: G01-G15 present')
print('Live demo and final release tag remain correctly Pending')
print('CI release commands: complete')
