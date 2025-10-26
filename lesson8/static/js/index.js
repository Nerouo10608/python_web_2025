<<<<<<< HEAD
console.log("Hello! index!")
=======
console.log("Hello! index.jsw")
document.addEventListener('DOMContentLoaded', () => {
    const nav = document.querySelector('.site-nav');
    const menu = nav?.querySelector('.menu');
    if (!nav || !menu) return;

    if (!menu.id) menu.id = 'primary-menu';

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'menu-toggle';
    btn.setAttribute('aria-controls', menu.id);
    btn.setAttribute('aria-expanded', 'false');
    btn.setAttribute('aria-label', '切換主選單');

    // 建立圖示 span
    const icon = document.createElement('span');
    icon.className = 'menu-icon';
    icon.innerHTML = '☰';
    btn.appendChild(icon);

    nav.insertBefore(btn, menu);

    const closeMenu = () => {
        nav.classList.remove('is-open');
        btn.querySelector('.menu-icon').innerHTML = '☰';
        btn.setAttribute('aria-expanded', 'false');
    };
    const openMenu = () => {
        nav.classList.add('is-open');
        btn.querySelector('.menu-icon').innerHTML = '×';
        btn.setAttribute('aria-expanded', 'true');
    };

    btn.addEventListener('click', () => {
        const expanded = btn.getAttribute('aria-expanded') === 'true';
        expanded ? closeMenu() : openMenu();
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) closeMenu();
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeMenu();
    });
});
>>>>>>> bb1d9793f1518be19249ca92557bc5c2927f5b09
