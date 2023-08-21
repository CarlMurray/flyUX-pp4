/*
Script for checkout.html.
This script is used to validate the card details entered by the user.
The script uses the payform library to validate the card details.
The script is used to validate the card number, expiry date and cvc.
If the card details are invalid, the user is prompted to enter the correct details.
*/

let cardName = document.querySelector("#card-name");
let cardNumber = document.querySelector("#card-number");
let cardCvc = document.querySelector("#card-cvc");
let cardExpiry = document.querySelector("#card-expiry");
let button = document.querySelector("button");

// DEFINE PAYFORM FIELDS
payform.cardNumberInput(cardNumber);
payform.expiryInput(cardExpiry);
payform.cvcInput(cardCvc);

// VALIDATE CARD DETAILS ON SUBMIT
button.addEventListener("click", function () {
  if (!payform.validateCardNumber(cardNumber.value)) {
    cardNumber.setCustomValidity("Invalid Card Number");
  } else {
    cardNumber.setCustomValidity("");
  }
  if (!payform.validateCardExpiry(payform.parseCardExpiry(cardExpiry.value))) {
    cardExpiry.setCustomValidity("Invalid Expiry Date");
  } else {
    cardExpiry.setCustomValidity("");
  }
  if (!payform.validateCardCVC(cardCvc.value)) {
    cardCvc.setCustomValidity("Invalid CVC");
  } else {
    cardCvc.setCustomValidity("");
  }
});
