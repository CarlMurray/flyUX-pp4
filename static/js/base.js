let hamburgerMenu = document.querySelector('#hamburger-menu')
let hamburgerMenuExpanded = document.querySelector('#hamburger-menu-expanded')
let isOpen = false
hamburgerMenu.addEventListener('click', function(){
    isOpen = !isOpen
    if (isOpen === true) {
        hamburgerMenuExpanded.classList.remove('hidden')
    }
    else hamburgerMenuExpanded.classList.add('hidden')
})