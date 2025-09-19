// open <details> corresponding to anchorlink

function openDetailsForHash() {
    // remove '#'
    const id = location.hash.slice(1);
    if (!id) return;

    const el = document.getElementById(id);
    if (!el || el.tagName.toLowerCase() !== 'details') return;

    // set to open 
    el.open = true;
}

// run by default (i.e. when DOM is loaded)
openDetailsForHash();
window.addEventListener('hashchange', openDetailsForHash);
const html = document.documentElement;
const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
    html.setAttribute("data-theme", savedTheme);
}
const themeToggle = document.getElementById("theme-toggle");

themeToggle.addEventListener("click", (event) => {
    event.preventDefault(); // Prevents page reload if it's a link
    const currentTheme = html.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";

    html.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
});
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
