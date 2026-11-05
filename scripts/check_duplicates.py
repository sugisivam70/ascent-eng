# check_duplicates.py
import re
from collections import Counter

for page in ['index.html', 'ourmachine.html', 'services.html', 'contact.html']:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    counts = Counter(imgs)
    print(f"=== {page} (Total images: {len(imgs)}) ===")
    duplicates = {k: v for k, v in counts.items() if v > 1 and not k.endswith(('logo.png', 'logo-transparent.png', 'favicon.svg'))}
    if duplicates:
        print("  DUPLICATES:")
        for k, v in duplicates.items():
            print(f"    - {k} ({v} times)")
    else:
        print("  No duplicates found within page.")
