/* click effect animates for menu */
const menu = document.querySelector("#mobile-menu")
const menuLinks = document.querySelector(".navbar__menu")

menu.addEventListener("click", function() {
    menu.classList.toggle("is-active");
    menuLinks.classList.toggle("active");
});

/*Project info from hovering*/
document.addEventListener("DOMContentLoaded", function() {
    const getStartedButton = document.querySelector(".main__btn");
    const mainImage = document.getElementById("main__img");

    // Define the new image source
    const newImageSrc = "images/marioEx.png"; // Change this to the path of your new image

    // Event listener for hovering over the "Get Started" button
    getStartedButton.addEventListener("mouseenter", function() {
        // Change the image source
        mainImage.src = newImageSrc;
    });

    // Event listener for when the mouse leaves the "Get Started" button
    getStartedButton.addEventListener("mouseleave", function() {
        // Change the image source back to the original image
        mainImage.src = "images/busManSite.svg";
    });
});



/* First Program PAGE */

/* TEXT FILE */
function updateInputData() {
    const sourceMario = document.getElementById("sourceMario").value;
    const sourceEmpty = document.getElementById("sourceEmpty").value;
    const sourceTreasure = document.getElementById("sourceTreasure").value;

    // Send source text data to server for updating InputData.txt
    fetch('/updateInputData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            sourceMario,
            sourceEmpty,
            sourceTreasure
        })
    });
}

function restart() {
    // Send request to server to restart InputData.txt
    fetch('/restart');
}


