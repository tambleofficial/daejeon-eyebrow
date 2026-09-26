const menu = document.querySelector('.menu-button');
const nav = document.querySelector('.site-nav');
if (menu && nav) {
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
  });
}
const carousel = document.querySelector('.carousel');
if (carousel) {
  const step = () => (carousel.querySelector('.card')?.getBoundingClientRect().width || 320) + 18;
  document.querySelector('.prev')?.addEventListener('click', () => carousel.scrollBy({left:-step(),behavior:'smooth'}));
  document.querySelector('.next')?.addEventListener('click', () => carousel.scrollBy({left:step(),behavior:'smooth'}));
}
