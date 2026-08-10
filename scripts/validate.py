from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / 'index.html',
    ROOT / 'app' / 'styles.css',
    ROOT / 'app' / 'data.js',
    ROOT / 'app' / 'app.js',
    ROOT / 'docs' / 'ARCHITECTURE.md',
    ROOT / 'docs' / 'EVIDENCE.md',
    ROOT / 'docs' / 'PUBLIC_OVERVIEW.md',
    ROOT / 'README.md',
]

errors = []
for path in required:
    if not path.exists():
        errors.append(f'Missing required file: {path.relative_to(ROOT)}')

if not errors:
    index = (ROOT / 'index.html').read_text(encoding='utf-8')
    data = (ROOT / 'app' / 'data.js').read_text(encoding='utf-8')
    app = (ROOT / 'app' / 'app.js').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')

    feature_ids = re.findall(r"\['F(\d{3})'", data)
    if len(feature_ids) != 60:
        errors.append(f'Expected 60 feature records, found {len(feature_ids)}')
    if len(set(feature_ids)) != len(feature_ids):
        errors.append('Duplicate feature identifiers detected')

    for asset in ('app/styles.css', 'app/data.js', 'app/app.js'):
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
print('Registered feature records: 60')
print('Arabic and English presentation markers: OK')
