# update_all_pages_images.py

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Hero background: use shop-floor-overview.jpg
    html = html.replace(
        'src="img/generated/hero-facility-cinematic.jpg"\n            alt="Ascent Engineering Modern CNC Manufacturing Facility"',
        'src="img/generated/shop-floor-overview.jpg"\n            alt="Ascent Engineering Modern CNC Manufacturing Facility Overview"'
    )

    # 2. Manufacturing Capabilities Card 1 (5-Axis): use aerospace-component-machining.jpg
    html = html.replace(
        'src="img/generated/machine-hurco-5axis.jpg"\n                  alt="5-Axis CNC Machining of Complex Engineered Component"',
        'src="img/generated/aerospace-component-machining.jpg"\n                  alt="5-Axis CNC Machining of Complex Engineered Aerospace Component"'
    )
    html = html.replace(
        'data-lightbox-src="img/generated/machine-hurco-5axis.jpg" data-lightbox-title="Hurco VC 500i 5-Axis CNC Machining"',
        'data-lightbox-src="img/generated/aerospace-component-machining.jpg" data-lightbox-title="Simultaneous 5-Axis Aerospace Component Machining"'
    )

    # 3. Manufacturing Capabilities Card 2 (3-Axis VMC): use vmc-machining-environment.jpg
    # (previously it was shop-floor-featured.jpg, which duplicated About section!)
    html = html.replace(
        'src="img/ascent/shop-floor-featured.jpg"\n                  alt="3-Axis VMC Machining Fleet at Ascent Engineering"',
        'src="img/generated/vmc-machining-environment.jpg"\n                  alt="3-Axis VMC Machining Station Environment at Ascent Engineering"'
    )
    html = html.replace(
        'data-lightbox-src="img/ascent/shop-floor-featured.jpg" data-lightbox-title="Ascent Engineering Production VMC Fleet"',
        'data-lightbox-src="img/generated/vmc-machining-environment.jpg" data-lightbox-title="Ascent Engineering 3-Axis VMC Production Environment"'
    )

    # 4. Manufacturing Capabilities Card 3 (CNC Tapping): use equipment-tooling-closeup.jpg
    html = html.replace(
        'src="img/generated/cnc-cutting-coolant.jpg"\n                  alt="CNC Tapping and Milling Operations with Flood Coolant"',
        'src="img/generated/equipment-tooling-closeup.jpg"\n                  alt="Precision CNC Rigid Tapping & Tooling Equipment Close-up"'
    )
    html = html.replace(
        'data-lightbox-src="img/generated/cnc-cutting-coolant.jpg" data-lightbox-title="Synchronized CNC Rigid Tapping"',
        'data-lightbox-src="img/generated/equipment-tooling-closeup.jpg" data-lightbox-title="Precision CNC Tooling and Synchronized Rigid Tapping"'
    )

    # 5. Quality Metrology Lab: use metrology-quality-measurement.jpg
    html = html.replace(
        'src="img/generated/metrology-inspection-lab.jpg"\n                alt="Quality Inspection and Dimensional Measurement Lab at Ascent Engineering"',
        'src="img/generated/metrology-quality-measurement.jpg"\n                alt="Quality Inspection and Dimensional Metrology Lab at Ascent Engineering"'
    )
    html = html.replace(
        'data-lightbox-src="img/generated/metrology-inspection-lab.jpg" data-lightbox-title="Ascent Engineering Metrology Inspection Laboratory"',
        'data-lightbox-src="img/generated/metrology-quality-measurement.jpg" data-lightbox-title="Ascent Engineering Precision Metrology & 2D Height Gauge Inspection"'
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated successfully with distinct, non-duplicate images!")


def update_services():
    with open('services.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. CNC Milling: cnc-operation-spindle.jpg
    html = html.replace(
        'src="img/generated/cnc-cutting-coolant.jpg"\n                  alt="High-Precision CNC Milling Operations with Flood Coolant"',
        'src="img/generated/cnc-operation-spindle.jpg"\n                  alt="High-Speed CNC Spindle Milling Operation with Active Flood Coolant"'
    )
    html = html.replace(
        'data-lightbox-src="img/generated/cnc-cutting-coolant.jpg" data-lightbox-title="High-Precision CNC Milling Operations"',
        'data-lightbox-src="img/generated/cnc-operation-spindle.jpg" data-lightbox-title="High-Speed CNC Spindle Milling with Flood Coolant Spray"'
    )

    # 2. Precision Component Manufacturing: precision-components-inspection.jpg
    html = html.replace(
        'src="img/generated/precision-components-hero.jpg"\n                  alt="Precision Machined Engineered Components"',
        'src="img/generated/precision-components-inspection.jpg"\n                  alt="Precision Aerospace Milled Components on Granite Metrology Bench"'
    )
    html = html.replace(
        'data-lightbox-src="img/generated/precision-components-hero.jpg" data-lightbox-title="Precision Component Manufacturing"',
        'data-lightbox-src="img/generated/precision-components-inspection.jpg" data-lightbox-title="Precision Aerospace Components on Inspection Surface"'
    )

    # 3. Aerospace Component Machining: aerospace-component-machining.jpg
    html = html.replace(
        'src="img/generated/component-aerospace-avionics-chassis.jpg"\n                  alt="Aerospace Avionics Chassis and Structural Enclosure"',
        'src="img/generated/aerospace-component-machining.jpg"\n                  alt="Continuous Multi-Axis Aerospace Component Machining Setup"'
    )
    html = html.replace(
        'data-lightbox-src="img/generated/component-aerospace-avionics-chassis.jpg" data-lightbox-title="Aerospace Component Machining"',
        'data-lightbox-src="img/generated/aerospace-component-machining.jpg" data-lightbox-title="Continuous Multi-Axis Aerospace Impeller & Component Machining"'
    )

    # 4. VMC Machining: vmc-machining-environment.jpg
    # (Previously it used shop-floor-featured.jpg, duplicating the showcase banner!)
    html = html.replace(
        'src="img/ascent/shop-floor-featured.jpg"\n                  alt="Ascent Engineering Shop Floor - 3-Axis VMC Fleet Line"',
        'src="img/generated/vmc-machining-environment.jpg"\n                  alt="Ascent Engineering 3-Axis VMC Machining Workstation"'
    )
    html = html.replace(
        'data-lightbox-src="img/ascent/shop-floor-featured.jpg" data-lightbox-title="Ascent Engineering Actual Shop Floor VMC Machine Fleet"',
        'data-lightbox-src="img/generated/vmc-machining-environment.jpg" data-lightbox-title="Ascent Engineering 3-Axis VMC Production Workstation"'
    )

    # 5. Shop Floor Showcase Banner: use authentic shop-floor-aisle.jpg
    html = html.replace(
        'src="img/ascent/shop-floor-featured.jpg"\n                alt="Ascent Engineering Actual Shop Floor - Peenya 3rd Stage, Bengaluru"',
        'src="img/ascent/shop-floor-aisle.jpg"\n                alt="Ascent Engineering Actual Shop Floor Machine Aisle - Peenya 3rd Stage, Bengaluru"'
    )
    html = html.replace(
        'data-lightbox-src="img/ascent/shop-floor-featured.jpg" data-lightbox-title="Ascent Engineering Actual Shop Floor - Peenya 3rd Stage, Bengaluru"',
        'data-lightbox-src="img/ascent/shop-floor-aisle.jpg" data-lightbox-title="Ascent Engineering Actual Shop Floor Aisle & VMC Bays - Peenya 3rd Stage, Bengaluru"'
    )

    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("services.html updated successfully with distinct, non-duplicate images!")


def update_ourmachine():
    with open('ourmachine.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Cap 3 (CNC Tapping Operations): use equipment-tooling-closeup.jpg
    # (previously precision-components-hero.jpg, which was duplicated!)
    html = html.replace(
        'src="img/generated/precision-components-hero.jpg"\n                  alt="CNC Tapping and Threading Operations"',
        'src="img/generated/equipment-tooling-closeup.jpg"\n                  alt="Precision CNC Rigid Tapping & Tooling Equipment Close-up"'
    )

    # 2. Metrology Lab Image: use metrology-quality-measurement.jpg
    html = html.replace(
        'src="img/generated/metrology-inspection-lab.jpg"',
        'src="img/generated/metrology-quality-measurement.jpg"'
    )
    html = html.replace(
        'data-lightbox-src="img/generated/metrology-inspection-lab.jpg"',
        'data-lightbox-src="img/generated/metrology-quality-measurement.jpg"'
    )

    with open('ourmachine.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("ourmachine.html updated successfully with distinct, non-duplicate images!")


update_index()
update_services()
update_ourmachine()
