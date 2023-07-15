let altDates = document.querySelectorAll('.altDate')
let dateInput = document.querySelector('#alt-date-input')
let form = document.querySelector('#alt-date-select-form')

// ADD CLICK LISTENER TO EACH ALT DATE
altDates.forEach(function(item){
    item.addEventListener('click', function(){
    selectedDate = this.id
    // SET INPUT VALUE TO SELECTED DATE
    dateInput.setAttribute('value', selectedDate)
    // SUBMIT FORM TO LOAD NEW FLIGHTS LIST
    form.submit()
})})