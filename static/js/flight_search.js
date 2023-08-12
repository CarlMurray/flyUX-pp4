let airportOrigin = document.querySelector("#origin");
let airportDestination = document.querySelector("#destination");
let airportsListOrigin = document.querySelector("#airports-list-origin");
let airportsListDestination = document.querySelector("#airports-list-destination");
let airportListItems = document.querySelectorAll('.airport-list-item')

// REQUIRED FOR FORM VALIDATION - DISABLES READONLY
let date_picker_from = flatpickr("#flatpickr-date-outbound", {allowInput:true});
let date_picker_to = flatpickr("#flatpickr-date-return", {allowInput:true});

// DISABLE USER KEY INPUT FOR FORM FIELDS
let dateFromInput = document.querySelector('#flatpickr-date-outbound')
let dateToInput = document.querySelector('#flatpickr-date-return')
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
      dateToInput.setAttribute('disabled' , true)
      dateToInput.classList.add('hidden')
      dateFromInput.classList.add('md:col-span-2', 'col-span-4')
    }
    else {
      dateToInput.setAttribute('disabled' , false)
      dateToInput.classList.remove('hidden')
      dateFromInput.classList.remove('md:col-span-2', 'col-span-4')
    }
  })
});
submit.addEventListener('click', validateForm)