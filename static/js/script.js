document.addEventListener("DOMContentLoaded", function () {
    const dialogueBox = document.getElementById("dialogue-box");
    const nextBtn = document.getElementById("next-btn");
    const choiceContainer = document.getElementById("choice-container");

    // Read image paths from data attribute
    const dialogues = JSON.parse(dialogueBox.getAttribute("data-dialogues"));
    
    let dialogueIndex = 0;

    // Handle dialogue progression
    nextBtn.addEventListener("click", function () {
        if (dialogueIndex < dialogues.length - 1) {
            dialogueIndex++;
            dialogueBox.src = dialogues[dialogueIndex];
        } else {
            // Show choices and hide arrow
            window.location.href = "/final";
        }
    });

});
