let altDates = document.querySelectorAll('.altDate')
let altDatesReturn = document.querySelectorAll('.altDateReturn')
let dateInputOutbound = document.querySelector('#alt-date-input-outbound')
let dateInputReturn = document.querySelector('#alt-date-input-return')
let form = document.querySelector('#alt-date-select-form')
console.log(dateInputOutbound)
console.log(dateInputReturn)
// ADD CLICK LISTENER TO EACH ALT DATE
altDates.forEach(function(item){
    item.addEventListener('click', function(){
    selectedDate = this.id
    // SET INPUT VALUE TO SELECTED DATE
    dateInputOutbound.setAttribute('value', selectedDate)
    // SUBMIT FORM TO LOAD NEW FLIGHTS LIST
    form.submit()
})})

// ADD CLICK LISTENER TO EACH ALT DATE
altDatesReturn.forEach(function(item){
    item.addEventListener('click', function(){
    selectedDate = this.id
    // SET INPUT VALUE TO SELECTED DATE
    dateInputReturn.setAttribute('value', selectedDate)
    // SUBMIT FORM TO LOAD NEW FLIGHTS LIST
    form.submit()
})})

// TODO: REFACTOR SCRIPT