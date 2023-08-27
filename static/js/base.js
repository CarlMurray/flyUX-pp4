/*
Base script for all pages.
Controls the hamburger menu.
Controls django messages styles.
*/

/*
Hambuger menu functionality.
On click, the hamburger menu expands to show the navigation links.
*/
let hamburgerMenu = document.querySelector("#hamburger-menu");
let hamburgerMenuExpanded = document.querySelector("#hamburger-menu-expanded");
let isOpen = false;
hamburgerMenu.addEventListener("click", function () {
  isOpen = !isOpen;
  if (isOpen === true) {
    hamburgerMenuExpanded.classList.toggle("max-h-[999px]");
    hamburgerMenuExpanded.classList.toggle("p-12");
  } else {
    hamburgerMenuExpanded.classList.toggle("max-h-[999px]");
    hamburgerMenuExpanded.classList.toggle("p-12");
  }
});

/*
Function to hide django messages after 5 seconds.
*/
const hideMessage = (message) => {
  // TRANSLATE MESSAGE DOWN TO SCREEN
  message.classList.remove("-translate-y-[1000px]");
  // FADE OUT MESSAGE AFTER 5 SECONDS
  setTimeout(function () {
    message.classList.add("opacity-0");
    // HIDE MESSAGE AFTER 6 SECONDS
    setTimeout(function () {
      message.parentElement.classList.add("hidden");
    }, 1000);
  }, 5000);
};

/*
When the page loads, the message is hidden after 5 seconds.
*/
window.onload = (e) => {
  let infoMessage = document.querySelector("#message");
  // IF MESSAGE EXISTS, CALL hideMessage FUNCTION
  if (infoMessage) {
    hideMessage(infoMessage);
  }
};
