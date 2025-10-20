document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.querySelector('.nav-toggle');
    const navList = document.querySelector('.nav-list');

	// 檢查 DOM 元素是否存在，避免在找不到元素時發生錯誤
	if (!toggle || !navList) return;

    toggle.addEventListener('click', function () {
        navList.classList.toggle('open');
    });

	// 在視窗尺寸改變到桌機時，自動關閉手機選單以避免遺留狀態
	window.addEventListener('resize', function () {
		if (window.innerWidth > 800) {
			if (navList.classList.contains('open')) {
				navList.classList.remove('open');
			}
			if (toggle.classList.contains('open')) {
				toggle.classList.remove('open');
				toggle.setAttribute('aria-expanded', 'false');
			}
		}
	});
});