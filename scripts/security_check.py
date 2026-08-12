from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_DIRS = {'.git', '.idea', '.vscode', '__pycache__', 'node_modules'}
FORBIDDEN_FILE_NAMES = {'.env', '.env.local', '.env.production', '.npmrc'}
FORBIDDEN_SUFFIXES = {'.pem', '.key', '.p12', '.pfx', '.jks', '.keystore'}
TEXT_SUFFIXES = {'.md', '.py', '.js', '.mjs', '.html', '.css', '.yml', '.yaml', '.json', '.txt'}

SECRET_PATTERNS = [
    ('private key block', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),
    ('GitHub token', re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}\b')),
    ('AWS access key', re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
    ('Google API key', re.compile(r'\bAIza[0-9A-Za-z_-]{30,}\b')),
    ('Slack token', re.compile(r'\bxox[baprs]-[0-9A-Za-z-]{10,}\b')),
]

errors = []
scanned = 0

for path in ROOT.rglob('*'):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDED_DIRS for part in rel.parts):
        continue

    if path.name in FORBIDDEN_FILE_NAMES:
        errors.append(f'Forbidden sensitive file tracked: {rel}')
    if path.suffix.lower() in FORBIDDEN_SUFFIXES:
        errors.append(f'Forbidden key/credential file tracked: {rel}')

    if path.suffix.lower() not in TEXT_SUFFIXES:
        continue

    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    scanned += 1

    for label, pattern in SECRET_PATTERNS:
        if pattern.search(text):
            errors.append(f'Potential {label} detected in {rel}')

index = (ROOT / 'index.html').read_text(encoding='utf-8')
external_scripts = re.findall(r'<script[^>]+src=["\']https?://', index, flags=re.IGNORECASE)
external_styles = re.findall(r'<link[^>]+href=["\']https?://', index, flags=re.IGNORECASE)
if external_scripts:
    errors.append('index.html contains external runtime script dependencies')
if external_styles:
    errors.append('index.html contains external runtime stylesheet dependencies')

if errors:
    print('SMART Camel AI security release check failed:')
    for error in errors:
        print(f' - {error}')
    sys.exit(1)

print('SMART Camel AI security release check passed.')
print(f'Text files scanned: {scanned}')
print('High-confidence secret patterns: none detected')
print('Forbidden credential/key files: none detected')
print('External runtime scripts/stylesheets: none detected')
