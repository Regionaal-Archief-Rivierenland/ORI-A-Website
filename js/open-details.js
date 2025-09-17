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

window.addEventListener('DOMContentLoaded', openDetailsForHash);
window.addEventListener('hashchange', openDetailsForHash);
