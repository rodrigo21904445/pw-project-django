const navButton = document.querySelectorAll('nav > ul > li > a');

document.addEventListener('DOMContentLoaded', () => {
    navButton.onclick = () => {
        navButton.style.color = green;
    }
});