let hamburgerMenu = document.querySelector("#hamburger-menu");
let hamburgerMenuExpanded = document.querySelector("#hamburger-menu-expanded");
let isOpen = false;
hamburgerMenu.addEventListener("click", function () {
  isOpen = !isOpen;
  if (isOpen === true) {
    hamburgerMenuExpanded.classList.remove("hidden");
  } else hamburgerMenuExpanded.classList.add("hidden");
});

// let date_picker_from = flatpickr("#flatpickr-date-outbound", {});
// let date_picker_to = flatpickr("#flatpickr-date-return", {});
