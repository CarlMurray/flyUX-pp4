// TODO: REFACTOR SCRIPT - DUPLICATE CODE
let confirmFlightsBtn = document.querySelector("#confirm-flights-button");
let selectedOutboundFlight = document.querySelector(
    '[name="selected-outbound-flight"]'
);
let selectedReturnFlight = document.querySelector(
    '[name="selected-return-flight"]'
);

const clickHandler = function (e) {
    let faresWrapper = this.parentNode.querySelector('.flight-fares-wrapper')
    // IF CONTAINER ALREADY EXPANDED:
    if (this.parentNode.getAttribute("data-expanded") === "True") {
        // HIDE FARES
        faresWrapper.classList.toggle('max-h-[100rem]');
        this.parentNode.classList.remove("rounded-b-[3rem]", "shadow-xl");
        this.parentNode.setAttribute("data-expanded", "False");
    }
    //  ELSE IF SELECTED FLIGHT NOT ALREADY EXPANDED:
    else {
        // SELECT THE FLIGHT THAT WAS PREVIOUSLY SELECTED, IF ANY
        let alreadySelected = document.querySelector('[data-expanded="True"]');
        // HIDE THE PREVIOUSLY SELECTED FLIGHT
        if (alreadySelected) {
            alreadySelected.setAttribute("data-expanded", "False");
            alreadySelected.classList.remove("rounded-b-[3rem]", "shadow-xl");
            let faresWrapperSelected = alreadySelected.querySelector('.flight-fares-wrapper')
            faresWrapperSelected.classList.toggle('max-h-[100rem]')
        }
        // SHOW THE CURRENTLY SELECTED FLIGHT
        this.parentNode.setAttribute("data-expanded", "True");
        this.parentNode.classList.toggle("rounded-b-[3rem]");
        this.parentNode.classList.toggle("shadow-xl");
        faresWrapper.classList.toggle('max-h-[100rem]')
    }
}

// TO TOGGLE FARE SELECTION ON CLICK
const toggleFlightFares = function () {
    let flightCardContainers = document.querySelectorAll(
        ".flight-details-card"
    );
    flightCardContainers.forEach((card) => {
        card.addEventListener("click", clickHandler);
    });
};

// CHECKS FOR HTMX REQUEST AND REATTACHES EVENT LISTENERS TO NEW DOM ELEMENTS
document.addEventListener("htmx:afterSettle", function (e) {
    console.log('settled')
    // toggleFlightFares();
    main();
    // reattachOutboundListeners()
    // reattachReturnListeners()
    // console.log(e.target.getAttribute("data-leg"));
    // let leg = e.target.getAttribute("data-leg");
    // if (leg === "outbound") {
    //     reattachOutboundListeners();
    // } else {
    //     reattachReturnListeners();
    // }
});

// --------
// OUTBOUND
// --------

// DEFINE CLASS FOR SELECTED FLIGHT
// let selectedClass = "border-green-500";

const reattachOutboundListeners = function () {
    // SELECT OUTBOUND FLIGHTS
    outboundFlights = document.querySelectorAll('[data-flight-leg="outbound"]');

    // ADD CLICK LISTENER TO EACH OUTBOUND FLIGHT
    outboundFlights.forEach(function (item) {
        item.addEventListener("click", function () {
            // ON CLICK, ITERATE THROUGH ALL OUTBOUND FLIGHTS AND SET FALSE
            // TO ENSURE ONLY ONE FLIGHT CAN BE SELECTED
            outboundFlights.forEach(function (each) {
                each.setAttribute("data-selected-outbound", "False");
                // each.classList.remove(selectedClass);
            });
            // SET SELECTED FLIGHT TO TRUE
            this.setAttribute("data-selected-outbound", "True");
            // this.classList.add(selectedClass);
            selectedOutboundFlight.setAttribute("value", this.id);
        });
    });
};

// --------
// RETURN
// --------

const reattachReturnListeners = function () {
    // SELECT RETURN FLIGHTS
    returnFlights = document.querySelectorAll('[data-flight-leg="return"]');

    // ADD CLICK LISTENER TO EACH RETURN FLIGHT
    returnFlights.forEach(function (item) {
        item.addEventListener("click", function () {
            // ON CLICK, ITERATE THROUGH ALL RETURN FLIGHTS AND SET FALSE
            // TO ENSURE ONLY ONE FLIGHT CAN BE SELECTED
            returnFlights.forEach(function (each) {
                each.setAttribute("data-selected-return", "False");
                // each.classList.remove(selectedClass);
            });
            // SET SELECTED FLIGHT TO TRUE
            this.setAttribute("data-selected-return", "True");
            // this.classList.add(selectedClass);
            selectedReturnFlight.setAttribute("value", this.id);
        });
    });
};
// -------
// SUBMIT
// -------
confirmFlightsBtn.addEventListener("click", function () {
    let outboundFlight = selectedOutboundFlight.getAttribute("value");
    let returnFlight = selectedReturnFlight.getAttribute("value");
    console.log(outboundFlight, returnFlight);
    sessionStorage.setItem("outbound_flight", outboundFlight);
    sessionStorage.setItem("return_flight", returnFlight);
});
// ATTACHES EVENT LISTNERS ON INITIAL LOAD
const main = function () {
    reattachOutboundListeners();
    reattachReturnListeners();
    toggleFlightFares();
};

window.addEventListener("load", main);
