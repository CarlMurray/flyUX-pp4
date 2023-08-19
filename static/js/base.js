let hamburgerMenu = document.querySelector("#hamburger-menu");
let hamburgerMenuExpanded = document.querySelector("#hamburger-menu-expanded");
let hamburgerNavLinks = document.querySelector("#hamburger-nav-links");
let isOpen = false;
hamburgerMenu.addEventListener("click", function () {
  isOpen = !isOpen;
  if (isOpen === true) {
    // hamburgerMenuExpanded.classList.remove("max-h-0");
    hamburgerMenuExpanded.classList.toggle("max-h-screen");
    hamburgerMenuExpanded.classList.toggle("p-12");
    // hamburgerNavLinks.classList.toggle("hidden");
  } else {
        hamburgerMenuExpanded.classList.toggle("max-h-screen");
        hamburgerMenuExpanded.classList.toggle("p-12");
    // hamburgerNavLinks.classList.toggle("hidden");
  }
});

// let date_picker_from = flatpickr("#flatpickr-date-outbound", {});
// let date_picker_to = flatpickr("#flatpickr-date-return", {});
