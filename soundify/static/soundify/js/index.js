function showPage(section) {
    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text => document.querySelector('#main-content').innerHTML = text);
}

document.addEventListener('DOMContentLoaded', () => {    
    document.querySelectorAll('nav').forEach(a => {
        a.onclick = () => {
            showPage(this.dataset.section);
        };
    });
});
