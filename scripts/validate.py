from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FEATURES = 235
FEATURE_FILES = [
    ROOT / 'app' / 'data.js',
    ROOT / 'app' / 'source-features-091-140.js',
    ROOT / 'app' / 'source-features-141-190.js',
    ROOT / 'app' / 'source-features-191-223.js',
    ROOT / 'app' / 'source-features-224-231.js',
    ROOT / 'app' / 'source-features-232-235.js',
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
    feature_text = '\n'.join(path.read_text(encoding='utf-8') for path in FEATURE_FILES)

    feature_ids = re.findall(r"\['F(\d{3})'", feature_text)
    if len(feature_ids) != EXPECTED_FEATURES:
        errors.append(f'Expected {EXPECTED_FEATURES} feature records, found {len(feature_ids)}')
    if len(set(feature_ids)) != len(feature_ids):
        errors.append('Duplicate feature identifiers detected')

    expected_sequence = [f'{i:03d}' for i in range(1, EXPECTED_FEATURES + 1)]
    if feature_ids != expected_sequence:
        errors.append('Feature identifiers are not a continuous F001-F235 sequence')

    for asset in (
        'app/styles.css',
        'app/data.js',
        'app/source-features-091-140.js',
        'app/source-features-141-190.js',
        'app/source-features-191-223.js',
        'app/source-features-224-231.js',
        'app/source-features-232-235.js',
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

if errors:
    print('SMART Camel AI MVP validation failed:')
    for error in errors:
        print(f' - {error}')
    sys.exit(1)

print('SMART Camel AI MVP validation passed.')
print('Required files: OK')
print(f'Registered feature records: {EXPECTED_FEATURES}')
print('Feature identifier sequence: F001-F235')
print('Arabic and English presentation markers: OK')
