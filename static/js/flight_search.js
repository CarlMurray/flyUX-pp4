let airportOrigin = document.querySelector("#origin");
let airportDestination = document.querySelector("#destination");
let airportsListOrigin = document.querySelector("#airports-list-origin");
let airportsListDestination = document.querySelector("#airports-list-destination");
let airportListItems = document.querySelectorAll('.airport-list-item')


document.addEventListener('click', (e) => {
    if (e.target == airportOrigin || e.target == airportDestination) {
      e.target.nextElementSibling.classList.remove('hidden');
    } else if (e.target != airportOrigin && e.target != airportsListOrigin || e.target != airportDestination && e.target != airportsListDestination) {
        airportsListOrigin.classList.add('hidden');
        airportsListDestination.classList.add('hidden');
    }
  });
  
  airportListItems.forEach((item) => {
    item.addEventListener('click', (e) => {
      console.log(item.innerText);
      let value = item.innerText;
      let parent = item.parentNode
      console.log('Parent:')
      console.dir(parent)
      let inputField = parent.parentNode.previousElementSibling
      console.dir(inputField)
      inputField.value = value;
    });
  });
