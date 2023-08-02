// TODO: REFACTOR SCRIPT - DUPLICATE CODE
let confirmFlightsBtn = document.querySelector("#confirm-flights-button");
let selectedOutboundFlight = document.querySelector(
    '[name="selected-outbound-flight"]'
);
let selectedReturnFlight = document.querySelector(
    '[name="selected-return-flight"]'
);

// TO TOGGLE FARE SELECTION ON CLICK
const toggleFlightFares = function () {
    let flightCardContainers = document.querySelectorAll(
        ".flight-card-container"
    );
    flightCardContainers.forEach((card) => {
        card.addEventListener("click", function () {
            // IF CONTAINER ALREADY EXPANDED:
            if (this.getAttribute("data-expanded") === "True") {
                let flightFaresContainer = this.querySelector(".flight-fares");
                console.log(flightFaresContainer);
                // HIDE FARES
                flightFaresContainer.classList.toggle("hidden");
                this.classList.remove("h-[40rem]", "rounded-b-[1rem]");
                this.setAttribute("data-expanded", "False");
            }
            //  ELSE IF SELECTED FLIGHT NOT ALREADY EXPANDED:
            else {
                // SELECT THE FLIGHT THAT WAS PREVIOUSLY SELECTED, IF ANY
                let alreadySelected = document.querySelector('[data-expanded="True"]');
                // HIDE THE PREVIOUSLY SELECTED FLIGHT
                if (alreadySelected) {
                    alreadySelected.setAttribute("data-expanded", "False");
                    alreadySelected.classList.remove("h-[40rem]", "rounded-b-[1rem]");
                    alreadySelected.childNodes[3].classList.toggle("hidden");
                }
                // SHOW THE CURRENTLY SELECTED FLIGHT
                this.setAttribute("data-expanded", "True");
                console.log(this.getAttribute("data-expanded"));
                this.classList.toggle("h-[40rem]");
                this.classList.toggle("rounded-b-[1rem]");
                console.dir(this.childNodes[3]);
                this.childNodes[3].classList.toggle("hidden");
            }
        });
    });
};

// CHECKS FOR HTMX REQUEST AND REATTACHES EVENT LISTENERS TO NEW DOM ELEMENTS
document.addEventListener("htmx:afterSettle", function (e) {
    toggleFlightFares();
    console.log(e.target.getAttribute("data-leg"));
    let leg = e.target.getAttribute("data-leg");
    if (leg === "outbound") {
        reattachOutboundListeners();
    } else {
        reattachReturnListeners();
    }
});

// --------
// OUTBOUND
// --------

// DEFINE CLASS FOR SELECTED FLIGHT
let selectedClass = "border-green-500";

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
                each.classList.remove(selectedClass);
            });
            // SET SELECTED FLIGHT TO TRUE
            this.setAttribute("data-selected-outbound", "True");
            this.classList.add(selectedClass);
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
                each.classList.remove(selectedClass);
            });
            // SET SELECTED FLIGHT TO TRUE
            this.setAttribute("data-selected-return", "True");
            this.classList.add(selectedClass);
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
