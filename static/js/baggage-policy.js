let modal = document.querySelector("#baggage-policy-modal");
/*
Adds click listeners to all buttons with data-id="baggage-policy"
Shows modal on click
*/
function addEventListeners(btn) {
  btn.addEventListener("click", () => {
    modal.showModal();
});
}

// Hide modal on click outside or close button
document.addEventListener('click', hideModal)
function hideModal(e) {
    if (e.target === document.querySelector('#baggage-policy-modal') || e.target === document.querySelector('#modal-close-btn')) {
        modal.close();
    }
}

/*
Attaches event listeners to all buttons with data-id="baggage-policy"
when htmx request is complete and settles i.e. when new date is selected
*/
function attachEventListners() {
  let showBaggagePolicyBtn = document.querySelectorAll(
    '[data-id="baggage-policy"]'
  );
  showBaggagePolicyBtn.forEach(addEventListeners);
}

// Attach event listeners on page load and after htmx request settles
window.addEventListener("load", attachEventListners);
document.addEventListener("htmx:afterSettle", attachEventListners);
