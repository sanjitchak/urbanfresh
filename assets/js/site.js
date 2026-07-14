(() => {
  const body = document.body;
  const menu = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('[data-main-nav]');

  if (menu && nav) {
    menu.addEventListener('click', () => {
      const open = body.classList.toggle('nav-open');
      menu.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', (event) => {
      if (event.target.closest('a')) {
        body.classList.remove('nav-open');
        menu.setAttribute('aria-expanded', 'false');
      }
    });
  }

  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  const phone = '919433569217';
  const form = document.querySelector('[data-quote-form]');
  if (form) {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const data = new FormData(form);
      const status = form.querySelector('[data-form-status]');
      const required = ['name', 'phone', 'location', 'quantity'];
      const missing = required.some((key) => !String(data.get(key) || '').trim());
      if (missing) {
        status.textContent = 'Please fill in your name, phone, delivery location and approximate quantity.';
        status.className = 'form-status show error';
        return;
      }

      const lines = [
        'Hello UrbanFresh, I would like a bulk rice quote.',
        '',
        `Name / company: ${data.get('name')}`,
        `Phone: ${data.get('phone')}`,
        `Delivery location: ${data.get('location')}`,
        `Buyer type: ${data.get('buyer_type') || 'Not specified'}`,
        `Rice variety: ${data.get('variety') || 'Please advise'}`,
        `Processing: ${data.get('processing') || 'Please advise'}`,
        `Approx. quantity: ${data.get('quantity')}`,
        `Packaging: ${data.get('packaging') || 'Please advise'}`,
        `Timeline: ${data.get('timeline') || 'Not specified'}`,
        `Notes: ${data.get('message') || 'None'}`
      ];
      window.open(`https://wa.me/${phone}?text=${encodeURIComponent(lines.join('\n'))}`, '_blank', 'noopener');
    });
  }
})();
