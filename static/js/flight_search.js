let airportInputs = document.querySelectorAll("#origin, #destination");
let airportsList = document.querySelectorAll("#airports-list, #airports-list1");
// SHOW AIRPORTS ON FOCUS
// for (item of origin){
    

// item.addEventListener("focus", function (e) {
//     airportsList.classList.remove("hidden");
//     // HIDE AIRPORTS ON BLUR
//     item.addEventListener("blur", function (e) {
//         airportsList.classList.add("hidden");
//     });
// });


airportInputs.forEach((item) => {
    item.addEventListener('focus', function (e) {
        airportsList[item].classList.remove("hidden");
        // HIDE AIRPORTS ON BLUR
        item.addEventListener("blur", function (e) {
            airportsList.classList.add("hidden");
        });
    });
})

// let showAirportsInputMenu = () => {
//     // SHOW AIRPORTS ON FOCUS
//     airportsList.classList.remove("hidden");
//     // HIDE AIRPORTS ON BLUR
//     item.addEventListener("blur", function (e) {
//         airportsList.classList.add("hidden");
//     });
// }