document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("theme-toggle");
    if (!themeToggle) return;

    const html = document.documentElement;
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        html.setAttribute("data-theme", savedTheme);
    }

    themeToggle.addEventListener("click", (event) => {
        event.preventDefault(); // Prevents page reload if it's a link
        const currentTheme = html.getAttribute("data-theme");
        const newTheme = currentTheme === "dark" ? "light" : "dark";

        html.setAttribute("data-theme", newTheme);
        localStorage.setItem("theme", newTheme);
    });
});
