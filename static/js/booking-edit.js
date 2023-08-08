let container = document.querySelector('#container')
const confirmDelete = (evt) => {
    console.log(evt)
    // PREVENT DEFAULT HTMX CONFIRMATION AND REQUEST
    evt.preventDefault()
    // CREATE POPUP CONFIRMATION DIALOG
    let dialog = document.createElement('dialog')
    dialog.classList.add('w-5/6', 'md:w-2/3', 'absolute', 'top-1/2', '-translate-y-1/2')
    dialog.innerHTML = 
    "<div class='flex flex-col gap-4 justify-center p-6 w-full bg-white rounded-lg shadow-lg border-primary border-2 '>\
    <p class='text-primary font-bold text-2xl text-center'>Cancel Booking</p>\
    <p class='text-center font-bold'>Are you sure you want to cancel this booking? You cannot undo this action.</p>\
    <p class='text-center'>Your card will be refunded within 7 days.</p>\
    <div class='flex justify-center gap-2 mt-2'>\
    <button id='no' class='dialog-btn w-auto px-4 py-2 border-primary border-[1px] bg-white text-text rounded-full'>No, go back</button>\
    <button id='yes' class='dialog-btn w-auto px-4 py-2 border-primary border-2 bg-primary text-white font-bold rounded-full'>Yes, cancel</button>\
    </div>\
    </div>"
    container.append(dialog)
    // SHOW DIALOG 
    dialog.show()
    // SELECT DIALOG BTNS
    let buttons = document.querySelectorAll('.dialog-btn')
    // ADD CLICK LISTENER
    buttons.forEach((button) => {
        button.addEventListener('click', function(e){
            handleClick(e, evt, dialog)
        })
    })
}

const handleClick = (e, evt, dialog) => {
    if (e.target.getAttribute('id') === 'yes'){
        // SUBMIT HTMX DELETE REQUEST
        evt.detail.issueRequest()
    } 
    else if (e.target.getAttribute('id') === 'no') {
        // HIDE DIALOG
        dialog.open = false
    }
}
let cancelBtn = document.querySelector('#cancel-booking')
document.addEventListener('htmx:confirm', function(e){
    if (e.detail.elt === cancelBtn){
        confirmDelete(e)
        console.log('WOWWOWOWO')
    }
})
