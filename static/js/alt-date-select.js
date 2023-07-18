// TODO: REFACTOR SCRIPT - DUPLICATE CODE
let altDates = document.querySelectorAll('.altDate')
let altDatesReturn = document.querySelectorAll('.altDateReturn')
let dateInputOutbound = document.querySelector('#alt-date-input-outbound')
let dateInputReturn = document.querySelector('#alt-date-input-return')
let form = document.querySelector('#alt-date-select-form')
let confirmFlightsBtn = document.querySelector('#confirm-flights-button')
let selectedFlightsForm = document.querySelector('#selected-flights')
let selectedOutboundFlight = document.querySelector('[name="selected-outbound-flight"]')
let selectedReturnFlight = document.querySelector('[name="selected-return-flight"]')


// --------
// OUTBOUND
// --------

// ADD CLICK LISTENER TO EACH ALT DATE
altDates.forEach(function(item){
    item.addEventListener('click', function(){
    selectedDate = this.id
    // SET INPUT VALUE TO SELECTED DATE
    dateInputOutbound.setAttribute('value', selectedDate)
    // SUBMIT FORM TO LOAD NEW FLIGHTS LIST
    form.submit()
})})

// DEFINE CLASS FOR SELECTED FLIGHT
let selectedClass = 'border-green-500'

// SELECT OUTBOUND FLIGHTS
outboundFlights = document.querySelectorAll('[data-flight-leg="outbound"]')

// ADD CLICK LISTENER TO EACH OUTBOUND FLIGHT
outboundFlights.forEach(function(item){

    item.addEventListener('click', function(){
        // ON CLICK, ITERATE THROUGH ALL OUTBOUND FLIGHTS AND SET FALSE
        // TO ENSURE ONLY ONE FLIGHT CAN BE SELECTED
        outboundFlights.forEach(function(each){
            each.setAttribute('data-selected-outbound', 'False')
            each.classList.remove(selectedClass)

        })
        // SET SELECTED FLIGHT TO TRUE
        this.setAttribute('data-selected-outbound', 'True')
        this.classList.add(selectedClass)
        selectedOutboundFlight.setAttribute('value', this.id)
    })
}) 


// --------
// RETURN
// --------

// ADD CLICK LISTENER TO EACH ALT DATE
altDatesReturn.forEach(function(item){
    item.addEventListener('click', function(){
    selectedDate = this.id
    // SET INPUT VALUE TO SELECTED DATE
    dateInputReturn.setAttribute('value', selectedDate)
    // SUBMIT FORM TO LOAD NEW FLIGHTS LIST
    form.submit()
})})


// SELECT RETURN FLIGHTS
returnFlights = document.querySelectorAll('[data-flight-leg="return"]')

// ADD CLICK LISTENER TO EACH RETURN FLIGHT
returnFlights.forEach(function(item){

    item.addEventListener('click', function(){
        // ON CLICK, ITERATE THROUGH ALL RETURN FLIGHTS AND SET FALSE
        // TO ENSURE ONLY ONE FLIGHT CAN BE SELECTED
        returnFlights.forEach(function(each){
            each.setAttribute('data-selected-returrn', 'False')
            each.classList.remove(selectedClass)

        })
        // SET SELECTED FLIGHT TO TRUE
        this.setAttribute('data-selected-return', 'True')
        this.classList.add(selectedClass)
        selectedReturnFlight.setAttribute('value', this.id)

    })
}) 

// -------
// SUBMIT
// -------
confirmFlightsBtn.addEventListener('click', function(){
    let outboundFlight = selectedOutboundFlight.getAttribute('value')
    let returnFlight = selectedReturnFlight.getAttribute('value')
    console.log(outboundFlight, returnFlight)
    sessionStorage.setItem('outbound_flight', outboundFlight)
    sessionStorage.setItem('return_flight', returnFlight)
})