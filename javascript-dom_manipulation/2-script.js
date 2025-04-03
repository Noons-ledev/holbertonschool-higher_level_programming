const header = document.querySelector('header');
const button = document.getElementById('red_header');

button.addEventListener('click', function() {
    header.classList.add('red');
});