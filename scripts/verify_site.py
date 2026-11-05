# scripts/verify_site.py
import os
import re

html_files = [
    'index.html',
    'ourmachine.html',
    'services.html',
    'contact.html'
]

errors = []
total_links = 0
total_images = 0

for file in html_files:
    if not os.path.exists(file):
        errors.append(f'Missing file: {file}')
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check images
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    for src in img_srcs:
        total_images += 1
        if src.startswith(('http://', 'https://', 'data:')):
            continue
        clean_src = src.split('?')[0].split('#')[0]
        if not os.path.exists(clean_src):
            errors.append(f'[{file}] Missing image: {clean_src}')
            
    # Check lightbox data-lightbox-src
    lb_srcs = re.findall(r'data-lightbox-src=["\']([^"\']+)["\']', html)
    for src in lb_srcs:
        if src.startswith(('http://', 'https://', 'data:')):
            continue
        clean_src = src.split('?')[0].split('#')[0]
        if not os.path.exists(clean_src):
            errors.append(f'[{file}] Missing lightbox target: {clean_src}')

    # Check internal links
    hrefs = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', html)
    for href in hrefs:
        total_links += 1
        if href.startswith(('http://', 'https://', 'tel:', 'mailto:', '#', 'javascript:')):
            continue
        page = href.split('?')[0].split('#')[0]
        if page and not os.path.exists(page):
            errors.append(f'[{file}] Broken link: {href} -> {page}')

print(f'Checked {len(html_files)} files. Total links checked: {total_links}, Total images checked: {total_images}')
if errors:
    print('Found errors:')
    for err in errors:
        print(' -', err)
else:
    print('SUCCESS! All images, lightbox targets, and internal navigation links verified without issues!')
