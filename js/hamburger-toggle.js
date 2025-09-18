document.addEventListener("DOMContentLoaded", () => {
    const menu = document.getElementById("mobile-menu");
    const hamburger = document.getElementById("hamburger-menu");
    const closeBtn = document.getElementById("close-btn");
    const anchorLinks = menu.querySelectorAll("a[href*='#']");

    function toggleMenu() {
        menu.setAttribute('aria-hidden',
                          menu.getAttribute('aria-hidden') === 'true' ? 'false' : 'true');
        menu.classList.toggle("open");
        document.body.classList.toggle("no-scroll");
    }

    hamburger.addEventListener("click", (e) => {
        e.preventDefault();
        toggleMenu();

    });

    closeBtn.addEventListener("click", () => {
                toggleMenu();
    });

    // Close menu when clicking on a same-page link within the menu
    anchorLinks.forEach(link => {
        link.addEventListener("click", () => {
            toggleMenu();
        });
    });
});
