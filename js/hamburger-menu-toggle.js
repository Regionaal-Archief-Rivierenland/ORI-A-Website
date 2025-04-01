document.addEventListener("DOMContentLoaded", () => {
    const menu = document.getElementById("mobile-menu");
    const hamburger = document.getElementById("hamburger-menu");
    const closeBtn = document.getElementById("close-btn");

    hamburger.addEventListener("click", (e) => {
        // don't go to the href in the <a>
        e.preventDefault();
        // menu.style.display = "flex";
        menu.classList.toggle("open");
    });

    closeBtn.addEventListener("click", () => {
        menu.classList.remove("open");
    });
});
