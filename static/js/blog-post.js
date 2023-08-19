/*
Content is added to blog posts via a markdown field in the admin panel without styles applied.
This script is used to add styles to the content of the blog post.
*/

let h2s = document.querySelectorAll('h2');
let h3s = document.querySelectorAll('h3');
let h4s = document.querySelectorAll('h4');
let h5s = document.querySelectorAll('h5');
let main = document.querySelector('main');
let ps = main.querySelectorAll('p');

h2s.forEach(h2 => {
    h2.classList.add('text-primary', 'mb-4', 'mt-10', 'text-2xl');
})

h3s.forEach(h3 => {
    h3.classList.add('text-primary', 'mb-4', 'text-xl');
})

h4s.forEach(h4 => {
    h4.classList.add('text-primary', 'mb-4', 'text-md');
}) 

h5s.forEach(h5 => {
    h5.classList.add('text-primary', 'mb-4', 'text-sm');
})

ps.forEach(p => {
    p.classList.add('mb-4', 'text-text');
})