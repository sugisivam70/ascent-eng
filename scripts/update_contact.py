# update_contact.py
with open('contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update navigation
old_nav = """        <!-- Desktop Navigation Links -->
        <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
          <a href="index.html" class="nav-link">About</a>
          <a href="ourmachine.html" class="nav-link">Our Machines</a>
          <a href="contact.html" class="nav-link active">Contact</a>
        </nav>"""

new_nav = """        <!-- Desktop Navigation Links -->
        <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
          <a href="index.html" class="nav-link">About</a>
          <a href="ourmachine.html" class="nav-link">Our Machines</a>
          <a href="services.html" class="nav-link">Services</a>
          <a href="contact.html" class="nav-link active">Contact</a>
        </nav>"""

if old_nav in text:
    text = text.replace(old_nav, new_nav)
    print("contact.html: Navigation updated.")

# 2. Update footer nav
old_footer = """            <ul class="footer-links">
              <li><a href="index.html">About Ascent Engineering</a></li>
              <li><a href="ourmachine.html">Our Machines &amp; Capacity</a></li>
              <li><a href="contact.html">Contact &amp; RFQ</a></li>
            </ul>"""

new_footer = """            <ul class="footer-links">
              <li><a href="index.html">About Ascent Engineering</a></li>
              <li><a href="ourmachine.html">Our Machines &amp; Capacity</a></li>
              <li><a href="services.html">Services &amp; Capabilities</a></li>
              <li><a href="contact.html">Contact &amp; RFQ</a></li>
            </ul>"""

if old_footer in text:
    text = text.replace(old_footer, new_footer)
    print("contact.html: Footer nav updated.")

# 3. Update Service Required dropdown with all 9 services
old_dropdown = """                  <select id="serviceRequired" class="form-control" required>
                    <option value="5-Axis CNC Machining">5-Axis CNC Machining</option>
                    <option value="3-Axis VMC Machining">3-Axis VMC Machining</option>
                    <option value="CNC Tapping">CNC Tapping</option>
                    <option value="Precision Component Manufacturing">Precision Component Manufacturing</option>
                    <option value="Other">Other</option>
                  </select>"""

new_dropdown = """                  <select id="serviceRequired" class="form-control" required>
                    <option value="" disabled selected>-- Select a Machining Service --</option>
                    <option value="CNC Milling">CNC Milling</option>
                    <option value="5-Axis CNC Machining">5-Axis CNC Machining</option>
                    <option value="Precision Component Manufacturing">Precision Component Manufacturing</option>
                    <option value="Aerospace Component Machining">Aerospace Component Machining</option>
                    <option value="Defense Component Manufacturing">Defense Component Manufacturing</option>
                    <option value="VMC Machining">VMC Machining</option>
                    <option value="Precision Drilling and Tapping">Precision Drilling and Tapping</option>
                    <option value="Custom Engineering Components">Custom Engineering Components</option>
                    <option value="Prototype and Small-Batch Manufacturing">Prototype and Small-Batch Manufacturing</option>
                    <option value="General Engineering RFQ / Other">General Engineering RFQ / Other</option>
                  </select>"""

if old_dropdown in text:
    text = text.replace(old_dropdown, new_dropdown)
    print("contact.html: Service dropdown expanded with all 9 services.")

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Clean redirect for contact/index.html
import os
if os.path.exists('contact/index.html'):
    with open('contact/index.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="refresh" content="0; url=../contact.html" />
    <title>Redirecting to Contact | ASCENT ENGINEERING</title>
    <script>
      window.location.href = '../contact.html';
    </script>
  </head>
  <body>
    <p>Redirecting to <a href="../contact.html">Contact</a>...</p>
  </body>
</html>
''')
    print("contact/index.html updated with clean redirect.")
