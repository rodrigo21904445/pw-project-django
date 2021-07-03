function showPage(page) {
    console.log(`${page}`);
    fetch(`${page}.html`)
    .then(response => response.text())
    .then(text => document.querySelector('#main-content').innerHTML = text);
    console.log("hello there2");
}

document.querySelectorAll('nav').forEach(a => {
    console.log("hello there1");
    a.onclick = () => {
        showPage(this.dataset);
        console.log("hello there3");
    };
});


document.addEventListener('DOMContentLoaded', () => {

    

    document.querySelectorAll('nav').forEach(a => {
        console.log("hello there1");
        a.onclick = () => {
            showPage(this.dataset);
            console.log("hello there3");
        };
    });
    
});
