from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    'readme': ROOT / 'README.md',
    'manifest': ROOT / 'docs' / 'ACQUISITION_RELEASE_MANIFEST.md',
    'deployment': ROOT / 'docs' / 'LIVE_DEMO_DEPLOYMENT.md',
    'verification': ROOT / 'docs' / 'LIVE_DEMO_VERIFICATION.md',
    'release_notes': ROOT / 'docs' / 'RELEASE_NOTES_v1.0-acquisition-demo.md',
    'release': ROOT / 'docs' / 'RELEASE_READINESS.md',
    'phase4': ROOT / 'docs' / 'PHASE4_245_RECONCILIATION.md',
    'algorithms': ROOT / 'docs' / 'ALGORITHM_ENGINE_REGISTRY.md',
    'families': ROOT / 'docs' / 'SYSTEM_FAMILIES.md',
    'strategic': ROOT / 'docs' / 'STRATEGIC_EVIDENCE_MATRIX.md',
    'security': ROOT / 'docs' / 'SECURITY.md',
    'dependency': ROOT / 'docs' / 'DEPENDENCY_AND_LICENSE_REVIEW.md',
    'workflow': ROOT / '.github' / 'workflows' / 'validate.yml',
}

CURRENT_RELEASE_ABSENCE = (
    ROOT / 'package.json', ROOT / 'package-lock.json', ROOT / 'yarn.lock', ROOT / 'pnpm-lock.yaml',
    ROOT / 'requirements.txt', ROOT / 'pyproject.toml', ROOT / 'Pipfile', ROOT / 'poetry.lock',
    ROOT / 'LICENSE', ROOT / 'LICENSE.md', ROOT / 'LICENSE.txt',
    ROOT / '.github' / 'workflows' / 'pages.yml',
)

errors = []
texts = {}

for key, path in FILES.items():
    if not path.exists():
        errors.append(f'Missing release-readiness file: {path.relative_to(ROOT)}')
        continue
    texts[key] = path.read_text(encoding='utf-8')

if not (ROOT / '.nojekyll').exists():
    errors.append('Missing .nojekyll required by branch-based GitHub Pages publishing')

for path in CURRENT_RELEASE_ABSENCE:
    if path.exists():
        errors.append(
            f'Current release boundary expects {path.relative_to(ROOT)} to remain absent; '
            'update release diligence before introducing it'
        )

for marker in (
    '245 canonical capabilities',
    '29 source-documented named algorithms/engines',
    '20 canonical system families',
    '12/12 selected strategic capabilities at Evidence Grade A',
    'Acquisition Demonstrator Release package',
):
    if marker not in texts.get('manifest', ''):
        errors.append(f'Acquisition manifest missing marker: {marker}')

for marker in (
    'F244', 'F245',
    'Genetic Breeding with Environmental Impact Analysis',
    'Positive Environmental Impact Evaluation for Camel Breeding',
):
    if marker not in texts.get('phase4', ''):
        errors.append(f'Phase 4 reconciliation missing: {marker}')

release_text = texts.get('release', '')
for gate in range(1, 16):
    token = f'G{gate:02d}'
    if token not in release_text:
        errors.append(f'Release readiness matrix missing gate {token}')

if 'G08 — Live Stable Demo | Ready' not in release_text:
    errors.append('G08 must be Ready after verified live GitHub Pages deployment')
if 'G09 — Fixed Acquisition Release Tag | Ready to publish' not in release_text:
    errors.append('G09 must remain Ready to publish until the fixed tag is created')

live_url = 'https://maksr2030.github.io/SMART-Camel-AI-MVP/'
for key in ('readme', 'manifest', 'deployment', 'verification', 'release_notes'):
    if live_url not in texts.get(key, ''):
        errors.append(f'{FILES[key].relative_to(ROOT)} missing verified live URL')

for marker in ('`built`', '`main`', '`/(root)`', 'Public', 'HTTPS'):
    if marker not in texts.get('verification', ''):
        errors.append(f'Live demo verification missing marker: {marker}')

for marker in ('main/(root)', '.nojekyll', 'G08'):
    if marker not in texts.get('deployment', ''):
        errors.append(f'Live deployment document missing marker: {marker}')

if '29 source-documented named algorithms and engines' not in texts.get('algorithms', ''):
    errors.append('Algorithm registry must retain the normalized 29-name declaration')
if '20 canonical system families' not in texts.get('families', ''):
    errors.append('System-family document must retain the 20-family declaration')
if '12 من 12 قدرة استراتيجية = Grade A Evidence' not in texts.get('strategic', ''):
    errors.append('Strategic evidence matrix must retain the 12/12 Grade A declaration')
if 'scripts/security_check.py' not in texts.get('security', ''):
    errors.append('Security baseline must document automated public security check')
if 'No public `LICENSE` file' not in texts.get('dependency', ''):
    errors.append('Dependency/license review must preserve the public licensing boundary')

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

for marker in ('F001-F245', 'v1.0-acquisition-demo'):
    if marker not in texts.get('release_notes', ''):
        errors.append(f'Release notes missing marker: {marker}')

# Protect buyer-facing release documents from reverting to 243 as the current scope.
stale_current_patterns = [
    re.compile(r'current[^\n]{0,80}\b243\b', re.IGNORECASE),
    re.compile(r'الحالي[^\n]{0,80}\b243\b'),
]
for key in ('readme', 'manifest', 'release', 'release_notes'):
    text = texts.get(key, '')
    for pattern in stale_current_patterns:
        match = pattern.search(text)
        if match and 'historical' not in match.group(0).lower() and 'تاريخ' not in match.group(0):
            errors.append(f'{FILES[key].relative_to(ROOT)} may present 243 as current scope')
            break

if errors:
    print('SMART Camel AI acquisition release check failed:')
    for error in errors:
        print(f' - {error}')
    sys.exit(1)

print('SMART Camel AI acquisition release check passed.')
print('Canonical scope: F001-F245')
print('Algorithms / system families: 29 / 20')
print('Strategic evidence: 12/12 Grade A')
print('Live demo G08: Ready')
print('GitHub Pages source: main/(root), branch publishing')
print('Custom Pages workflow: absent by design')
print('.nojekyll: present')
print('G09: Ready to publish v1.0-acquisition-demo')
print('CI release commands: complete')
