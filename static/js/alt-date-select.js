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

let selectedFare;
let selectedFareLeg;

// HANDLE FARE SELECTION
const selectFare = function (e) {
    selectedFare = this.getAttribute('data-fare-type')
    selectedFareLeg = this.getAttribute('data-leg')
    console.log(selectedFare, selectedFareLeg)
    // STORE SELECTED FARE IN SESSION STORAGE
    sessionStorage.setItem(selectedFareLeg+'_fare', selectedFare)
    addSelectedFlight(this, selectedFare)
    // GET TOP LEVEL PARENT ELEMENT
    // let parent = getParent(this, selectedFareLeg)
    // // HIDES FLIGHTS NOT SELECTED
    // parent.classList.add('hidden')
    // // CREATE NEW ELEMENT FOR SELECTED FLIGHT
    // card = createSelectedFlightCard()
    // // INSERT NEW ELEMENT FOR SELECTED FLIGHT
    // parent.insertAdjacentElement('beforebegin', card)

}

const addSelectedFlight = function(selected) {
    let topParent = getParent(selected, 'id', `${selectedFareLeg}-flights`)
    let flightNumber = selected.getAttribute('data-flight-number')
    console.log(flightNumber)
    let selectedFlight = document.querySelector(`#${flightNumber}`)
    let selectedFare = selected.getAttribute('data-fare-type')
    console.log(selectedFare)
    console.log(selectedFlight)
    // HIDES FLIGHTS NOT SELECTED
    topParent.classList.add('hidden')
    selectedFlight.nextElementSibling.classList.toggle("max-h-[100rem]")
    selectedFlight.parentElement.classList.toggle("rounded-b-[3rem]")
    selectedFlight.parentElement.classList.toggle("shadow-xl")
    selectedFlight.parentElement.setAttribute("data-expanded", "False")

    // CREATE NEW ELEMENT FOR SELECTED FLIGHT
    card = createSelectedFlightCard(selectedFlight, selectedFare)
    // INSERT NEW ELEMENT FOR SELECTED FLIGHT
    topParent.insertAdjacentElement('beforebegin', card)

    editFlightSelection()


}

// CLICK HANDLER FOR EDIT FLIGHT BTN
const editFlight = function(e) {
    console.log('EDIT!')
    console.log(this)
    let leg = this.getAttribute('data-leg')
    console.log(leg)
    let flightSearchResults = document.querySelector(`#${leg}-flights`)
    console.dir(flightSearchResults)
    flightSearchResults.classList.remove('hidden')
    let selectedFlight = document.querySelector(`#${leg}-selected`)
    console.dir(selectedFlight)
    selectedFlight.remove()

}

// FUNCTION TO EDIT FLIGHT
const editFlightSelection = function () {
    editButton = document.querySelectorAll('.flight-edit-button')
    console.dir(editButton)
    editButton.forEach(btn => {
        btn.addEventListener('click', editFlight)
    });

}

// GET TOP LEVEL PARENT ELEMENT
const getParent = function(node, attribute, value) {
        let parent = node.parentElement
        while (parent.getAttribute(attribute) !== value){
            parent = parent.parentElement
        }
        console.log(parent)
        return parent
    
}

const createSelectedFlightCard = function(flight, selectedFare) {
    origin = flight.getAttribute('data-flight-origin')
    destination = flight.getAttribute('data-flight-destination')
    depTime = flight.getAttribute('data-flight-deptime')
    arrTime = flight.getAttribute('data-flight-arrtime')
    price = flight.getAttribute(`data-price-${selectedFare}`)
    flightNumber = flight.getAttribute('id')
    fare = selectedFare
    date = flight.getAttribute('data-flight-date')
    leg = flight.getAttribute('data-flight-leg')

    card = document.createElement('div')
    card.setAttribute('id', `${leg}-selected`)
    card.innerHTML = `<div class="flex flex-col items-center justify-between w-full bg-white border-2 border-green-500 flight-details-card flex-0 drop-shadow-md h-52 sm:h-36 sm:rounded-full sm:flex-row sm:pl-8 md:pl-16 rounded-3xl overflow-clip">
    <div class="flex items-center justify-between p-4">
        <div>
            <div class="text-xs font-semibold md:text-md text-text">${origin}</div>
            <div class="text-xl font-bold md:text-4xl text-text">${depTime}</div>
        </div>
        <div class="mx-8">
            <div class="text-sm font-light text-center md:text-md text-text">[Duration]</div>
<hr class="w-[200px]">        
</div>
        <div>
            <div class="text-xs font-semibold md:text-md text-text">${destination}</div>
            <div class="text-xl font-bold md:text-4xl text-text">${arrTime}</div>
        </div>
    </div>
    <div class="pb-4 text-sm text-center sm:pb-0 sm:pr-4 text-text flex-grow">
        Flight no.
        <br class="hidden sm:block">
        ${flightNumber}
    </div>
    <div class="ml-auto mr-8 text-right">
        <p class="text-normal text-text text-lg">${fare}</p>
        <p class="text-primary text-2xl font-bold">€${price}pp</p>
        <p class="text-text font-bold text-md">${date}</p>
    </div>
    <div class="flex items-center justify-center w-full h-full text-xl font-normal bg-white text-primary sm:aspect-square sm:w-auto sm:rounded-full">
        <span class="w-0 h-4/6 border-[1px] ml-0"></span>
        <p class="w-2/3 text-center mx-auto p-2 cursor-pointer flight-edit-button" data-leg=${leg}>Edit</p>
    </div>
</div>
`
    return card
}

// ADD EVENT LISTENER TO FARE BUTTONS
const addFareButtonListeners = function () {
    let fareSelectionButtons = document.querySelectorAll('[data-fare-type]')
    fareSelectionButtons.forEach(button => {
        button.addEventListener('click', selectFare)
    });
}


// ATTACHES EVENT LISTNERS ON INITIAL LOAD
const main = function () {
    reattachOutboundListeners();
    reattachReturnListeners();
    toggleFlightFares();
    addFareButtonListeners()
};

window.addEventListener("load", main);
