document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll(".message");
    const nextBtn = document.getElementById("next-btn");
    let index = 0;

    nextBtn.addEventListener("click", function () {
        messages[index].classList.remove("active");
        index++;

        if (index < messages.length) {
            messages[index].classList.add("active");
        } else {
            window.location.href = "/main";
        }
    });
});
