# -*- coding: utf-8 -*-
import re
import os

with open('company-profile/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check img src
srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
print(f"Total <img> src elements: {len(srcs)}")
missing_srcs = []
for src in srcs:
    target = os.path.normpath(os.path.join('company-profile', src))
    if not os.path.exists(target):
        missing_srcs.append(src)

print(f"Missing img srcs: {len(missing_srcs)}")
for m in missing_srcs:
    print(f"  Missing: {m}")

# Check data-cp-lightbox
lb_srcs = re.findall(r'data-cp-lightbox=["\']([^"\']+)["\']', content)
print(f"Total data-cp-lightbox elements: {len(lb_srcs)}")
missing_lbs = []
for src in lb_srcs:
    target = os.path.normpath(os.path.join('company-profile', src))
    if not os.path.exists(target):
        missing_lbs.append(src)

print(f"Missing lightbox srcs: {len(missing_lbs)}")
for m in missing_lbs:
    print(f"  Missing lightbox: {m}")
