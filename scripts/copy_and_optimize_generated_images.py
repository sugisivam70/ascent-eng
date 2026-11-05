# copy_and_optimize_generated_images.py
import os
import shutil
from PIL import Image

artifact_dir = r"C:\Users\Asus\.gemini\antigravity\brain\7dc31b2e-f965-4f67-b4c4-07963fd21d8f"
dest_dir = r"img\generated"
os.makedirs(dest_dir, exist_ok=True)

mappings = {
    "shop_floor_overview_1793861149102.jpg": "shop-floor-overview.jpg",
    "cnc_operation_spindle_1793861169361.jpg": "cnc-operation-spindle.jpg",
    "vmc_machining_environment_1793861191094.jpg": "vmc-machining-environment.jpg",
    "precision_components_inspection_1793861212061.jpg": "precision-components-inspection.jpg",
    "operator_production_console_1793861236897.jpg": "operator-production-console.jpg",
    "metrology_quality_measurement_1793861261696.jpg": "metrology-quality-measurement.jpg",
    "aerospace_component_machining_1793861287507.jpg": "aerospace-component-machining.jpg",
    "equipment_tooling_closeup_1793861316161.jpg": "equipment-tooling-closeup.jpg",
}

for src_name, dst_name in mappings.items():
    src_path = os.path.join(artifact_dir, src_name)
    dst_path = os.path.join(dest_dir, dst_name)
    dst_webp = os.path.join(dest_dir, dst_name.replace(".jpg", ".webp"))
    
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        with Image.open(dst_path) as im:
            im.save(dst_webp, "WEBP", quality=90)
        print(f"Copied & converted: {dst_name} ({os.path.getsize(dst_path)} bytes)")
    else:
        print(f"Warning: {src_path} not found!")

print("All generated images transferred to img/generated/ successfully!")
