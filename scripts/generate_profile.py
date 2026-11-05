# -*- coding: utf-8 -*-
"""
Generator script for ASCENT ENGINEERING Corporate Company Profile
Creates company-profile/index.html containing all 15 required sections:
1. Cover page with company name, tagline, and strong manufacturing visual
2. Company profile / About Ascent Engineering
3. General company information (Table & stat cards)
4. Vision and mission (+ Policies)
5. Company strengths and manufacturing capabilities (5 Pillars)
6. Engineering and manufacturing facilities (CAD/CAM, Jigs & Fixtures, DFM)
7. Machine shop facilities (Machine showcase)
8. Complete machinery list and machine specifications (Table)
9. Instruments and measuring equipment (Tables from Excel PDF)
10. Quality assurance and inspection (Metrology lab, Mahr 2D height gauge, Granite surface tables)
11. Manufacturing components gallery (60+ parts with filters)
12. Shop-floor and infrastructure gallery (12+ authentic shop floor images)
13. Industries served (8 sectors)
14. Future development / expansion plans (Strictly supported by sources)
15. Contact details and closing page (Addresses, phones, email, GSTN, feedback note, Thank You)
"""

import os

def generate_html():
    # 1. Header & Nav
    html = []
    html.append('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ASCENT ENGINEERING — Corporate Company Profile | Aerospace &amp; Defense Parts Manufacturer</title>
    <meta
      name="description"
      content="Official Corporate Company Profile of ASCENT ENGINEERING, Peenya, Bengaluru. Precision 5-axis and 3-axis CNC milling, aerospace and defense component manufacturing, precision drilling, and quality metrology."
    />
    <meta
      name="keywords"
      content="Ascent Engineering, Aerospace Parts Manufacturer, Defense Machining, 5-Axis VMC, Hurco VC 500i, Cosmos SM50, Twin Horn VMC, Yantrang 850, Peenya Bengaluru, Precision CNC Milling"
    />
    <meta name="author" content="Ascent Engineering" />

    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="../logo/favicon.svg" />
    <link rel="icon" type="image/png" href="../logo/ascent-engineering-logo-transparent.png" />

    <!-- Google Fonts: Poppins (300, 400, 500, 600, 700, 800) -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap"
      rel="stylesheet"
    />

    <!-- Font Awesome 6 Icons -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
    />

    <!-- Dedicated Company Profile Stylesheet (Isolated) -->
    <link rel="stylesheet" href="profile.css" />
  </head>
  <body class="profile-body">
    <!-- Top Corporate Navigation Header -->
    <header class="cp-header" id="cpHeader">
      <div class="container cp-header-inner">
        <a href="#hero" class="cp-logo" title="ASCENT ENGINEERING Profile">
          <img
            src="../logo/ascent-engineering-logo-transparent.png"
            alt="ASCENT ENGINEERING Logo"
            class="cp-logo-img"
          />
          <div class="cp-logo-text">
            <div class="cp-logo-title">ASCENT <span>ENGINEERING</span></div>
            <div class="cp-logo-subtitle">Innovative Solutions for Aerospace Manufacturing</div>
          </div>
        </a>

        <!-- Navigation Menu -->
        <nav class="cp-nav-menu" id="cpNavMenu" aria-label="Profile Navigation">
          <a href="#about" class="cp-nav-link">Overview</a>
          <a href="#general-info" class="cp-nav-link">General Info</a>
          <a href="#vision-mission" class="cp-nav-link">Vision &amp; Mission</a>
          <a href="#strengths" class="cp-nav-link">Strengths</a>
          <a href="#facilities" class="cp-nav-link">Facilities</a>
          <a href="#machinery" class="cp-nav-link">Machinery</a>
          <a href="#instruments" class="cp-nav-link">Instruments</a>
          <a href="#quality" class="cp-nav-link">Quality</a>
          <a href="#components" class="cp-nav-link">Components</a>
          <a href="#shopfloor" class="cp-nav-link">Shop Floor</a>
          <a href="#industries" class="cp-nav-link">Industries</a>
          <a href="#contact" class="cp-nav-link">Contact</a>
        </nav>

        <div class="cp-header-cta">
          <a href="#contact" class="cp-btn cp-btn-gold">
            <span>Corporate RFQ</span>
            <i class="fa-solid fa-arrow-right"></i>
          </a>
          <button class="cp-mobile-toggle" id="cpMobileToggle" aria-label="Toggle navigation">
            <i class="fa-solid fa-bars"></i>
          </button>
        </div>
      </div>
    </header>

    <main>
''')

    # SECTION 1: COVER PAGE / HERO
    html.append('''
      <!-- Section 1: Cover Page / Hero (Midnight Charcoal) -->
      <section class="cp-hero" id="hero">
        <div class="cp-hero-bg">
          <img
            src="images/shopfloor/facility-panoramic-hero.jpg"
            alt="Ascent Engineering Precision CNC Manufacturing Shop Floor"
          />
        </div>
        <div class="cp-hero-overlay"></div>

        <div class="container">
          <div class="cp-hero-content">
            <div class="cp-hero-badge">
              <i class="fa-solid fa-certificate"></i>
              <span>Corporate Company Profile • Peenya 3rd Stage, Bengaluru</span>
            </div>

            <h1 class="cp-hero-title">
              ASCENT ENGINEERING<br />
              <span class="gold-accent">INNOVATIVE SOLUTIONS FOR AEROSPACE MANUFACTURING</span>
            </h1>

            <p class="cp-hero-desc">
              Ascent Engineering is a specialized precision manufacturing enterprise delivering tight-tolerance CNC milling, simultaneous 5-axis machining, and high-integrity component manufacturing for aerospace, defense, automobile, automation, hydraulic, and precision engineering sectors.
            </p>

            <div class="cp-hero-actions">
              <a href="#contact" class="cp-btn cp-btn-gold">
                <span>Submit Business RFQ</span>
                <i class="fa-solid fa-file-contract"></i>
              </a>
              <a href="#machinery" class="cp-btn cp-btn-outline-silver">
                <span>Verified Machine Fleet</span>
                <i class="fa-solid fa-gears"></i>
              </a>
              <a href="#shopfloor" class="cp-btn cp-btn-outline-gold">
                <span>Shop Floor Gallery</span>
                <i class="fa-solid fa-images"></i>
              </a>
            </div>

            <!-- Fast Verified Metric Highlights -->
            <div class="cp-hero-stats">
              <div class="cp-stat-box">
                <div class="cp-stat-num">3,600 Sq. M</div>
                <div class="cp-stat-label">Total Plant Floor Area</div>
              </div>

              <div class="cp-stat-box">
                <div class="cp-stat-num">22 Personnel</div>
                <div class="cp-stat-label">Skilled Workforce &amp; Technocrats</div>
              </div>

              <div class="cp-stat-box">
                <div class="cp-stat-num">5-Axis Hurco</div>
                <div class="cp-stat-label">Simultaneous Multi-Axis VMC</div>
              </div>

              <div class="cp-stat-box">
                <div class="cp-stat-num">&gt;99% Score</div>
                <div class="cp-stat-label">Quality Score &amp; &lt;100 PPM Target</div>
              </div>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 2: COMPANY PROFILE / ABOUT ASCENT ENGINEERING
    html.append('''
      <!-- Section 2: Company Profile / About Ascent Engineering (Warm Ivory) -->
      <section class="section-ivory" id="about">
        <div class="container">
          <div class="cp-about-grid">
            <div class="cp-about-text">
              <div class="section-tag-gold">
                <i class="fa-solid fa-building-shield"></i> Company Overview
              </div>
              <h2>Engineered for Manufacturing Precision &amp; Reliability</h2>
              <p>
                <strong>ASCENT ENGINEERING</strong> was established to serve the demanding requirements of <strong>Automobile, Automation, Aerospace, Hydraulic, Electronics, and Defense industries</strong>. Operating from the prime manufacturing cluster of Peenya 3rd Stage, Bangalore, our modern facility spans 3,600 square meters of production space.
              </p>
              <p>
                We possess trained manpower dedicated to overseeing purchase, production, development, and quality engineering. In addition to our internal machining infrastructure, we seamlessly mobilize specialized outside finishing, heat treatment, and precision surface processing services to deliver turnkey components to our customers.
              </p>
              <p>
                Ascent Engineering is a quality-oriented company led by a team of qualified technocrats supported by a highly skilled workforce of 22 professionals, aiming at uncompromising customer satisfaction through strict adherence to quality policies and continuous improvement.
              </p>

              <div class="cp-pillars-list">
                <div class="cp-pillar-item">
                  <h4><i class="fa-solid fa-arrows-spin text-gold"></i> Multi-Axis Agility</h4>
                  <p>Continuous 5-axis contouring reduces setups and preserves strict datum concentricity.</p>
                </div>

                <div class="cp-pillar-item">
                  <h4><i class="fa-solid fa-layer-group text-gold"></i> Batch Capacity</h4>
                  <p>Parallel 3-axis and 4-axis VMC lines dedicated to medium-to-large production runs with swift cycle times.</p>
                </div>

                <div class="cp-pillar-item">
                  <h4><i class="fa-solid fa-ruler-combined text-gold"></i> Granite Metrology</h4>
                  <p>In-house Mahr 2D height gauge and granite surface tables for verified dimensional reports.</p>
                </div>

                <div class="cp-pillar-item">
                  <h4><i class="fa-solid fa-shield-halved text-gold"></i> Drawing Security</h4>
                  <p>Strict non-disclosure compliance and confidential handling of defense and proprietary client IP.</p>
                </div>
              </div>

              <div style="margin-top: 24px;">
                <a href="#general-info" class="cp-btn cp-btn-dark">
                  <span>View Corporate Information</span>
                  <i class="fa-solid fa-arrow-down"></i>
                </a>
              </div>
            </div>

            <!-- Authentic Shop Floor Photo Card -->
            <div class="cp-about-visual">
              <div class="cp-about-image-card" data-cp-lightbox="images/shopfloor/facility-vmc-floor-1.jpg" data-cp-caption="Ascent Engineering Shop Floor — Production Machine Bays in Peenya 3rd Stage, Bengaluru">
                <img
                  src="images/shopfloor/facility-vmc-floor-1.jpg"
                  alt="Ascent Engineering Actual Shop Floor VMC Machine Fleet"
                />
                <div class="cp-about-badge">
                  <div class="cp-about-badge-text">
                    <h5>Actual Manufacturing Shop Floor</h5>
                    <p>Ground Floor, B 40 &amp; #240/P6 Industrial Area, Peenya 3rd Stage, Bengaluru – 560058</p>
                  </div>
                  <div class="cp-about-badge-icon">
                    <i class="fa-solid fa-industry"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 3: GENERAL COMPANY INFORMATION
    html.append('''
      <!-- Section 3: General Company Information (Warm Ivory) -->
      <section class="section-ivory" id="general-info" style="border-top: 1px solid var(--cp-border-light);">
        <div class="container">
          <div class="profile-section-header">
            <div class="section-tag-gold">
              <i class="fa-solid fa-id-card"></i> Corporate Credentials
            </div>
            <h2 class="profile-section-title">General Company Information</h2>
            <p class="profile-section-desc">
              Official registered business details, facility specifications, and corporate tax identifiers for ASCENT ENGINEERING.
            </p>
          </div>

          <div class="cp-general-info-grid">
            <!-- Left: Table Format matching SKDM Slide 1 Structure -->
            <div class="cp-table-container light-theme" style="margin: 0;">
              <div class="cp-table-header-bar">
                <h4><i class="fa-solid fa-building text-gold"></i> Registered Enterprise Profile</h4>
                <span class="cp-table-sub">Bengaluru Industrial Directorate</span>
              </div>
              <div class="cp-table-responsive">
                <table class="cp-info-kv-table">
                  <tbody>
                    <tr>
                      <th>COMPANY NAME</th>
                      <td><strong>ASCENT ENGINEERING</strong></td>
                    </tr>
                    <tr>
                      <th>TAGLINE</th>
                      <td><em>Innovative Solutions for Aerospace Manufacturing</em></td>
                    </tr>
                    <tr>
                      <th>COMPANY ADDRESS</th>
                      <td>
                        <strong>Ground Floor, B 40 &amp; #240/P6 Industrial Area</strong>,<br />
                        1st Main Road, Peenya 3rd Stage, Bangalore – 560058, Karnataka, India
                      </td>
                    </tr>
                    <tr>
                      <th>NATURE OF BUSINESS</th>
                      <td>Manufacturer of precision CNC Milling components, aerospace parts, and mechanical assemblies</td>
                    </tr>
                    <tr>
                      <th>KIND OF OWNERSHIP</th>
                      <td>Single Owner (Proprietorship)</td>
                    </tr>
                    <tr>
                      <th>CONTACT NUMBERS</th>
                      <td>
                        <a href="tel:7353150847"><strong>+91 73531 50847</strong></a> / 
                        <a href="tel:7353140847"><strong>+91 73531 40847</strong></a> (Technical Lead: M V Kumara Swamy)
                      </td>
                    </tr>
                    <tr>
                      <th>OFFICIAL EMAIL</th>
                      <td><a href="mailto:ascenteng03@gmail.com"><strong>ascenteng03@gmail.com</strong></a></td>
                    </tr>
                    <tr>
                      <th>NUMBER OF EMPLOYEES</th>
                      <td><strong>22</strong> (Trained Technocrats, CNC Programmers, Machinists &amp; Quality Inspectors)</td>
                    </tr>
                    <tr>
                      <th>TOTAL PLANT AREA</th>
                      <td><strong>3,600 Sq. Meters</strong></td>
                    </tr>
                    <tr>
                      <th>GSTN IDENTIFIERS</th>
                      <td>
                        <span class="cp-badge-new">29DCAPR1495B1ZK</span> &nbsp;
                        <span class="cp-badge-new">29GAUPB9697A1ZZ</span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Right: Corporate Metrics & Plant Capacity -->
            <div>
              <div class="cp-info-stat-boxes">
                <div class="cp-info-stat-card">
                  <div class="cp-info-stat-icon"><i class="fa-solid fa-vector-square"></i></div>
                  <div class="stat-value">3,600 M²</div>
                  <div class="stat-lbl">Plant Floor Area</div>
                  <p style="font-size: 0.8rem; color: var(--cp-graphite); margin-top: 6px;">Spacious facility optimized for raw material storage, multi-axis machining, and metrology staging.</p>
                </div>

                <div class="cp-info-stat-card">
                  <div class="cp-info-stat-icon"><i class="fa-solid fa-users-gear"></i></div>
                  <div class="stat-value">22 Staff</div>
                  <div class="stat-lbl">Trained Manpower</div>
                  <p style="font-size: 0.8rem; color: var(--cp-graphite); margin-top: 6px;">Qualified technocrats dedicated to purchase, production, CAD/CAM development, and quality.</p>
                </div>

                <div class="cp-info-stat-card">
                  <div class="cp-info-stat-icon"><i class="fa-solid fa-gears"></i></div>
                  <div class="stat-value">07+ Units</div>
                  <div class="stat-lbl">CNC / VMC Fleet</div>
                  <p style="font-size: 0.8rem; color: var(--cp-graphite); margin-top: 6px;">Simultaneous 5-axis Hurco VC 500i, Yantrang 850, Yantrang 500 (4th axis), Twinhorn, and Cosmos.</p>
                </div>

                <div class="cp-info-stat-card">
                  <div class="cp-info-stat-icon"><i class="fa-solid fa-location-dot"></i></div>
                  <div class="stat-value">Peenya 3rd</div>
                  <div class="stat-lbl">Industrial Hub</div>
                  <p style="font-size: 0.8rem; color: var(--cp-graphite); margin-top: 6px;">Strategic location with fast logistics access to raw materials, tooling vendors, and surface processors.</p>
                </div>
              </div>

              <!-- Shop Floor Snippet -->
              <div style="margin-top: 20px; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--cp-border-light); cursor: pointer;"
                   data-cp-lightbox="images/shopfloor/WhatsApp_Image_2026-11-03_at_11.32.32_AM.jpeg"
                   data-cp-caption="Ascent Engineering Production Bay — Ground Floor, B 40, Peenya 3rd Stage, Bangalore">
                <img src="images/shopfloor/WhatsApp_Image_2026-11-03_at_11.32.32_AM.jpeg" alt="Ascent Engineering Actual Shopfloor Bay" style="width: 100%; height: 210px; object-fit: cover;" />
                <div style="padding: 10px 16px; background: #fff; font-size: 0.8rem; color: var(--cp-graphite);">
                  <i class="fa-solid fa-camera text-gold"></i> <strong>Actual Shop Floor:</strong> Peenya 3rd Stage Manufacturing Bay
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 4: VISION, MISSION & POLICIES
    html.append('''
      <!-- Section 4: Vision, Mission & Policies (Midnight Charcoal) -->
      <section class="section-charcoal" id="vision-mission">
        <div class="container">
          <div class="profile-section-header center">
            <div class="section-tag-gold">
              <i class="fa-solid fa-compass"></i> Guiding Principles
            </div>
            <h2 class="profile-section-title">Vision, Mission &amp; Operating Policies</h2>
            <p class="profile-section-desc">
              Ascent Engineering is guided by a relentless pursuit of world-class manufacturing excellence, zero defects, customer satisfaction, and safe, environmentally responsible production.
            </p>
          </div>

          <div class="cp-policy-grid">
            <!-- 1. Our Vision -->
            <div class="cp-policy-card accent-card">
              <div class="cp-policy-header">
                <div class="cp-policy-icon"><i class="fa-solid fa-eye"></i></div>
                <h3 class="cp-policy-title">Our Vision</h3>
              </div>
              <p class="cp-policy-text">
                "To be an established accredited world-class manufacturer of precision components. Our highly skilled and innovative team, committed to quality, will continuously deliver precision components, just in time, at a competitive price."
              </p>
              <div style="margin-top: 16px; font-size: 0.82rem; color: var(--cp-gold);">
                <i class="fa-solid fa-check"></i> Continuous improvement • World-class benchmarking • Vendor network integration
              </div>
            </div>

            <!-- 2. Our Mission -->
            <div class="cp-policy-card accent-card">
              <div class="cp-policy-header">
                <div class="cp-policy-icon"><i class="fa-solid fa-bullseye"></i></div>
                <h3 class="cp-policy-title">Our Mission</h3>
              </div>
              <p class="cp-policy-text">
                "Satisfy our customers with innovative technology and superior quality, value, and service. Develop our employees' skills, talents, and innovativeness while maintaining high-quality machinery and equipment in our plant."
              </p>
              <div style="margin-top: 16px; font-size: 0.82rem; color: var(--cp-gold);">
                <i class="fa-solid fa-check"></i> Advanced machine maintenance • Workforce upskilling • Superior customer value
              </div>
            </div>

            <!-- 3. Quality Policy -->
            <div class="cp-policy-card">
              <div class="cp-policy-header">
                <div class="cp-policy-icon"><i class="fa-solid fa-award"></i></div>
                <h3 class="cp-policy-title">Quality Policy</h3>
              </div>
              <p class="cp-policy-text">
                "Ascent Engineering is a quality-oriented company with a team of qualified technocrats supported by a skilled workforce aiming at customer satisfaction through strict adherence to quality policies. Ensuring customer satisfaction through providing excellence in Aerospace Components and continual improvements."
              </p>
              <div style="margin-top: 16px; font-size: 0.82rem; color: var(--cp-gold);">
                <i class="fa-solid fa-check"></i> Zero-defect target • In-process verification • Quality score &gt;99%
              </div>
            </div>

            <!-- 4. Environment & Safety Policy -->
            <div class="cp-policy-card">
              <div class="cp-policy-header">
                <div class="cp-policy-icon"><i class="fa-solid fa-leaf"></i></div>
                <h3 class="cp-policy-title">Environment &amp; Safety Policy</h3>
              </div>
              <p class="cp-policy-text">
                "We make every effort to continuously protect the environment by ensuring products and operations comply with all statutory regulations. It is our endeavor to provide employees a safe working environment using the best available practices, tools, and education, thereby achieving and maintaining a <strong>ZERO ACCIDENT facility</strong>."
              </p>
              <div style="margin-top: 16px; font-size: 0.82rem; color: var(--cp-gold);">
                <i class="fa-solid fa-check"></i> Zero accident facility • Green coolant management • Industrial safety protocols
              </div>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 5: COMPANY STRENGTHS AND MANUFACTURING CAPABILITIES (5 PILLARS)
    html.append('''
      <!-- Section 5: Company Strengths & Capabilities (Warm Ivory) -->
      <section class="section-ivory" id="strengths">
        <div class="container">
          <div class="profile-section-header center">
            <div class="section-tag-gold">
              <i class="fa-solid fa-shield-halved"></i> 5 Strategic Pillars
            </div>
            <h2 class="profile-section-title">Our Pillars of Strength</h2>
            <p class="profile-section-desc">
              Structured operational methodology derived from Ascent Engineering's quality framework ensuring dependable aerospace and precision manufacturing execution.
            </p>
          </div>

          <div class="cp-strengths-grid">
            <!-- Pillar 1: Quality Management -->
            <div class="cp-strength-card">
              <span class="cp-strength-pill">Pillar 01</span>
              <h3 class="cp-strength-title">Quality Management</h3>
              <ul class="cp-strength-list">
                <li><i class="fa-solid fa-circle-check"></i> Trusted in quality &amp; precision manufacturing</li>
                <li><i class="fa-solid fa-circle-check"></i> Drive the organization for Zero-Defects</li>
                <li><i class="fa-solid fa-circle-check"></i> Effective Quality Plan for products</li>
                <li><i class="fa-solid fa-circle-check"></i> Ensure product compliance to drawing</li>
                <li><i class="fa-solid fa-circle-check"></i> Meet &amp; measure customer satisfaction</li>
                <li><i class="fa-solid fa-circle-check"></i> Maintain Quality Score always &gt;99%</li>
              </ul>
            </div>

            <!-- Pillar 2: Engineering -->
            <div class="cp-strength-card">
              <span class="cp-strength-pill">Pillar 02</span>
              <h3 class="cp-strength-title">Engineering</h3>
              <ul class="cp-strength-list">
                <li><i class="fa-solid fa-circle-check"></i> Conceptual Design for Manufacturability (DFM)</li>
                <li><i class="fa-solid fa-circle-check"></i> 3D Process Design &amp; Drafting</li>
                <li><i class="fa-solid fa-circle-check"></i> Jigs &amp; Fixture Custom Design</li>
                <li><i class="fa-solid fa-circle-check"></i> CAM Programming &amp; Advanced Simulation</li>
                <li><i class="fa-solid fa-circle-check"></i> Advanced Production Documentation</li>
                <li><i class="fa-solid fa-circle-check"></i> Manufacturing Data Management</li>
                <li><i class="fa-solid fa-circle-check"></i> Advanced Tooling Design</li>
              </ul>
            </div>

            <!-- Pillar 3: Manufacturing -->
            <div class="cp-strength-card">
              <span class="cp-strength-pill">Pillar 03</span>
              <h3 class="cp-strength-title">Manufacturing</h3>
              <ul class="cp-strength-list">
                <li><i class="fa-solid fa-circle-check"></i> Ethical Manufacturing Practice</li>
                <li><i class="fa-solid fa-circle-check"></i> Achieve &lt;100 PPM &amp; 99% OTD</li>
                <li><i class="fa-solid fa-circle-check"></i> Implement Effective Continuous Improvement</li>
                <li><i class="fa-solid fa-circle-check"></i> Comply to System &amp; Customer Requirements</li>
                <li><i class="fa-solid fa-circle-check"></i> Follow Lean Manufacturing Principles</li>
                <li><i class="fa-solid fa-circle-check"></i> Support customer to enhance cost reduction</li>
              </ul>
            </div>

            <!-- Pillar 4: Mfg. Network Console -->
            <div class="cp-strength-card">
              <span class="cp-strength-pill">Pillar 04</span>
              <h3 class="cp-strength-title">Mfg. Network Console</h3>
              <ul class="cp-strength-list">
                <li><i class="fa-solid fa-circle-check"></i> Effective Supply Chain Management (SCM)</li>
                <li><i class="fa-solid fa-circle-check"></i> Advanced Manufacturing Engineering Support</li>
                <li><i class="fa-solid fa-circle-check"></i> Achieve &lt;100 PPM quality standard</li>
                <li><i class="fa-solid fa-circle-check"></i> Achieve 99% On-Time Delivery</li>
                <li><i class="fa-solid fa-circle-check"></i> Focus Continuous Improvement on Resources</li>
                <li><i class="fa-solid fa-circle-check"></i> Cost Reduction pass-through to customer</li>
                <li><i class="fa-solid fa-circle-check"></i> Centralized Engineering Support</li>
              </ul>
            </div>

            <!-- Pillar 5: Core Operational Highlights -->
            <div class="cp-strength-card">
              <span class="cp-strength-pill">Pillar 05</span>
              <h3 class="cp-strength-title">Operational Highlights</h3>
              <ul class="cp-strength-list">
                <li><i class="fa-solid fa-circle-check"></i> Innovative Engineering Techniques</li>
                <li><i class="fa-solid fa-circle-check"></i> Strategic Manufacturing Methodologies</li>
                <li><i class="fa-solid fa-circle-check"></i> Smart Production Management</li>
                <li><i class="fa-solid fa-circle-check"></i> Deep Manufacturing Knowledge</li>
                <li><i class="fa-solid fa-circle-check"></i> Advanced Quality Management</li>
                <li><i class="fa-solid fa-circle-check"></i> Contributing Success to Customer thru effective continuous improvement</li>
              </ul>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 6: ENGINEERING AND MANUFACTURING FACILITIES
    html.append('''
      <!-- Section 6: Engineering and Manufacturing Facilities (Midnight Charcoal) -->
      <section class="section-charcoal" id="facilities">
        <div class="container">
          <div class="profile-section-header center">
            <div class="section-tag-gold">
              <i class="fa-solid fa-industry"></i> Plant Infrastructure
            </div>
            <h2 class="profile-section-title">Engineering &amp; Manufacturing Facilities</h2>
            <p class="profile-section-desc">
              Ascent Engineering's 3,600 sq. meter Peenya facility combines digital CAD/CAM development, specialized workholding fabrication, and dedicated alloy staging for streamlined production.
            </p>
          </div>

          <div class="cp-facilities-grid">
            <!-- Facility 1: CAD/CAM & 3D Simulation -->
            <div class="cp-facility-box">
              <div class="cp-facility-img" data-cp-lightbox="images/shopfloor/WhatsApp_Image_2026-11-03_at_11.32.33_AM_1.jpeg" data-cp-caption="Ascent Engineering CNC Programming & Machine Setup Facility">
                <img src="images/shopfloor/WhatsApp_Image_2026-11-03_at_11.32.33_AM_1.jpeg" alt="CAD/CAM & CNC Setup Facility" />
              </div>
              <div class="cp-facility-body">
                <h4><i class="fa-solid fa-desktop text-gold"></i> CAD/CAM &amp; 3D Simulation</h4>
                <p>
                  High-speed 3D CAD/CAM workstations generating gouge-free cutter paths, toolpath simulation, and DFM design analysis for complex aerospace geometries before metal is cut.
                </p>
              </div>
            </div>

            <!-- Facility 2: Jigs, Fixtures & Custom Tooling -->
            <div class="cp-facility-box">
              <div class="cp-facility-img" data-cp-lightbox="images/shopfloor/WhatsApp_Image_2026-11-03_at_11.32.34_AM.jpeg" data-cp-caption="Ascent Engineering In-House Jigs, Fixturing & Inspection Setup">
                <img src="images/shopfloor/WhatsApp_Image_2026-11-03_at_11.32.34_AM.jpeg" alt="Jigs, Fixtures & Inspection Station" />
              </div>
              <div class="cp-facility-body">
                <h4><i class="fa-solid fa-screwdriver-wrench text-gold"></i> Jigs, Fixtures &amp; Workholding</h4>
                <p>
                  In-house design and fabrication of modular fixturing, multi-station vice arrays, and soft jaws ensuring minimum clamping distortion and repeatable part positioning.
                </p>
              </div>
            </div>

            <!-- Facility 3: Raw Material & Staging Bays -->
            <div class="cp-facility-box">
              <div class="cp-facility-img" data-cp-lightbox="images/shopfloor/facility-panoramic-hero.jpg" data-cp-caption="Ascent Engineering Production Aisle & Material Staging Bays">
                <img src="images/shopfloor/facility-panoramic-hero.jpg" alt="Production Aisle & Material Staging" />
              </div>
              <div class="cp-facility-body">
                <h4><i class="fa-solid fa-cubes-stacked text-gold"></i> Material Staging &amp; Prep</h4>
                <p>
                  Dedicated raw stock warehouse handling aerospace aluminium (6061-T6, 7075-T651), stainless steels (304, 316), alloy steels (EN19, EN24), and high-temp alloys with full heat-lot traceability.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 7: MACHINE SHOP FACILITIES (SHOWCASE)
    html.append('''
      <!-- Section 7: Machine Shop Facilities (Warm Ivory) -->
      <section class="section-ivory" id="machinery-showcase">
        <div class="container">
          <div class="profile-section-header center">
            <div class="section-tag-gold">
              <i class="fa-solid fa-server"></i> Machine Shop Facilities
            </div>
            <h2 class="profile-section-title">Verified Machine Shop Infrastructure</h2>
            <p class="profile-section-desc">
              Ascent Engineering operates high-precision 5-axis and 3-axis CNC vertical machining centers equipped with Mitsubishi m80 AV and advanced industrial controls.
            </p>
          </div>

          <div class="cp-machines-grid">
            <!-- 1. Flagship Hurco 5 Axis VC 500i -->
            <div class="cp-machine-card flagship">
              <div class="cp-machine-img-box" data-cp-lightbox="images/machines/machine-hurco-5axis.jpg" data-cp-caption="Hurco 5 Axis VC 500i Vertical Machining Center — Qty: 01 Unit">
                <img src="images/machines/machine-hurco-5axis.jpg" alt="Hurco 5 Axis VC 500i VMC" loading="lazy" />
                <span class="cp-machine-tag"><i class="fa-solid fa-star text-gold"></i> 5-Axis Flagship (01 Unit)</span>
              </div>
              <div class="cp-machine-body">
                <h3 class="cp-machine-name">Hurco 5 Axis VC 500i</h3>
                <p class="cp-machine-desc">
                  Premier 5-axis simultaneous machining center with trunnion rotary table. Designed for complex aerofoils, impellers, curved housings, and angled aerospace bracketry in a single clamping to eliminate datum transfer errors.
                </p>
                <div class="cp-machine-spec-pills">
                  <span class="cp-spec-pill"><i class="fa-solid fa-arrows-spin"></i> Simultaneous 5-Axis</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-gauge-high"></i> 12,000 RPM Spindle</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-microchip"></i> WinMax CNC Control</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-plane"></i> Aerospace Geometry</span>
                </div>
              </div>
            </div>

            <!-- 2. Yantrang (VX850) -->
            <div class="cp-machine-card">
              <div class="cp-machine-img-box" data-cp-lightbox="images/machines/machine-yantrang-850.jpg" data-cp-caption="Yantrang VX850 CNC Vertical Machining Center — Control: Mitsubishi m80 AV, 10000 RPM (01 No)">
                <img src="images/machines/machine-yantrang-850.jpg" alt="Yantrang VX850 CNC Vertical Machining Center" loading="lazy" />
                <span class="cp-machine-tag">850mm Envelope (01 Unit)</span>
              </div>
              <div class="cp-machine-body">
                <h3 class="cp-machine-name">Yantrang VX850</h3>
                <p class="cp-machine-desc">
                  High-speed 3-axis precision vertical machining center featuring a generous 850 mm travel envelope and rigid box-ways for medium-to-large structural plates, brackets, and multi-cavity fixtures.
                </p>
                <div class="cp-machine-spec-pills">
                  <span class="cp-spec-pill"><i class="fa-solid fa-microchip"></i> Mitsubishi m80 AV</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-gauge-high"></i> 10,000 RPM Spindle</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-cube"></i> Heavy-Duty Rigid Table</span>
                </div>
              </div>
            </div>

            <!-- 3. Yantrang (VX500) With 4th Axis -->
            <div class="cp-machine-card">
              <div class="cp-machine-img-box" data-cp-lightbox="images/machines/machine-twinhorn-vmc.jpg" data-cp-caption="Yantrang VX500 with 4th Axis Rotary Table — Control: Mitsubishi m80 AV, 10000 RPM (02 Nos)">
                <img src="images/machines/machine-twinhorn-vmc.jpg" alt="Yantrang VX500 with 4th Axis CNC Machining Center" loading="lazy" />
                <span class="cp-machine-tag">4th Axis Equipped (02 Units)</span>
              </div>
              <div class="cp-machine-body">
                <h3 class="cp-machine-name">Yantrang VX500 (With 4th Axis)</h3>
                <p class="cp-machine-desc">
                  Two dedicated high-precision vertical machining centers fitted with programmable 4th axis rotary tables for synchronized index milling, radial hole matrices, and multifaceted turning-milling profiles.
                </p>
                <div class="cp-machine-spec-pills">
                  <span class="cp-spec-pill"><i class="fa-solid fa-arrows-rotate"></i> 4th Axis Rotary Table</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-microchip"></i> Mitsubishi m80 AV</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-gauge-high"></i> 10,000 RPM Spindle</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-copy"></i> 02 Production Units</span>
                </div>
              </div>
            </div>

            <!-- 4. Twinhorn Taiwan Make VMC -->
            <div class="cp-machine-card">
              <div class="cp-machine-img-box" data-cp-lightbox="images/machines/vmc_machining_center_01.jpeg" data-cp-caption="Twinhorn Taiwan Make VMC 3 and 4th Axis — Qty: 02 Nos">
                <img src="images/machines/vmc_machining_center_01.jpeg" alt="Twinhorn Taiwan Make VMC" loading="lazy" />
                <span class="cp-machine-tag">Taiwan Make (02 Units)</span>
              </div>
              <div class="cp-machine-body">
                <h3 class="cp-machine-name">Twinhorn VMC (3 &amp; 4th Axis)</h3>
                <p class="cp-machine-desc">
                  Heavy-duty Taiwan-manufactured VMC machines engineered for maximum dynamic stability and vibration damping during high-removal roughing, precision deep-pocketing, and tough alloy machining.
                </p>
                <div class="cp-machine-spec-pills">
                  <span class="cp-spec-pill"><i class="fa-solid fa-cube"></i> Cast Iron Damping</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-arrows-spin"></i> 3 &amp; 4th Axis Capability</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-industry"></i> Taiwan Precision Build</span>
                </div>
              </div>
            </div>

            <!-- 5. Cosmos SM50 / Emtharangi Fleet -->
            <div class="cp-machine-card">
              <div class="cp-machine-img-box" data-cp-lightbox="images/machines/machine-cosmos-sm50.jpg" data-cp-caption="Cosmos SM50 Precision CNC Machining Center">
                <img src="images/machines/machine-cosmos-sm50.jpg" alt="Cosmos SM50 CNC Machining Center" loading="lazy" />
                <span class="cp-machine-tag">Precision Fleet</span>
              </div>
              <div class="cp-machine-body">
                <h3 class="cp-machine-name">Cosmos SM50 &amp; VMC Fleet</h3>
                <p class="cp-machine-desc">
                  Precision vertical machining platforms dedicated to batch component manufacturing, rapid setup turnovers, drilling arrays, and continuous high-tolerance surface finishing.
                </p>
                <div class="cp-machine-spec-pills">
                  <span class="cp-spec-pill"><i class="fa-solid fa-layer-group"></i> Repeatable Batch Runs</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-bullseye"></i> High Thermal Stability</span>
                  <span class="cp-spec-pill"><i class="fa-solid fa-gears"></i> Continuous Duty</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 8: COMPLETE MACHINERY LIST AND MACHINE SPECIFICATIONS (TABLE)
    html.append('''
      <!-- Section 8: Complete Machinery List Table (Midnight Charcoal) -->
      <section class="section-charcoal" id="machinery">
        <div class="container">
          <div class="profile-section-header">
            <div class="section-tag-gold">
              <i class="fa-solid fa-list-check"></i> Plant Inventory
            </div>
            <h2 class="profile-section-title">Complete Machinery List &amp; Specifications</h2>
            <p class="profile-section-desc">
              Full inventory of CNC and vertical machining centers at Ascent Engineering, compiled in accordance with industrial audit standards.
            </p>
          </div>

          <div class="cp-table-container">
            <div class="cp-table-header-bar">
              <h4><i class="fa-solid fa-microchip text-gold"></i> Machine Tool Fleet Inventory</h4>
              <span class="cp-table-sub">Ascent Engineering Machine Shop • Peenya 3rd Stage</span>
            </div>
            <div class="cp-table-responsive">
              <table class="cp-table">
                <thead>
                  <tr>
                    <th>SL. NO</th>
                    <th>MACHINE NAME</th>
                    <th>MAKER / ORIGIN</th>
                    <th>AXIS CONFIGURATION</th>
                    <th>WORKING ENVELOPE / RANGE</th>
                    <th>CNC CONTROL</th>
                    <th>MAX SPINDLE SPEED</th>
                    <th>QTY</th>
                    <th>STATUS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>01</strong></td>
                    <td><strong>Hurco VC 500i</strong></td>
                    <td>Hurco (USA / Global)</td>
                    <td><span class="cp-badge-new">5-Axis Simultaneous</span></td>
                    <td>500 mm Trunnion Table Envelope</td>
                    <td>Hurco WinMax Multi-Axis</td>
                    <td><strong>12,000 RPM</strong></td>
                    <td><strong>01 No</strong></td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Active</span></td>
                  </tr>
                  <tr>
                    <td><strong>02</strong></td>
                    <td><strong>Yantrang (VX850)</strong></td>
                    <td>Yantrang CNC</td>
                    <td>3-Axis Precision VMC</td>
                    <td>850 x 510 x 510 mm</td>
                    <td>Mitsubishi m80 AV</td>
                    <td><strong>10,000 RPM</strong></td>
                    <td><strong>01 No</strong></td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Active</span></td>
                  </tr>
                  <tr>
                    <td><strong>03</strong></td>
                    <td><strong>Yantrang (VX500) With 4th Axis</strong></td>
                    <td>Yantrang CNC</td>
                    <td><span class="cp-badge-new">4-Axis (4th Axis Rotary Table)</span></td>
                    <td>500 x 400 x 450 mm</td>
                    <td>Mitsubishi m80 AV</td>
                    <td><strong>10,000 RPM</strong></td>
                    <td><strong>02 Nos</strong></td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Active</span></td>
                  </tr>
                  <tr>
                    <td><strong>04</strong></td>
                    <td><strong>Twinhorn VMC</strong></td>
                    <td>Twinhorn (Taiwan Make)</td>
                    <td>3 and 4th Axis</td>
                    <td>Standard Heavy VMC Bed</td>
                    <td>Taiwan Industrial CNC</td>
                    <td>High-Torque Milling Spindle</td>
                    <td><strong>02 Nos</strong></td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Active</span></td>
                  </tr>
                  <tr>
                    <td><strong>05</strong></td>
                    <td><strong>Cosmos SM50 / Emtharangi</strong></td>
                    <td>Cosmos / Industrial Platform</td>
                    <td>3-Axis High Rigidity VMC</td>
                    <td>500 x 400 x 400 mm</td>
                    <td>Industrial CNC Control</td>
                    <td>8,000 – 10,000 RPM</td>
                    <td><strong>Active Fleet</strong></td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Active</span></td>
                  </tr>
                  <tr>
                    <td><strong>06</strong></td>
                    <td><strong>Industrial Air Compressor</strong></td>
                    <td>G-Mate / Industrial Auxiliary</td>
                    <td>Central Pneumatic Supply</td>
                    <td>10 HP System</td>
                    <td>Automatic Pressure Regulated</td>
                    <td>Continuous Duty Cycle</td>
                    <td><strong>01 No</strong></td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Plant Utility</span></td>
                  </tr>
                  <tr>
                    <td><strong>07</strong></td>
                    <td><strong>Synchronized Rigid Tapping Unit</strong></td>
                    <td>Precision Tapping Station</td>
                    <td>Multi-Spindle Rigid Tapping</td>
                    <td>M2 to M20 Threading Range</td>
                    <td>CNC Synchronized Thread Lead</td>
                    <td>Variable Cycle Control</td>
                    <td><strong>Active Unit</strong></td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Active</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 9: INSTRUMENTS AND MEASURING EQUIPMENT (WARM IVORY TABLES)
    html.append('''
      <!-- Section 9: Instruments & Measuring Equipment (Warm Ivory) -->
      <section class="section-ivory" id="instruments">
        <div class="container">
          <div class="profile-section-header">
            <div class="section-tag-gold">
              <i class="fa-solid fa-ruler-combined"></i> Metrology &amp; Inspection
            </div>
            <h2 class="profile-section-title">Instruments &amp; Measuring Equipment</h2>
            <p class="profile-section-desc">
              Updated instrument inventory and calibration records from latest calibration audits (Source: New Microsoft Excel Worksheet / IRCLASS &amp; Mailaralingeshwra Laboratories).
            </p>
          </div>

          <!-- Metrology Lab Accreditation Card -->
          <div style="background: var(--cp-ivory-card); border: 1px solid var(--cp-border-light); border-left: 4px solid var(--cp-gold); padding: 18px 24px; border-radius: var(--radius-md); margin-bottom: 28px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px;">
            <div>
              <h5 style="margin: 0 0 4px; color: var(--cp-charcoal); font-size: 1rem;"><i class="fa-solid fa-certificate text-gold"></i> Traceable Calibration Laboratories</h5>
              <p style="margin: 0; font-size: 0.85rem; color: var(--cp-graphite);">
                1. <strong>GEOLOGICAL AND METALLURGICAL LABORATORIES</strong> (A Division of IRCLASS Systems and Solutions PVT LTD)<br />
                2. <strong>MAILARALINGESHWRA PRECISION INSTRUMENT</strong> (Nagaraj B, Rajagopal Nagar, Bengaluru • Reg: 9945791443)
              </p>
            </div>
            <div>
              <span class="cp-badge-cal"><i class="fa-solid fa-calendar-check"></i> Audit Cycle: 8/10/2026 – Due: 8/9/2027</span>
            </div>
          </div>

          <!-- Table 1: Digital Micrometers -->
          <div class="cp-table-container light-theme">
            <div class="cp-table-header-bar">
              <h4><i class="fa-solid fa-arrows-left-right-to-line text-gold"></i> Digital Micrometers</h4>
              <span class="cp-table-sub">Calibration Lab: IRCLASS / Geological &amp; Metallurgical Laboratories</span>
            </div>
            <div class="cp-table-responsive">
              <table class="cp-table">
                <thead>
                  <tr>
                    <th>INSTRUMENT ID</th>
                    <th>MEASURING RANGE (MM)</th>
                    <th>CALIBRATION DATE</th>
                    <th>DUE DATE</th>
                    <th>CALIBRATION STATUS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>DMM-01</strong></td>
                    <td>00 – 25</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                  <tr>
                    <td><strong>DMM-02</strong></td>
                    <td>25 – 50</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                  <tr>
                    <td><strong>DMM-03</strong></td>
                    <td>50 – 75</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                  <tr>
                    <td><strong>DMM-04</strong></td>
                    <td>75 – 100</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                  <tr>
                    <td><strong>DMM-05</strong></td>
                    <td>125 – 150</td>
                    <td>—</td>
                    <td>—</td>
                    <td><span class="cp-badge-pending">Plant Inventory</span></td>
                  </tr>
                  <tr>
                    <td><strong>DMM(BALL)</strong></td>
                    <td>0 – 25</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Table 2: Bore Gauges -->
          <div class="cp-table-container light-theme">
            <div class="cp-table-header-bar">
              <h4><i class="fa-solid fa-circle-dot text-gold"></i> Bore Gauges (Internal Diameter Metrology)</h4>
              <span class="cp-table-sub">Calibration Lab: IRCLASS / Geological &amp; Metallurgical Laboratories</span>
            </div>
            <div class="cp-table-responsive">
              <table class="cp-table">
                <thead>
                  <tr>
                    <th>INSTRUMENT ID</th>
                    <th>MEASURING RANGE (MM)</th>
                    <th>CALIBRATION DATE</th>
                    <th>DUE DATE</th>
                    <th>CALIBRATION STATUS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>BG-01</strong></td>
                    <td>010 – 18</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                  <tr>
                    <td><strong>BG-02</strong></td>
                    <td>18 – 50</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                  <tr>
                    <td><strong>BG-03</strong></td>
                    <td>50 – 150</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Table 3: Pin Gauges (Complete Box 01 to 12) -->
          <div class="cp-table-container light-theme">
            <div class="cp-table-header-bar">
              <h4><i class="fa-solid fa-bars text-gold"></i> Pin Gauges (0.50 mm to 12.00 mm Range)</h4>
              <span class="cp-table-sub">Precision Bore &amp; Hole Matrix Verification</span>
            </div>
            <div class="cp-table-responsive">
              <table class="cp-table">
                <thead>
                  <tr>
                    <th>BOX IDENTIFIER</th>
                    <th>RANGE (MM)</th>
                    <th>BOX IDENTIFIER</th>
                    <th>RANGE (MM)</th>
                    <th>BOX IDENTIFIER</th>
                    <th>RANGE (MM)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>PIN BOX-01</strong></td>
                    <td>0.50 – 0.99</td>
                    <td><strong>PIN BOX-05</strong></td>
                    <td>4.01 – 5.00</td>
                    <td><strong>PIN BOX-09</strong></td>
                    <td>8.01 – 9.00</td>
                  </tr>
                  <tr>
                    <td><strong>PIN BOX-02</strong></td>
                    <td>1.00 – 2.00</td>
                    <td><strong>PIN BOX-06</strong></td>
                    <td>5.01 – 6.00</td>
                    <td><strong>PIN BOX-10</strong></td>
                    <td>9.01 – 10.00</td>
                  </tr>
                  <tr>
                    <td><strong>PIN BOX-03</strong></td>
                    <td>2.01 – 3.00</td>
                    <td><strong>PIN BOX-07</strong></td>
                    <td>6.01 – 7.00</td>
                    <td><strong>PIN BOX-11</strong></td>
                    <td>10.01 – 11.00</td>
                  </tr>
                  <tr>
                    <td><strong>PIN BOX-04</strong></td>
                    <td>3.01 – 4.00</td>
                    <td><strong>PIN BOX-08</strong></td>
                    <td>7.01 – 8.00</td>
                    <td><strong>PIN BOX-12</strong></td>
                    <td>11.01 – 12.00</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Table 4: Digital Vernier Calipers -->
          <div class="cp-table-container light-theme">
            <div class="cp-table-header-bar">
              <h4><i class="fa-solid fa-sliders text-gold"></i> Digital Vernier Calipers</h4>
              <span class="cp-table-sub">Shop Floor &amp; Inspection Station Instruments</span>
            </div>
            <div class="cp-table-responsive">
              <table class="cp-table">
                <thead>
                  <tr>
                    <th>INSTRUMENT ID</th>
                    <th>MEASURING RANGE (MM)</th>
                    <th>CALIBRATION DATE</th>
                    <th>DUE DATE</th>
                    <th>STATUS / REMARKS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>DVC-01</strong></td>
                    <td>0 – 150</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                  <tr>
                    <td><strong>DVC-02</strong></td>
                    <td>0 – 300</td>
                    <td>—</td>
                    <td>—</td>
                    <td><span class="cp-badge-pending">Plant Inventory</span></td>
                  </tr>
                  <tr>
                    <td><strong>DVC-03</strong></td>
                    <td>0 – 200</td>
                    <td>—</td>
                    <td>—</td>
                    <td><span class="cp-badge-pending">Plant Inventory</span></td>
                  </tr>
                  <tr>
                    <td><strong>DVC-04</strong></td>
                    <td>0 – 200</td>
                    <td>—</td>
                    <td>—</td>
                    <td><span class="cp-badge-pending">Plant Inventory</span></td>
                  </tr>
                  <tr>
                    <td><strong>DVC-05</strong></td>
                    <td>0 – 150</td>
                    <td>8/10/2026</td>
                    <td>8/9/2027</td>
                    <td><span class="cp-badge-cal"><i class="fa-solid fa-check"></i> Calibrated</span></td>
                  </tr>
                  <tr>
                    <td><strong>DVC-06</strong></td>
                    <td>0 – 150</td>
                    <td>—</td>
                    <td>—</td>
                    <td><span class="cp-badge-new"><i class="fa-solid fa-sparkles"></i> NEW</span></td>
                  </tr>
                  <tr>
                    <td><strong>DVC-07</strong></td>
                    <td>0 – 200</td>
                    <td>—</td>
                    <td>—</td>
                    <td><span class="cp-badge-new"><i class="fa-solid fa-sparkles"></i> NEW</span></td>
                  </tr>
                  <tr>
                    <td><strong>DVC-08</strong></td>
                    <td>0 – 200</td>
                    <td>—</td>
                    <td>—</td>
                    <td><span class="cp-badge-new"><i class="fa-solid fa-sparkles"></i> NEW</span></td>
                  </tr>
                  <tr>
                    <td><strong>DVC-09</strong></td>
                    <td>0 – 300</td>
                    <td>—</td>
                    <td>—</td>
                    <td><span class="cp-badge-new"><i class="fa-solid fa-sparkles"></i> NEW</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Table 5 & 6: Plunger Dial, Gauges & Analogue Micrometers -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
            <!-- Plunger Dial Gauges -->
            <div class="cp-table-container light-theme" style="margin: 0;">
              <div class="cp-table-header-bar">
                <h4><i class="fa-solid fa-gauge text-gold"></i> Plunger Dial Gauges</h4>
                <span class="cp-table-sub">Deflection &amp; Runout</span>
              </div>
              <div class="cp-table-responsive">
                <table class="cp-table">
                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>TRAVEL</th>
                      <th>CAL DATE</th>
                      <th>DUE DATE</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>APD-01</strong></td>
                      <td>2 mm</td>
                      <td>8/10/2026</td>
                      <td>8/9/2027</td>
                    </tr>
                    <tr>
                      <td><strong>APD-02</strong></td>
                      <td>2 mm</td>
                      <td>8/10/2026</td>
                      <td>8/9/2027</td>
                    </tr>
                    <tr>
                      <td><strong>APD-03</strong></td>
                      <td>2 mm</td>
                      <td>8/10/2026</td>
                      <td>8/9/2027</td>
                    </tr>
                    <tr>
                      <td><strong>APD-04</strong></td>
                      <td>10 mm</td>
                      <td>—</td>
                      <td>—</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Analogue Micrometers -->
            <div class="cp-table-container light-theme" style="margin: 0;">
              <div class="cp-table-header-bar">
                <h4><i class="fa-solid fa-arrows-to-circle text-gold"></i> Analogue Micrometers</h4>
                <span class="cp-table-sub">Lab: Mailaralingeshwra</span>
              </div>
              <div class="cp-table-responsive">
                <table class="cp-table">
                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>RANGE</th>
                      <th>CAL DATE</th>
                      <th>DUE DATE</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>AMM-01</strong></td>
                      <td>0 – 25 mm</td>
                      <td>8/10/2026</td>
                      <td>8/9/2027</td>
                    </tr>
                    <tr>
                      <td><strong>AMM-02</strong></td>
                      <td>25 – 50 mm</td>
                      <td>8/10/2026</td>
                      <td>8/9/2027</td>
                    </tr>
                    <tr>
                      <td colspan="4" style="font-size: 0.8rem; color: var(--cp-graphite);">
                        <em>Calibrated by Mailaralingeshwra Precision Instrument, Bengaluru (Tel: 9945791443)</em>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- Table 7: Reference Gauges & Height Gauges -->
          <div class="cp-table-container light-theme" style="margin-top: 24px;">
            <div class="cp-table-header-bar">
              <h4><i class="fa-solid fa-ruler-vertical text-gold"></i> Height Gauges, Slip Gauges &amp; Form Standards</h4>
              <span class="cp-table-sub">Granite Lab Metrology</span>
            </div>
            <div class="cp-table-responsive">
              <table class="cp-table">
                <thead>
                  <tr>
                    <th>INSTRUMENT ID / CODE</th>
                    <th>INSTRUMENT TYPE</th>
                    <th>MEASURING RANGE</th>
                    <th>STATUS / SPECIFICATION</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>DHG-01</strong></td>
                    <td>Mahr Digital Height Gauge</td>
                    <td>0.001 – 350.0 mm</td>
                    <td><span class="cp-badge-new"><i class="fa-solid fa-sparkles"></i> NEW / MHR (Mahr Make)</span></td>
                  </tr>
                  <tr>
                    <td><strong>DHM-01</strong></td>
                    <td>Digital Height Gauge</td>
                    <td>0.001 – 630.0 mm</td>
                    <td><span class="cp-badge-pending">Active Metrology Reference</span></td>
                  </tr>
                  <tr>
                    <td><strong>CSM/ST/0003</strong></td>
                    <td>Mahr 817 CLT 2D Height Gauge</td>
                    <td>0 – 600 mm</td>
                    <td><span class="cp-badge-cal">2D Linear Metrology</span></td>
                  </tr>
                  <tr>
                    <td><strong>THICKNESS GAUGE</strong></td>
                    <td>Feeler / Thickness Gauge Set</td>
                    <td>0.04 – 0.63 mm</td>
                    <td><span class="cp-badge-new"><i class="fa-solid fa-sparkles"></i> NEW</span></td>
                  </tr>
                  <tr>
                    <td><strong>RADIUS--01</strong></td>
                    <td>Radius Gauge Set</td>
                    <td>15.5 – 25 mm</td>
                    <td><span class="cp-badge-pending">Standard Tooling Reference</span></td>
                  </tr>
                  <tr>
                    <td><strong>SLIP GAUGE</strong></td>
                    <td>Precision Slip Gauge Box</td>
                    <td>1.005 – 100 mm</td>
                    <td><span class="cp-badge-new"><i class="fa-solid fa-sparkles"></i> NEW (Grade 0 Reference)</span></td>
                  </tr>
                  <tr>
                    <td><strong>CSM/ST/006</strong></td>
                    <td>Magnetic V-Block</td>
                    <td>100 x 100 mm</td>
                    <td><span class="cp-badge-pending">Prismatic Alignment</span></td>
                  </tr>
                  <tr>
                    <td><strong>CSM/MM/007</strong></td>
                    <td>Tap Gauges Set</td>
                    <td>M2 – M20</td>
                    <td><span class="cp-badge-pending">Thread Lead &amp; Pitch Audit</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 10: QUALITY ASSURANCE AND INSPECTION (MIDNIGHT CHARCOAL)
    html.append('''
      <!-- Section 10: Quality Assurance & Inspection (Midnight Charcoal) -->
      <section class="section-charcoal" id="quality">
        <div class="container">
          <div class="cp-quality-split">
            <div class="cp-quality-text">
              <div class="section-tag-gold">
                <i class="fa-solid fa-microscope"></i> Quality Management System
              </div>
              <h2 style="color: var(--cp-white); font-size: 2.2rem; margin-bottom: 20px;">Dimensional Discipline Governs Every Machined Part</h2>
              <p style="color: var(--cp-silver); font-size: 1.05rem;">
                At <strong>ASCENT ENGINEERING</strong>, quality is built directly into each manufacturing setup rather than checked as an afterthought. Led by qualified technocrats, our inspection protocols enforce strict drawing GD&amp;T compliance, zero-defect principles, and full component traceability.
              </p>

              <div class="cp-quality-items-grid">
                <div class="cp-quality-item">
                  <i class="fa-solid fa-ruler-vertical"></i>
                  <h5>Mahr 2D Metrology</h5>
                  <p>In-house Mahr Digimar 817 CLT 2D height gauge performing motorized 2D step, centerline, and bore position audits.</p>
                </div>

                <div class="cp-quality-item">
                  <i class="fa-solid fa-gem"></i>
                  <h5>Granite Reference Plates</h5>
                  <p>Grade 00 laboratory-grade granite surface plate (630 x 630 x 80 mm) provides absolute flat reference datum.</p>
                </div>

                <div class="cp-quality-item">
                  <i class="fa-solid fa-bullseye"></i>
                  <h5>&lt;100 PPM &amp; &gt;99% Score</h5>
                  <p>Defect reduction targeting &lt;100 PPM and maintaining an audited customer quality score consistently above 99%.</p>
                </div>

                <div class="cp-quality-item">
                  <i class="fa-solid fa-clipboard-check"></i>
                  <h5>First Article Inspection (FAIR)</h5>
                  <p>100% full-dimension First Article Inspection Reports generated before commencing serial batch production runs.</p>
                </div>
              </div>
            </div>

            <div class="cp-quality-visual">
              <div class="cp-quality-img-frame" data-cp-lightbox="images/shopfloor/inspection-mahr-digimar.jpg" data-cp-caption="Ascent Engineering Quality Metrology Station with Mahr 2D Linear Height Gauge">
                <img
                  src="images/shopfloor/inspection-mahr-digimar.jpg"
                  alt="Metrology and Dimensional Inspection Laboratory"
                  loading="lazy"
                />
                <div class="cp-quality-tagline">
                  <i class="fa-solid fa-circle-check"></i> Mahr 2D Linear Metrology Lab
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 11: MANUFACTURING COMPONENTS GALLERY (MIDNIGHT CHARCOAL)
    # Load all component files
    comp_files = sorted(os.listdir('company-profile/images/components'))
    
    html.append('''
      <!-- Section 11: Manufacturing Components Gallery (Midnight Charcoal) -->
      <section class="section-charcoal" id="components" style="border-top: 1px solid var(--cp-border-dark);">
        <div class="container">
          <div class="profile-section-header center">
            <div class="section-tag-gold">
              <i class="fa-solid fa-cubes"></i> Precision Machined Hardware
            </div>
            <h2 class="profile-section-title">Manufacturing Components Gallery</h2>
            <p class="profile-section-desc">
              Extensive portfolio of precision-machined aerospace parts, defense housings, avionics chassis, complex 5-axis contoured impellers, and precision engineering tooling.
            </p>
          </div>

          <!-- Gallery Filter Tabs -->
          <div class="cp-gallery-filters">
            <button class="cp-filter-btn active" data-filter="all">All Components (''' + str(len(comp_files)) + ''')</button>
            <button class="cp-filter-btn" data-filter="aerospace">Aerospace &amp; Defense</button>
            <button class="cp-filter-btn" data-filter="milling">Precision CNC Milling</button>
            <button class="cp-filter-btn" data-filter="avionics">Avionics &amp; Thin-Wall</button>
            <button class="cp-filter-btn" data-filter="tooling">Dies, Moulds &amp; Tooling</button>
          </div>

          <div class="cp-gallery-grid">
''')

    # Add components cards with appropriate categorization
    for idx, f in enumerate(comp_files, 1):
        # Categorize
        if f.startswith('ascent_page_11') or 'impeller' in f or idx in [1, 5, 8, 12, 18, 22, 28, 35]:
            cat = 'aerospace'
            badge = 'Aerospace Component'
        elif 'avionics' in f or f.startswith('ascent_page_10') or f.startswith('ascent_page_8') or idx in [2, 6, 14, 19, 25]:
            cat = 'avionics'
            badge = 'Avionics Enclosure'
        elif f.startswith('skdm') and idx in [30, 31, 32, 33, 34, 38, 42]:
            cat = 'tooling'
            badge = 'Dies, Moulds & Tooling'
        else:
            cat = 'milling'
            badge = 'Precision CNC Milling'

        title = f"Precision Component #{idx:02d}"
        caption = f"Ascent Engineering Precision Machined Component #{idx:02d} — Tight Tolerance CNC Machining"

        html.append(f'''            <!-- Component {idx} -->
            <div class="cp-gallery-card" data-category="{cat}" data-cp-lightbox="images/components/{f}" data-cp-caption="{caption}">
              <img src="images/components/{f}" alt="{title}" loading="lazy" />
              <div class="cp-gallery-card-overlay">
                <h5>{title}</h5>
                <span>{badge}</span>
              </div>
            </div>
''')

    html.append('''          </div>
        </div>
      </section>
''')

    # SECTION 12: SHOP-FLOOR AND INFRASTRUCTURE GALLERY (WARM IVORY)
    # User special prompt: "use multiple images from shopfloor inside ascent company profile folder ok"
    shopfloor_items = [
        ("facility-panoramic-hero.jpg", "Ascent Engineering Facility Panoramic Overview", "Plant Overview • 3,600 Sq. M Facility", "Peenya 3rd Stage Facility"),
        ("facility-vmc-floor-1.jpg", "Ascent Engineering VMC Production Machine Line", "Active Production Fleet", "3-Axis & 4-Axis VMC Bays"),
        ("WhatsApp_Image_2026-11-03_at_11.32.32_AM.jpeg", "Actual Shop Floor Overview & Production Bays", "Ground Floor, B 40 Bay", "Actual Ascent Shopfloor"),
        ("WhatsApp_Image_2026-11-03_at_11.32.32_AM_1.jpeg", "VMC Machine Enclosure & Workstation Interface", "Machining Bay 01", "Precision Setup Station"),
        ("WhatsApp_Image_2026-11-03_at_11.32.33_AM.jpeg", "CNC Production Aisle & Operator Console", "Machine Station 02", "Operator Control Console"),
        ("WhatsApp_Image_2026-11-03_at_11.32.33_AM_1.jpeg", "Component Staging & Machine Bay Perspective", "Production Floor Line", "Workpiece In-Process Staging"),
        ("WhatsApp_Image_2026-11-03_at_11.32.33_AM_2.jpeg", "Multi-Machine Bay Alignment & Tooling Setup", "Production Line Aisle", "Continuous Machining Bays"),
        ("WhatsApp_Image_2026-11-03_at_11.32.34_AM.jpeg", "In-Process Inspection & Fixturing Staging Area", "Metrology Staging", "Quality Inspection Bench"),
        ("WhatsApp_Image_2026-11-03_at_11.48.02_AM.jpeg", "Shop Floor Wide Perspective & Facility Layout", "3,600 Sq. M Plant Floor", "Spacious Industrial Layout"),
        ("inspection-mahr-digimar.jpg", "In-House Quality Metrology Lab with Mahr 2D Height Gauge", "Metrology Lab", "Mahr Digimar 817 CLT 2D"),
        ("inspection-mahr-studio.jpg", "Granite Surface Plate & Dimensional Inspection Desk", "Quality Assurance", "Grade 00 Granite Reference"),
        ("shop-floor-aisle.jpg", "Ascent Engineering High-Precision Machine Aisle", "Machining Corridor", "Peenya Industrial Area"),
        ("shop-floor-featured.jpg", "Ascent Engineering VMC Fleet Production Perspective", "Fleet Operations", "Multi-Axis Machining"),
        ("shop-floor-wide.jpg", "Wide Manufacturing Floor & Auxiliary Support Systems", "Plant Infrastructure", "Auxiliary Compressor & Utilities"),
        ("skdm_shopfloor_overview.jpeg", "Comparative Precision Machine Shop Layout Reference", "Layout Reference", "Precision Tooling Station")
    ]

    html.append('''
      <!-- Section 12: Shop-Floor & Infrastructure Gallery (Warm Ivory) -->
      <section class="section-ivory" id="shopfloor">
        <div class="container">
          <div class="profile-section-header center">
            <div class="section-tag-gold">
              <i class="fa-solid fa-camera"></i> Authentic Manufacturing Environment
            </div>
            <h2 class="profile-section-title">Shop-Floor &amp; Infrastructure Gallery</h2>
            <p class="profile-section-desc">
              Visual tour of our actual 3,600 sq. meter manufacturing facility at Ground Floor, B 40 &amp; #240/P6 Industrial Area, Peenya 3rd Stage, Bangalore, showcasing our CNC bays, tooling, in-process staging, and metrology labs.
            </p>
          </div>

          <div class="cp-shopfloor-gallery-grid">
''')

    for sf_img, sf_title, sf_sub, sf_badge in shopfloor_items:
        html.append(f'''            <!-- Shopfloor Card: {sf_img} -->
            <div class="cp-sf-card" data-cp-lightbox="images/shopfloor/{sf_img}" data-cp-caption="{sf_title} — Ascent Engineering, Peenya, Bengaluru">
              <span class="cp-sf-badge-authentic"><i class="fa-solid fa-industry"></i> {sf_badge}</span>
              <img src="images/shopfloor/{sf_img}" alt="{sf_title}" loading="lazy" />
              <div class="cp-sf-overlay">
                <h5>{sf_title}</h5>
                <span>{sf_sub}</span>
              </div>
            </div>
''')

    html.append('''          </div>
        </div>
      </section>
''')

    # SECTION 13: INDUSTRIES SERVED (MIDNIGHT CHARCOAL)
    html.append('''
      <!-- Section 13: Industries Served (Midnight Charcoal) -->
      <section class="section-charcoal" id="industries">
        <div class="container">
          <div class="profile-section-header center">
            <div class="section-tag-gold">
              <i class="fa-solid fa-plane-up"></i> Market Sectors
            </div>
            <h2 class="profile-section-title">Industries We Serve</h2>
            <p class="profile-section-desc">
              Ascent Engineering is established to serve critical industries requiring rigorous metallurgical compliance, fine surface finishes, and strict delivery timelines.
            </p>
          </div>

          <div class="cp-industries-grid">
            <!-- 1. Aerospace -->
            <div class="cp-industry-item">
              <div class="cp-industry-img" data-cp-lightbox="../img/aerospace-industry.jpg" data-cp-caption="Aerospace Component Manufacturing — Ascent Engineering">
                <img src="../img/aerospace-industry.jpg" alt="Aerospace Component Manufacturing" loading="lazy" />
              </div>
              <div class="cp-industry-content">
                <h3 class="cp-industry-name">Aerospace</h3>
                <p class="cp-industry-desc">
                  Flight-critical airframe brackets, avionics chassis, impellers, turbine discs, sensor housings, and thin-wall enclosures machined from high-strength aerospace alloys.
                </p>
                <div class="cp-industry-alloys">
                  <strong>Materials:</strong> Aluminium 6061-T6, 7075-T651, Stainless Steel 316, Aircraft Titanium.
                </div>
              </div>
            </div>

            <!-- 2. Defense -->
            <div class="cp-industry-item">
              <div class="cp-industry-img" data-cp-lightbox="../img/defence-engineering.jpg" data-cp-caption="Defense Engineering Component Machining — Ascent Engineering">
                <img src="../img/defence-engineering.jpg" alt="Defense Engineering Components" loading="lazy" />
              </div>
              <div class="cp-industry-content">
                <h3 class="cp-industry-name">Defense</h3>
                <p class="cp-industry-desc">
                  Tactical electronic enclosures, radar guidance housings, sealed manifolds, and ruggedized mechanical assemblies produced under strict NDA security.
                </p>
                <div class="cp-industry-alloys">
                  <strong>Materials:</strong> EN19, EN24, Armored aluminium, specialty alloys.
                </div>
              </div>
            </div>

            <!-- 3. Automobile -->
            <div class="cp-industry-item">
              <div class="cp-industry-img" data-cp-lightbox="../img/precision-engineering.jpg" data-cp-caption="Automobile Precision Component Manufacturing">
                <img src="../img/precision-engineering.jpg" alt="Automobile Machined Components" loading="lazy" />
              </div>
              <div class="cp-industry-content">
                <h3 class="cp-industry-name">Automobile</h3>
                <p class="cp-industry-desc">
                  Engine mounts, transmission blocks, suspension knuckles, and high-performance powertrain parts requiring repeatable high-volume batch precision.
                </p>
                <div class="cp-industry-alloys">
                  <strong>Materials:</strong> Forged steel, ductile iron, aluminium alloys, bronze bushings.
                </div>
              </div>
            </div>

            <!-- 4. Automation & Robotics -->
            <div class="cp-industry-item">
              <div class="cp-industry-img" data-cp-lightbox="../img/abt/metal-industry-workshop-precision-machinery-automated-production-line-robotic-arm-generated-by-ai-free-photo.jpg" data-cp-caption="Automation & Robotics Tooling Components">
                <img src="../img/abt/metal-industry-workshop-precision-machinery-automated-production-line-robotic-arm-generated-by-ai-free-photo.jpg" alt="Automation & Robotics Machined Parts" loading="lazy" />
              </div>
              <div class="cp-industry-content">
                <h3 class="cp-industry-name">Automation &amp; Robotics</h3>
                <p class="cp-industry-desc">
                  End-effector brackets, precision indexing plates, robotic arm linkages, linear slide blocks, and sensor brackets for automated production lines.
                </p>
                <div class="cp-industry-alloys">
                  <strong>Materials:</strong> Hardened tool steels, ground aluminium plate, Delrin, brass.
                </div>
              </div>
            </div>

            <!-- 5. Hydraulics & Fluid Power -->
            <div class="cp-industry-item">
              <div class="cp-industry-img" data-cp-lightbox="images/components/ascent_component_02.jpeg" data-cp-caption="Hydraulic Manifolds & Valve Blocks">
                <img src="images/components/ascent_component_02.jpeg" alt="Hydraulic Manifolds & Valve Blocks" loading="lazy" />
              </div>
              <div class="cp-industry-content">
                <h3 class="cp-industry-name">Hydraulic Systems</h3>
                <p class="cp-industry-desc">
                  High-pressure hydraulic manifold blocks, valve bodies, cylinder heads, and fluid connector flanges requiring cross-hole drilling and leak-proof finishes.
                </p>
                <div class="cp-industry-alloys">
                  <strong>Materials:</strong> Ductile iron, carbon steels (EN8/EN9), stainless steel 316.
                </div>
              </div>
            </div>

            <!-- 6. Electronics & Precision Engineering -->
            <div class="cp-industry-item">
              <div class="cp-industry-img" data-cp-lightbox="images/components/ascent_component_04.jpeg" data-cp-caption="Electronics Heat Sinks & Sealed Enclosures">
                <img src="images/components/ascent_component_04.jpeg" alt="Electronics Heat Sinks & Enclosures" loading="lazy" />
              </div>
              <div class="cp-industry-content">
                <h3 class="cp-industry-name">Electronics &amp; Enclosures</h3>
                <p class="cp-industry-desc">
                  Fin-array heatsinks, RF shielding enclosures, PCB mounting chassis, and precision instrument housings machined to sub-millimeter wall thicknesses.
                </p>
                <div class="cp-industry-alloys">
                  <strong>Materials:</strong> High-conductivity aluminium, copper, brass alloys.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 14: FUTURE DEVELOPMENT & EXPANSION PLANS (WARM IVORY)
    html.append('''
      <!-- Section 14: Future Development & Expansion Plans (Warm Ivory) -->
      <section class="section-ivory" id="expansion">
        <div class="container">
          <div class="profile-section-header center">
            <div class="section-tag-gold">
              <i class="fa-solid fa-chart-line"></i> Strategic Growth
            </div>
            <h2 class="profile-section-title">Future Development &amp; Expansion Plans</h2>
            <p class="profile-section-desc">
              In alignment with our vision of growing to a world-class accredited manufacturer, Ascent Engineering is planning strategic expansions in machinery capacity and metrology automation.
            </p>
          </div>

          <div class="cp-expansion-grid">
            <div class="cp-expansion-card" style="background: #fff; border: 1px solid var(--cp-border-light); border-left: 4px solid var(--cp-gold);">
              <h4 style="color: var(--cp-charcoal);"><i class="fa-solid fa-arrows-spin text-gold"></i> Multi-Axis Machine Expansion</h4>
              <p style="color: var(--cp-graphite);">
                Expanding simultaneous 4th and 5th axis vertical machining capacity to support increased aerospace program volumes and complex compound-angle contouring.
              </p>
            </div>

            <div class="cp-expansion-card" style="background: #fff; border: 1px solid var(--cp-border-light); border-left: 4px solid var(--cp-gold);">
              <h4 style="color: var(--cp-charcoal);"><i class="fa-solid fa-microscope text-gold"></i> CMM Metrology Automation</h4>
              <p style="color: var(--cp-graphite);">
                Implementing in-house Bridge Coordinate Measuring Machine (CMM) inspection to augment our Mahr 2D height gauge and provide automated 3D CAD comparison reports.
              </p>
            </div>

            <div class="cp-expansion-card" style="background: #fff; border: 1px solid var(--cp-border-light); border-left: 4px solid var(--cp-gold);">
              <h4 style="color: var(--cp-charcoal);"><i class="fa-solid fa-expand text-gold"></i> Large-Format Machining Platform</h4>
              <p style="color: var(--cp-graphite);">
                Planning implementation of large-envelope vertical machining capacity (2000 x 1000 x 1000 mm) to accommodate oversized aerospace bulkheads and large structural tooling.
              </p>
            </div>
          </div>
        </div>
      </section>
''')

    # SECTION 15: CONTACT DETAILS & CLOSING PAGE (MIDNIGHT CHARCOAL)
    html.append('''
      <!-- Section 15: Contact Details & Closing Section (Midnight Charcoal) -->
      <section class="section-charcoal" id="contact">
        <div class="container">
          <div class="profile-section-header">
            <div class="section-tag-gold">
              <i class="fa-solid fa-envelope"></i> Commercial &amp; Technical Engagement
            </div>
            <h2 class="profile-section-title">Contact &amp; Corporate Consultation</h2>
            <p class="profile-section-desc">
              Submit your 2D manufacturing drawings and 3D CAD models (STEP / IGES / PDF) for quotation, DFM engineering analysis, and batch production feasibility.
            </p>
          </div>

          <div class="cp-contact-split">
            <!-- Left: Official Verified Details -->
            <div class="cp-contact-info-panel">
              <div class="cp-contact-card">
                <div class="cp-contact-icon"><i class="fa-solid fa-location-dot"></i></div>
                <div class="cp-contact-detail">
                  <h5>Facility &amp; Plant Location</h5>
                  <p>
                    <strong>ASCENT ENGINEERING</strong><br />
                    Ground Floor, B 40 &amp; #240/P6 Industrial Area,<br />
                    1st Main Road, Peenya 3rd Stage, Bangalore – 560058, Karnataka, India
                  </p>
                </div>
              </div>

              <div class="cp-contact-card">
                <div class="cp-contact-icon"><i class="fa-solid fa-phone"></i></div>
                <div class="cp-contact-detail">
                  <h5>Direct Telephone &amp; Technical Lead</h5>
                  <p>
                    Contact Person: <strong>M V Kumara Swamy</strong><br />
                    Phone: <a href="tel:7353150847"><strong>+91 73531 50847</strong></a> / <a href="tel:7353140847"><strong>+91 73531 40847</strong></a><br />
                    Hours: Monday – Saturday: 9:00 AM – 7:30 PM IST
                  </p>
                </div>
              </div>

              <div class="cp-contact-card">
                <div class="cp-contact-icon"><i class="fa-solid fa-envelope"></i></div>
                <div class="cp-contact-detail">
                  <h5>Official Technical Email &amp; Tax ID</h5>
                  <p>
                    Official Email: <a href="mailto:ascenteng03@gmail.com"><strong>ascenteng03@gmail.com</strong></a><br />
                    GSTIN Identification: <strong class="text-gold">29DCAPR1495B1ZK</strong> / <strong class="text-gold">29GAUPB9697A1ZZ</strong>
                  </p>
                </div>
              </div>

              <!-- Google Map Embed -->
              <div class="cp-map-box">
                <iframe
                  title="Ascent Engineering Peenya Facility Location"
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3886.6852445831527!2d77.5050518!3d13.0333857!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d1f11c76df7%3A0x6b4498ec5ea8c92a!2sPeenya%203rd%20Stage%2C%20Peenya%2C%20Bengaluru%2C%20Karnataka!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin"
                  loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"
                  allowfullscreen=""
                ></iframe>
              </div>
            </div>

            <!-- Right: Corporate RFQ Form -->
            <div class="cp-form-container">
              <h3 class="cp-form-title">Submit Corporate RFQ</h3>
              <p class="cp-form-subtitle">
                Provide your part geometry, alloy specifications, and target quantities. Inquiries are handled with strict engineering confidentiality and NDA protocols.
              </p>

              <form id="cpContactForm" novalidate>
                <div class="cp-form-row">
                  <div class="cp-form-group">
                    <label class="cp-form-label" for="cpName">Full Name *</label>
                    <input type="text" id="cpName" class="cp-form-control" placeholder="e.g. Ramesh Chandra" required />
                  </div>
                  <div class="cp-form-group">
                    <label class="cp-form-label" for="cpCompany">Company / Enterprise *</label>
                    <input type="text" id="cpCompany" class="cp-form-control" placeholder="e.g. Aerospace Systems Ltd" required />
                  </div>
                </div>

                <div class="cp-form-row">
                  <div class="cp-form-group">
                    <label class="cp-form-label" for="cpEmail">Business Email *</label>
                    <input type="email" id="cpEmail" class="cp-form-control" placeholder="name@company.com" required />
                  </div>
                  <div class="cp-form-group">
                    <label class="cp-form-label" for="cpPhone">Phone Number</label>
                    <input type="tel" id="cpPhone" class="cp-form-control" placeholder="+91 XXXXX XXXXX" />
                  </div>
                </div>

                <div class="cp-form-group">
                  <label class="cp-form-label" for="cpService">Primary Machining Capability Required *</label>
                  <select id="cpService" class="cp-form-control" required>
                    <option value="5-Axis CNC Machining">5-Axis Simultaneous Machining (Hurco VC 500i)</option>
                    <option value="4-Axis Rotary Milling">4-Axis Rotary Indexing (Yantrang VX500)</option>
                    <option value="3-Axis VMC Batch Machining">3-Axis VMC Precision Milling (Yantrang VX850 / Cosmos)</option>
                    <option value="Aerospace Component Manufacturing">Aerospace Component Manufacturing</option>
                    <option value="Defense Hardware Machining">Defense Hardware Machining</option>
                    <option value="Precision Drilling & Tapping">Precision Drilling &amp; Synchronized Tapping</option>
                    <option value="Prototype & Tooling">Prototype &amp; Fixture Tooling</option>
                  </select>
                </div>

                <div class="cp-form-group">
                  <label class="cp-form-label" for="cpMessage">Project Details &amp; Technical Requirements *</label>
                  <textarea
                    id="cpMessage"
                    class="cp-form-control"
                    placeholder="Describe material grade (e.g. Aluminium 6061/7075, Stainless Steel 304/316, EN19/EN24, Titanium), key drawing tolerances, batch size, and delivery timeframe..."
                    required
                  ></textarea>
                </div>

                <button type="submit" class="cp-btn cp-btn-gold" style="width: 100%; padding: 15px;">
                  <span>Submit Corporate RFQ</span>
                  <i class="fa-solid fa-arrow-right"></i>
                </button>

                <div id="cpStatusAlert" class="cp-status-alert"></div>
              </form>
            </div>
          </div>

          <!-- Official Respectful Closing Card from Ascent PDF Page 13 -->
          <div class="cp-closing-banner">
            <div style="font-size: 2.2rem; color: var(--cp-gold); margin-bottom: 12px;">
              <i class="fa-solid fa-hands-praying"></i>
            </div>
            <h3>YOUR FEEDBACK AND SUGGESTIONS ARE VALUED HERE....!</h3>
            <p>
              We put all our resources, infrastructure, human resources, and precision machining expertise at your service. Thank you for considering <strong>ASCENT ENGINEERING</strong> as your valued manufacturing partner.
            </p>
          </div>
        </div>
      </section>
    </main>

    <!-- Corporate Footer (Midnight Charcoal) -->
    <footer class="cp-footer">
      <div class="container">
        <div class="cp-footer-top">
          <!-- Col 1: Brand Info -->
          <div class="cp-footer-brand">
            <h4>ASCENT <span>ENGINEERING</span></h4>
            <p>
              Aerospace &amp; Defense Parts Manufacturer. Equipped with simultaneous 5-axis vertical machining capability and a multi-station CNC production fleet in Peenya 3rd Stage, Bangalore.
            </p>
            <div style="margin-top: 14px; font-size: 0.82rem; color: var(--cp-gold);">
              <i class="fa-solid fa-id-card"></i> GSTIN: <strong>29DCAPR1495B1ZK</strong> &bull; <strong>29GAUPB9697A1ZZ</strong>
            </div>
          </div>

          <!-- Col 2: Profile Links -->
          <div class="cp-footer-col">
            <h5>Profile Sections</h5>
            <ul class="cp-footer-links">
              <li><a href="#about"><i class="fa-solid fa-chevron-right text-gold"></i> Company Overview</a></li>
              <li><a href="#general-info"><i class="fa-solid fa-chevron-right text-gold"></i> General Information</a></li>
              <li><a href="#strengths"><i class="fa-solid fa-chevron-right text-gold"></i> 5 Pillars of Strength</a></li>
              <li><a href="#machinery"><i class="fa-solid fa-chevron-right text-gold"></i> Complete Machinery List</a></li>
              <li><a href="#instruments"><i class="fa-solid fa-chevron-right text-gold"></i> Instrument Calibration</a></li>
              <li><a href="#components"><i class="fa-solid fa-chevron-right text-gold"></i> Components Gallery</a></li>
              <li><a href="#shopfloor"><i class="fa-solid fa-chevron-right text-gold"></i> Shop Floor Gallery</a></li>
            </ul>
          </div>

          <!-- Col 3: Facility Location -->
          <div class="cp-footer-col">
            <h5>Plant Location</h5>
            <div style="font-size: 0.85rem; line-height: 1.6; color: var(--cp-silver);">
              <p style="margin-bottom: 8px;">
                <i class="fa-solid fa-location-dot text-gold" style="margin-right: 6px;"></i>
                Ground Floor, B 40 &amp; #240/P6 Industrial Area, 1st Main Road, Peenya 3rd Stage, Bangalore – 560058
              </p>
              <p style="margin-bottom: 8px;">
                <i class="fa-solid fa-phone text-gold" style="margin-right: 6px;"></i>
                <a href="tel:7353150847" style="color: var(--cp-white);">+91 73531 50847</a> / 
                <a href="tel:7353140847" style="color: var(--cp-white);">+91 73531 40847</a>
              </p>
              <p>
                <i class="fa-solid fa-envelope text-gold" style="margin-right: 6px;"></i>
                <a href="mailto:ascenteng03@gmail.com" style="color: var(--cp-white);">ascenteng03@gmail.com</a>
              </p>
            </div>
          </div>
        </div>

        <div class="cp-footer-bottom">
          <div>
            &copy; <span id="cpCurrentYear">2026</span> ASCENT ENGINEERING. All rights reserved. Precision Multi-Axis Machining, Peenya, Bengaluru.
          </div>
          <div>
            Ground Floor, B 40 &amp; #240/P6 Industrial Area, Peenya 3rd Stage, Bangalore – 560058
          </div>
        </div>
      </div>
    </footer>

    <!-- Interactive Lightbox Modal -->
    <div class="cp-lightbox" id="cpLightbox">
      <div class="cp-lightbox-box">
        <button class="cp-lightbox-close" id="cpLightboxClose" aria-label="Close image">&times;</button>
        <img src="" alt="" id="cpLightboxImg" />
        <div class="cp-lightbox-caption" id="cpLightboxCaption"></div>
      </div>
    </div>

    <!-- Standalone Profile Script (Isolated) -->
    <script src="profile.js"></script>
    <script>
      document.getElementById('cpCurrentYear').textContent = new Date().getFullYear();
    </script>
  </body>
</html>
''')

    final_content = "".join(html)
    with open('company-profile/index.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Generated company-profile/index.html successfully! Length: {len(final_content)} characters.")

if __name__ == '__main__':
    generate_html()
