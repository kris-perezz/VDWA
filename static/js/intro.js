document.addEventListener("DOMContentLoaded", function () {
    // Add class to trigger pop-up effect
    document.body.classList.add("loaded");

    // Click event to go to the main page
    document.getElementById("popup-image").addEventListener("click", function () {
        window.location.href = "/index";
    });
});
