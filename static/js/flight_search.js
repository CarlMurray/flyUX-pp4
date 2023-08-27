/*
Script for flight search form.
Checks if the return date is after the departure date.
Checks if the destination is not the same as the origin.
Controls the date picker.
Validates the form and submits the form if the form is valid.
*/

// SELECT FORM ELEMENTS
let airportOrigin = document.querySelector("#origin");
let airportDestination = document.querySelector("#destination");
let airportsListOrigin = document.querySelector("#airports-list-origin");
let airportsListDestination = document.querySelector(
  "#airports-list-destination"
);
let airportListItems = document.querySelectorAll(".airport-list-item");

// CREATES DATE OBJECTS FOR FLATPICKR ENABLED DATE RANGE
let dateToday = new Date();
let dateTomorrow = new Date();
dateTomorrow.setDate(dateToday.getDate() + 1);

// CONVERTS DATE OBJECTS TO STRINGS
let dateTodayString =
  dateToday.getFullYear() +
  "-" +
  (dateToday.getMonth() + 1) +
  "-" +
  dateToday.getDate();
let dateTomorrowString =
  dateTomorrow.getFullYear() +
  "-" +
  (dateTomorrow.getMonth() + 1) +
  "-" +
  dateTomorrow.getDate();

// ENABLES DATES FOR FLATPICKR
let enabledDatesFrom = [{ from: dateTodayString, to: "2024-07-01" }];
let enabledDatesTo = [{ from: dateTomorrowString, to: "2024-07-01" }];

// REQUIRED FOR FORM VALIDATION - DISABLES READONLY
let date_picker_from = flatpickr("#flatpickr-date-outbound", {
  allowInput: true,
  enable: enabledDatesFrom,
});
let date_picker_to = flatpickr("#flatpickr-date-return", {
  allowInput: true,
  enable: enabledDatesTo,
});

// DISABLE USER KEY INPUT FOR FORM FIELDS
let dateFromInput = document.querySelector(
  "#flatpickr-date-outbound-container"
);
let dateToInput = document.querySelector("#flatpickr-date-return-container");
let dateFromInputField = document.querySelector("#flatpickr-date-outbound");
let dateToInputField = document.querySelector("#flatpickr-date-return");
dateFromInput.onkeypress = () => false;
dateToInput.onkeypress = () => false;
airportOrigin.onkeypress = () => false;
airportDestination.onkeypress = () => false;

// SHOW AIRPORT LIST ON CLICK
document.addEventListener("click", (e) => {
  if (e.target == airportOrigin || e.target == airportDestination) {
    e.target.nextElementSibling.classList.remove("hidden");
  }
  // HIDE AIRPORT LIST ON CLICK OUTSIDE
  else if (
    (e.target != airportOrigin && e.target != airportsListOrigin) ||
    (e.target != airportDestination && e.target != airportsListDestination)
  ) {
    airportsListOrigin.classList.add("hidden");
    airportsListDestination.classList.add("hidden");
  }
});

// ADD AIRPORT TO INPUT FIELD ON CLICK
airportListItems.forEach((item) => {
  item.addEventListener("click", (e) => {
    let value = item.innerText;
    let parent = item.parentNode;
    let inputField = parent.parentNode.previousElementSibling;
    inputField.value = value;
  });
});

// FLATPICKR DATE INPUT VALIDATION
let dates = document.querySelectorAll('[data-id="datetime"]');
let submit = document.querySelector("#submit");
let form = document.querySelector("form");

// SEARCH FORM VALIDATION
const validateForm = function (e) {
  e.preventDefault();
  document.querySelectorAll("input").forEach((input) => {
    input.removeAttribute("readonly");
  });
  // CHECK IF RETURN DATE IS BEFORE DEPARTURE DATE
  if (new Date(dateFromInputField.value) >= new Date(dateToInputField.value)) {
    dateToInputField.setCustomValidity(
      "Return date must be after departure date"
    );
  } else {
    dateToInputField.setCustomValidity("");
  }

  // CHECK IF DESTINATION IS SAME AS ORIGIN
  if (airportDestination.value === airportOrigin.value) {
    airportDestination.setCustomValidity(
      "Destination cannot be same as origin"
    );
  } else {
    airportDestination.setCustomValidity("");
  }
  // CHECK IF FORM IS VALID
  form.checkValidity();
  form.reportValidity();
  form.requestSubmit();
};

// ADD GREY TEXT COLOUR TO PASSENGERS PLACEHOLDER - NOT POSSIBLE TO DO WITH HTML/CSS ONLY
let passengersInput = document.querySelector('[name="passengers"]');
passengersInput.addEventListener("click", function (e) {
  // REMOVE GRAY ON CLICK
  passengersInput.classList.remove("text-gray-400");
});

// CONTROL TRIP TYPE RADIO BUTTONS - ONE WAY OR RETURN
let tripRadioSelects = document.querySelectorAll('[type="radio"]');
tripRadioSelects.forEach((radio) => {
  radio.addEventListener("click", function (e) {
    let tripType = e.target.value;
    if (tripType === "oneway") {
      dateToInputField.setAttribute("disabled", true);
      dateToInput.classList.add("hidden");
      dateFromInput.classList.add("sm:col-span-4", "md:col-span-2");
    } else {
      dateToInputField.removeAttribute("disabled");
      dateToInput.classList.remove("hidden");
      dateFromInput.classList.remove("sm:col-span-4", "md:col-span-2");
    }
  });
});

// ADD CLICK LISTENER TO SUBMIT BTN - VALIDATE FORM
submit.addEventListener("click", validateForm);
