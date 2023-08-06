# flyUX-pp4

# Project Background

- This project represents an opportunity to showcase my skills in both UX design and web development, bridging the gap between form and function. 
- This Django web development project is a continuation of a UX Design project I completed during my Diploma with the UX Design Institute which goes through the full UX process from research all the way to prototyping and handover.
- The end result was a user-friendly flight booking flow which was informed by user research and prototyped to a medium fidelity in Figma.
- Revisiting the project a year later, I am now using it as a foundation to build upon and bring it from Figma prototype, to a fully functioning Django-based web application, combining my passions for user-centric design and web development to build a holistic solution.


# Bugs

- Couldn't animate fares card transition. Tried animating from hidden, height=0 etc. Solution: Remove 'hidden' class and set overflow:hidden with height=0. Transition height above max needed.

- Alt date selector bug - cards not expanding. Event listener was being added twice therefore when clicked the styles were toggled repeatedly meaning nothing was happening. Fixed by creating seperate click handler function so it doesn't get added repeatedly. Used dev tools to see what event listeners were added to diagnose problem. Ref: https://stackoverflow.com/questions/41720943/rebind-javascript-events-and-addeventlistener-fires-twice

Before:
```javascript
// TO TOGGLE FARE SELECTION ON CLICK
const toggleFlightFares = function () {
    let flightCardContainers = document.querySelectorAll(
        ".flight-card-container"
    );
    flightCardContainers.forEach((card) => {
        card.addEventListener("click", function () {
            let faresWrapper = this.querySelector('.flight-fares-wrapper')
            // IF CONTAINER ALREADY EXPANDED:
            if (this.getAttribute("data-expanded") === "True") {
                // HIDE FARES
                faresWrapper.classList.toggle('max-h-[50rem]');
                this.classList.remove("rounded-b-[3rem]", "shadow-xl");
                this.setAttribute("data-expanded", "False");
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
                    faresWrapperSelected.classList.toggle('max-h-[50rem]')
                }
                // SHOW THE CURRENTLY SELECTED FLIGHT
                this.setAttribute("data-expanded", "True");
                this.classList.toggle("rounded-b-[3rem]");
                this.classList.toggle("shadow-xl");
                faresWrapper.classList.toggle('max-h-[50rem]')
            }
        });
    });
};
```

After:
```javascript
const clickHandler = function (e) {
    let faresWrapper = this.querySelector('.flight-fares-wrapper')
    // IF CONTAINER ALREADY EXPANDED:
    if (this.getAttribute("data-expanded") === "True") {
        // HIDE FARES
        faresWrapper.classList.toggle('max-h-[50rem]');
        this.classList.remove("rounded-b-[3rem]", "shadow-xl");
        this.setAttribute("data-expanded", "False");
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
            faresWrapperSelected.classList.toggle('max-h-[50rem]')
        }
        // SHOW THE CURRENTLY SELECTED FLIGHT
        this.setAttribute("data-expanded", "True");
        this.classList.toggle("rounded-b-[3rem]");
        this.classList.toggle("shadow-xl");
        faresWrapper.classList.toggle('max-h-[50rem]')
    }
}

// TO TOGGLE FARE SELECTION ON CLICK
const toggleFlightFares = function () {
    let flightCardContainers = document.querySelectorAll(
        ".flight-card-container"
    );
    flightCardContainers.forEach((card) => {
        card.addEventListener("click", clickHandler);
    });
};
```

Bug: Could not load Booking model in Admin. Due to 90k rows in DB. Added ModelAdmin config to fix. Reference: https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields