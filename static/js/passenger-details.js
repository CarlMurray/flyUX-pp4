// SELECT SUBMIT BTN
let submitBtn = document.querySelector('#submit')
// SELECT FORM
let form = document.querySelector('form')
// SELECT BOTH EMAIL FIELDS
let emails = document.querySelectorAll('[type="email"]')

// VALIDATE FORM ON CLICK
const validateForm = function(e) {
    // PREVENT SUBMIT
    e.preventDefault()
    // REPORT ERRORS TO USER
    form.reportValidity()
    // CHECK IF EMAILS MATCH
    if (emails[0].value != emails[1].value) {
        emails[1].setCustomValidity("Email address doesn't match")
        form.reportValidity()
    }
    // IF EMAILS MATCH SUBMIT FORM
    else {
        emails[1].setCustomValidity('')
        form.requestSubmit()
    }
}

// ADD CLICK LISTENER TO SUBMIT BTN
submitBtn.addEventListener('click', validateForm)