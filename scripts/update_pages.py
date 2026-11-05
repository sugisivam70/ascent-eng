# update_pages.py
with open('ourmachine.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update nav
old_nav = """        <!-- Desktop Navigation Links -->
        <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
          <a href="index.html" class="nav-link">About</a>
          <a href="ourmachine.html" class="nav-link active">Our Machines</a>
          <a href="contact.html" class="nav-link">Contact</a>
        </nav>"""

new_nav = """        <!-- Desktop Navigation Links -->
        <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
          <a href="index.html" class="nav-link">About</a>
          <a href="ourmachine.html" class="nav-link active">Our Machines</a>
          <a href="services.html" class="nav-link">Services</a>
          <a href="contact.html" class="nav-link">Contact</a>
        </nav>"""

if old_nav in text:
    text = text.replace(old_nav, new_nav)
    print("ourmachine.html: Navigation updated successfully.")
else:
    print("ourmachine.html: Warning - old_nav pattern not found.")

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
    print("ourmachine.html: Footer nav updated.")

# 3. Update VMC Cap image to authentic shop floor photo
text = text.replace(
    'src="img/generated/cnc-cutting-coolant.jpg"\n                  alt="3-Axis Precision VMC Machining"',
    'src="img/ascent/shop-floor-featured.jpg"\n                  alt="3-Axis Precision VMC Machining Fleet on Ascent Engineering Shop Floor"'
)

with open('ourmachine.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Also check our-machines/index.html if present
import os
if os.path.exists('our-machines/index.html'):
    with open('our-machines/index.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="refresh" content="0; url=../ourmachine.html" />
    <title>Redirecting to Our Machines | ASCENT ENGINEERING</title>
    <script>
      window.location.href = '../ourmachine.html';
    </script>
  </head>
  <body>
    <p>Redirecting to <a href="../ourmachine.html">Our Machines</a>...</p>
  </body>
</html>
''')
    print("our-machines/index.html updated with clean redirect.")
