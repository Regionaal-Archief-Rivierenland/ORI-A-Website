const fileMap = {
    "v1.0.0": "ORI-A (v1.0.0).xsd",
    "v0.0.14": "ORI-A.xsd",
    "pdf_diagram": "ORI-A-diagram.pdf",
    "svg_diagram": "ORI-A-diagram.svg",
    "png_logo": "logo.png",
    "svg_logo": "logo.svg",
    "ORI-A + MDTO": "ORI-A Voorbeeldbestanden.zip",
    "ORI-A + MDTO (opex)": "ORI-A Voorbeeldbestanden.zip",
};


document.querySelectorAll(".grid.download").forEach(group => {
    const select = group.querySelector("select");
    // link == download button
    const link = group.querySelector("a");
    const span = link.querySelector("span");
    const strong = link.querySelector("strong");

    // Update link/button label when selection changes
    select.addEventListener("change", () => {
        const value = select.value;
        if (!value) return;
        const label = value.split("_")[0];
        span.innerHTML = `<strong>${strong.textContent}</strong> (${label.toLowerCase()})`;
        const file = fileMap[value];
        if (!file) return;
        link.setAttribute("href", file)
    });

});
