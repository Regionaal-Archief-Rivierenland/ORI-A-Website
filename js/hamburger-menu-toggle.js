document.addEventListener("DOMContentLoaded", () => {
    const menu = document.getElementById("mobile-menu");
    const hamburger = document.getElementById("hamburger-menu");
    const closeBtn = document.getElementById("close-btn");
    const anchorLinks = menu.querySelectorAll("a[href*='#']");

    function toggleMenu() {
        menu.classList.toggle("open");
        document.body.classList.toggle("no-scroll");
    }

    hamburger.addEventListener("click", (e) => {
        // don't go to the href in the <a>
        e.preventDefault();
        toggleMenu();

    });

    closeBtn.addEventListener("click", () => {
                toggleMenu();
    });

    // Close menu when clicking an anchor link
    anchorLinks.forEach(link => {
        link.addEventListener("click", () => {
            toggleMenu();
        });
    });
});
