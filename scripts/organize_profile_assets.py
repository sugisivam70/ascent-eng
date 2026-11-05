# organize_profile_assets.py
import os
import shutil

dest_dir = r'company-profile\images'
os.makedirs(os.path.join(dest_dir, 'components'), exist_ok=True)
os.makedirs(os.path.join(dest_dir, 'shopfloor'), exist_ok=True)
os.makedirs(os.path.join(dest_dir, 'machines'), exist_ok=True)

# 1. Copy authentic Ascent shop floor images
shopfloor_src = r'img\ascent\shop floor'
if os.path.exists(shopfloor_src):
    for f in os.listdir(shopfloor_src):
        src_p = os.path.join(shopfloor_src, f)
        if os.path.isfile(src_p):
            # Clean filename
            clean_name = f.replace(' ', '_').replace('(', '').replace(')', '')
            shutil.copy2(src_p, os.path.join(dest_dir, 'shopfloor', clean_name))

# Copy the processed shop floor photos too
for name in ['shop-floor-featured.jpg', 'shop-floor-wide.jpg', 'shop-floor-aisle.jpg']:
    p = os.path.join(r'img\ascent', name)
    if os.path.exists(p):
        shutil.copy2(p, os.path.join(dest_dir, 'shopfloor', name))

# 2. Copy component images from Ascent PDF
components_src = r'img\ascent\components'
if os.path.exists(components_src):
    for f in os.listdir(components_src):
        src_p = os.path.join(components_src, f)
        if os.path.isfile(src_p):
            shutil.copy2(src_p, os.path.join(dest_dir, 'components', 'ascent_' + f))

# 3. Copy components from SKDM PPTX
pptx_dir = r'company-profile\images\pptx'
if os.path.exists(pptx_dir):
    # PPTX images mapping
    # image4: shopfloor overview
    # image5: VMC 1 (STM VD 610)
    # image6: VMC 2 (STM VD 850)
    # image9 to image34: components & sample parts
    shutil.copy2(os.path.join(pptx_dir, 'image4.jpeg'), os.path.join(dest_dir, 'shopfloor', 'skdm_shopfloor_overview.jpeg'))
    shutil.copy2(os.path.join(pptx_dir, 'image5.jpeg'), os.path.join(dest_dir, 'machines', 'vmc_machining_center_01.jpeg'))
    shutil.copy2(os.path.join(pptx_dir, 'image6.jpeg'), os.path.join(dest_dir, 'machines', 'vmc_machining_center_02.jpeg'))
    
    comp_imgs = ['image9.jpeg', 'image10.jpg', 'image11.jpg', 'image12.jpg', 'image13.jpg', 
                 'image14.jpg', 'image15.jpg', 'image16.jpg', 'image17.jpg', 'image18.jpg', 
                 'image19.jpg', 'image20.png', 'image21.jpg', 'image22.jpg', 'image23.jpg', 
                 'image24.jpg', 'image25.jpg', 'image26.jpg', 'image27.jpg', 'image28.jpg', 
                 'image29.jpg', 'image30.jpeg', 'image31.jpeg', 'image32.jpeg', 'image33.jpeg', 'image34.jpeg']
    
    for c in comp_imgs:
        p = os.path.join(pptx_dir, c)
        if os.path.exists(p):
            shutil.copy2(p, os.path.join(dest_dir, 'components', 'skdm_' + c))

# 4. Copy machine images from img/generated
for m in ['machine-hurco-5axis.jpg', 'machine-yantrang-850.jpg', 'machine-twinhorn-vmc.jpg', 'machine-cosmos-sm50.jpg', 'machine-cosmos-emtharangi.jpg']:
    p = os.path.join(r'img\generated', m)
    if os.path.exists(p):
        shutil.copy2(p, os.path.join(dest_dir, 'machines', m))

print("Assets organized successfully into company-profile/images/")
