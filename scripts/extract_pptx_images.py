# extract_pptx_images.py
import zipfile
import os
from PIL import Image

pptx_path = r'C:\Users\Asus\Downloads\Profile SKDM MILLS.pptx'
dest_dir = r'company-profile\images\pptx'
os.makedirs(dest_dir, exist_ok=True)

with zipfile.ZipFile(pptx_path, 'r') as z:
    for filename in z.namelist():
        if filename.startswith('ppt/media/'):
            base = os.path.basename(filename)
            target = os.path.join(dest_dir, base)
            with open(target, 'wb') as f:
                f.write(z.read(filename))

print(f"Extracted all images into {dest_dir}")

# Analyze extracted images
for f in sorted(os.listdir(dest_dir)):
    p = os.path.join(dest_dir, f)
    try:
        with Image.open(p) as img:
            print(f"{f}: format={img.format}, size={img.size}, bytes={os.path.getsize(p)}")
    except Exception as e:
        print(f"{f}: error {e}")
