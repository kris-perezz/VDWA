document.addEventListener("DOMContentLoaded", function () {
    const noBtn = document.getElementById("no-btn");

    noBtn.addEventListener("mouseover", function () {
        const randomX = Math.floor(Math.random() * (window.innerWidth - 200));
        const randomY = Math.floor(Math.random() * (window.innerHeight - 100));
        noBtn.style.position = "absolute";
        noBtn.style.left = `${randomX}px`;
        noBtn.style.top = `${randomY}px`;
    });
});
