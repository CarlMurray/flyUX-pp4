let container = document.querySelector("#container");

/*
Shows a dialog confirmation popup when the user clicks the cancel booking button.
The dialog contains a message asking the user to confirm the cancellation.
If the user clicks the yes button, the htmx delete request is submitted.
If the user clicks the no button, the dialog is hidden.
*/

function confirmDelete(evt) {
  // PREVENT DEFAULT HTMX CONFIRMATION AND REQUEST
  evt.preventDefault();
  // CREATE POPUP CONFIRMATION DIALOG
  let dialog = document.createElement("dialog");
  // ADD CLASSES
  dialog.classList.add(
    "w-5/6",
    "md:w-2/3",
    "absolute",
    "top-1/2",
    "-translate-y-1/2"
  );
  // ADD DIALOG CONTENT
  dialog.innerHTML = `<div class='flex flex-col gap-4 justify-center p-6 w-full bg-white rounded-lg shadow-lg border-primary border-2 '>
    <p class='text-primary font-bold text-2xl text-center'>Cancel Booking</p>
    <p class='text-center font-bold'>Are you sure you want to cancel this booking? You cannot undo this action.</p>
    <p class='text-center'>Your card will be refunded within 7 days.</p>
    <div class='flex justify-center gap-2 mt-2'>
    <button id='no' class='dialog-btn w-auto px-4 py-2 border-primary border-[1px] bg-white text-text rounded-full transition-all hover:bg-primary hover:text-white duration-300'>No, go back</button>
    <button id='yes' class='dialog-btn w-auto px-4 py-2 border-primary border-2 bg-primary text-white font-bold rounded-full transition-all duration-300 hover:bg-[#FB257F]'>Yes, cancel</button>
    </div>
    </div>`;
  // APPEND DIALOG TO CONTAINER
  container.append(dialog);
  // SHOW DIALOG
  dialog.show();
  // SELECT DIALOG BTNS
  let buttons = document.querySelectorAll(".dialog-btn");
  // ADD CLICK LISTENER
  buttons.forEach((button) => {
    button.addEventListener("click", function (e) {
      handleClick(e, evt, dialog);
    });
  });
}

/*
Handles the click event on the dialog buttons.
If the user clicks the yes button, the htmx delete request is submitted.
If the user clicks the no button, the dialog is hidden.
*/
function handleClick(e, evt, dialog) {
  if (e.target.getAttribute("id") === "yes") {
    // SUBMIT HTMX DELETE REQUEST
    evt.detail.issueRequest();
  } else if (e.target.getAttribute("id") === "no") {
    // HIDE DIALOG
    dialog.open = false;
  }
}

/*
Calls the confirmDelete function when the user clicks the cancel booking booking button.
*/
let cancelBtn = document.querySelector("#cancel-booking");
document.addEventListener("htmx:confirm", function (e) {
  if (e.detail.elt === cancelBtn) {
    confirmDelete(e);
  }
});

/*
Checks if the user has entered a valid name.
If the user has not entered a valid name, the form is invalid and the user is shown an error message.
If the user has entered a valid name, the form is submitted.
*/
document.addEventListener("htmx:validation:validate", checkFailedValidation);
function checkFailedValidation(evt) {
  evt.detail.elt.setCustomValidity("");
  document.addEventListener("htmx:validation:failed", (evt) => {
    let form = document.querySelector("form");
    evt.detail.elt.setCustomValidity(
      "Name must contain at least 1 character and can't start with a space"
    );
    form.reportValidity();
  });
}
