const trigger = document.getElementById('update_header');
const header = document.querySelector('header');

trigger.addEventListener('click', function() {
    header.textContent = 'New Header!!!';
})