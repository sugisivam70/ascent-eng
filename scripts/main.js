/**
 * ASCENT ENGINEERING - Official Website Scripts
 * Aerospace & Defense Parts Manufacturer | Peenya, Bengaluru
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobileMenuBtn');
  const navLinks = document.getElementById('navLinks');

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      navLinks.classList.toggle('mobile-open');
      const icon = mobileToggle.querySelector('i');
      if (icon) {
        if (navLinks.classList.contains('mobile-open')) {
          icon.className = 'fa-solid fa-xmark';
        } else {
          icon.className = 'fa-solid fa-bars';
        }
      }
    });

    // Close when clicking a nav link
    navLinks.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('mobile-open');
        const icon = mobileToggle.querySelector('i');
        if (icon) icon.className = 'fa-solid fa-bars';
      });
    });
  }

  // 2. Navbar Scroll Effect
  const navbar = document.getElementById('mainNavbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  }

  // 3. Image Lightbox for Galleries
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  const lightboxClose = document.getElementById('lightboxClose');

  if (lightboxModal && lightboxImg) {
    const clickableItems = document.querySelectorAll('[data-lightbox-src]');
    clickableItems.forEach(item => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        const src = item.getAttribute('data-lightbox-src') || item.querySelector('img')?.src;
        const caption = item.getAttribute('data-lightbox-title') || item.querySelector('img')?.alt || '';
        if (src) {
          lightboxImg.src = src;
          if (lightboxCaption) lightboxCaption.textContent = caption;
          lightboxModal.classList.add('active');
          document.body.style.overflow = 'hidden';
        }
      });
    });

    const closeLightbox = () => {
      lightboxModal.classList.remove('active');
      document.body.style.overflow = '';
    };

    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    lightboxModal.addEventListener('click', (e) => {
      if (e.target === lightboxModal) closeLightbox();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lightboxModal.classList.contains('active')) {
        closeLightbox();
      }
    });
  }

  // 4. Contact Form Validation & Real Submission Handler
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    const feedbackBox = document.getElementById('formFeedback');

    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = contactForm.querySelector('#fullName');
      const companyInput = contactForm.querySelector('#companyName');
      const emailInput = contactForm.querySelector('#emailAddress');
      const phoneInput = contactForm.querySelector('#phoneNumber');
      const serviceInput = contactForm.querySelector('#serviceRequired');
      const messageInput = contactForm.querySelector('#projectDescription') || contactForm.querySelector('#projectMessage');

      const name = nameInput ? nameInput.value.trim() : '';
      const company = companyInput ? companyInput.value.trim() : '';
      const email = emailInput ? emailInput.value.trim() : '';
      const phone = phoneInput ? phoneInput.value.trim() : '';
      const service = serviceInput ? serviceInput.value : '5-Axis CNC Machining';
      const message = messageInput ? messageInput.value.trim() : '';

      // Reset errors
      contactForm.querySelectorAll('.form-control').forEach(el => el.classList.remove('is-invalid'));
      contactForm.querySelectorAll('.form-error-feedback').forEach(el => el.classList.remove('active'));

      let hasError = false;

      // Validate Name
      if (!name) {
        if (nameInput) nameInput.classList.add('is-invalid');
        const err = contactForm.querySelector('#nameError');
        if (err) err.classList.add('active');
        hasError = true;
      }

      // Validate Company
      if (!company) {
        if (companyInput) companyInput.classList.add('is-invalid');
        const err = contactForm.querySelector('#companyError');
        if (err) err.classList.add('active');
        hasError = true;
      }

      // Validate Email
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!email || !emailRegex.test(email)) {
        if (emailInput) emailInput.classList.add('is-invalid');
        const err = contactForm.querySelector('#emailError');
        if (err) err.classList.add('active');
        hasError = true;
      }

      // Validate Phone (allow international, minimum 8 digits)
      const phoneClean = phone.replace(/[^0-9]/g, '');
      if (!phone || phoneClean.length < 8) {
        if (phoneInput) phoneInput.classList.add('is-invalid');
        const err = contactForm.querySelector('#phoneError');
        if (err) err.classList.add('active');
        hasError = true;
      }

      // Validate Message
      if (!message) {
        if (messageInput) messageInput.classList.add('is-invalid');
        const err = contactForm.querySelector('#messageError');
        if (err) err.classList.add('active');
        hasError = true;
      }

      if (hasError) {
        if (feedbackBox) {
          feedbackBox.className = 'form-status-alert info';
          feedbackBox.style.display = 'block';
          feedbackBox.style.background = '#FEF2F2';
          feedbackBox.style.borderColor = '#FECACA';
          feedbackBox.style.color = '#B91C1C';
          feedbackBox.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> <strong>Validation Notice:</strong> Please correct the highlighted fields above.';
        }
        return;
      }

      // Prepare truthful submission details
      const subject = encodeURIComponent(`Ascent Engineering RFQ: ${service} - ${company}`);
      const bodyContent = 
`ASCENT ENGINEERING - Business Inquiry & RFQ

Contact Details:
- Name: ${name}
- Company: ${company}
- Email: ${email}
- Phone: ${phone}
- Service Required: ${service}

Project Description & Specifications:
${message}

Facility: Ascent Engineering, Ground Floor, B 40, Peenya 3rd Stage, 1st Main Road, Bengaluru – 560058`;

      const mailtoUrl = `mailto:ascenteng03@gmail.com?subject=${subject}&body=${encodeURIComponent(bodyContent)}`;
      const waText = encodeURIComponent(`Hello Ascent Engineering, my name is ${name} (${company}). I would like to inquire regarding ${service}: ${message}`);
      const waUrl = `https://wa.me/917353140847?text=${waText}`;

      // Show transparent pending-backend message with instant functional dispatch buttons
      if (feedbackBox) {
        feedbackBox.className = 'form-status-alert info';
        feedbackBox.style.display = 'block';
        feedbackBox.style.background = '#F0F9FF';
        feedbackBox.style.borderColor = '#BAE6FD';
        feedbackBox.style.color = '#0369A1';
        feedbackBox.innerHTML = `
          <div style="margin-bottom: 10px;">
            <i class="fa-solid fa-circle-info" style="color: #0284C7; font-size: 1.1rem; margin-right: 6px;"></i>
            <strong>Inquiry Formulated – Direct Dispatch Ready</strong>
          </div>
          <p style="font-size: 0.88rem; line-height: 1.55; color: #334155; margin-bottom: 14px;">
            Thank you, <strong>${name}</strong>. Your inquiry for <strong>${service}</strong> has been structured. Because live automated backend form processing is currently pending server deployment, you can immediately send these formatted details to our engineering team via Email or WhatsApp with one click:
          </p>
          <div style="display: flex; gap: 12px; flex-wrap: wrap;">
            <a href="${mailtoUrl}" class="btn btn-primary" style="padding: 8px 18px; font-size: 0.88rem;">
              <i class="fa-solid fa-envelope"></i> Send via Email Client
            </a>
            <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn" style="padding: 8px 18px; font-size: 0.88rem; background: #16A34A; color: white;">
              <i class="fa-brands fa-whatsapp"></i> Send via WhatsApp
            </a>
          </div>
        `;
      }
    });
  }

  // 5. Pre-select Service from URL Query Parameter (e.g. contact.html?service=CNC+Milling)
  const urlParams = new URLSearchParams(window.location.search);
  const serviceParam = urlParams.get('service');
  if (serviceParam) {
    const serviceSelect = document.getElementById('serviceRequired');
    if (serviceSelect) {
      for (let i = 0; i < serviceSelect.options.length; i++) {
        if (
          serviceSelect.options[i].value.toLowerCase() === serviceParam.toLowerCase() ||
          serviceSelect.options[i].value.toLowerCase().includes(serviceParam.toLowerCase())
        ) {
          serviceSelect.selectedIndex = i;
          break;
        }
      }
    }
  }

});
