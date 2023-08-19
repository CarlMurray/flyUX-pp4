let airportOrigin = document.querySelector("#origin");
let airportDestination = document.querySelector("#destination");
let airportsListOrigin = document.querySelector("#airports-list-origin");
let airportsListDestination = document.querySelector("#airports-list-destination");
let airportListItems = document.querySelectorAll('.airport-list-item')
let dateToday = new Date();
let dateTodayString = dateToday.getFullYear() + "-" + (dateToday.getMonth() + 1) + "-" + dateToday.getDate()
let enabledDates = [{from:dateTodayString, to:"2024-07-01"}]
// REQUIRED FOR FORM VALIDATION - DISABLES READONLY
let date_picker_from = flatpickr("#flatpickr-date-outbound", {allowInput:true, enable:enabledDates});
let date_picker_to = flatpickr("#flatpickr-date-return", {allowInput:true, enable:enabledDates});

// DISABLE USER KEY INPUT FOR FORM FIELDS
let dateFromInput = document.querySelector('#flatpickr-date-outbound-container')
let dateToInput = document.querySelector('#flatpickr-date-return-container')
let dateFromInputField = document.querySelector('#flatpickr-date-outbound')
let dateToInputField = document.querySelector('#flatpickr-date-return')
dateFromInput.onkeypress = () => false
dateToInput.onkeypress = () => false
airportOrigin.onkeypress = () => false
airportDestination.onkeypress = () => false

document.addEventListener('click', (e) => {
    if (e.target == airportOrigin || e.target == airportDestination) {
      e.target.nextElementSibling.classList.remove('hidden');
    } else if (e.target != airportOrigin && e.target != airportsListOrigin || e.target != airportDestination && e.target != airportsListDestination) {
        airportsListOrigin.classList.add('hidden');
        airportsListDestination.classList.add('hidden');
    }})
  airportListItems.forEach((item) => {
    item.addEventListener('click', (e) => {
      console.log(item.innerText);
      let value = item.innerText;
      let parent = item.parentNode
      console.log('Parent:')
      console.dir(parent)
      let inputField = parent.parentNode.previousElementSibling
      console.dir(inputField)
      inputField.value = value;
    });
  });

// FLATPICKR DATE INPUT VALIDATION
let dates = document.querySelectorAll('[data-id="datetime"]')
let submit = document.querySelector('#submit')
let form = document.querySelector('form')

// SEARCH FORM VALIDATION
const validateForm = function(e){
  e.preventDefault()
  if (new Date(dateFromInputField.value) > new Date(dateToInputField.value)){
    dateToInputField.setCustomValidity('Return date cannot be before departure date')
  }
  else {
    dateToInputField.setCustomValidity('')
  }
  if (airportDestination.value === airportOrigin.value){
    airportDestination.setCustomValidity('Destination cannot be same as origin')
  } 
  else {
    airportDestination.setCustomValidity('')
  }

  form.checkValidity()
  form.reportValidity()
  form.requestSubmit()

}

// ADD GREY TEXT COLOUR TO PASSENGERS PLACEHOLDER - NOT POSSIBLE TO DO WITH HTML/CSS ONLY
let passengersInput = document.querySelector('[name="passengers"]')
passengersInput.addEventListener('click', function(e){
  // REMOVE GRAY ON CLICK
  passengersInput.classList.remove('text-gray-400')
})

let tripRadioSelects = document.querySelectorAll('[type="radio"]')
tripRadioSelects.forEach(radio => {
  radio.addEventListener('click', function(e){
    let tripType = e.target.value
    if (tripType === 'oneway'){
      dateToInputField.setAttribute('disabled' , true)
      dateToInput.classList.add('hidden')
      dateFromInput.classList.add('sm:col-span-4','md:col-span-2')
      console.log(tripType)
    }
    else {
      dateToInputField.removeAttribute('disabled')
      dateToInput.classList.remove('hidden')
      dateFromInput.classList.remove('sm:col-span-4','md:col-span-2')
      console.log(tripType)
    }
  })
});
submit.addEventListener('click', validateForm)