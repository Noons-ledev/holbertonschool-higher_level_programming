const toToggle = document.getElementById('toggle_header');
const header = document.querySelector('header');
toToggle.addEventListener('click', function() {
  if (header.classList.contains('red')) {
    header.classList.toggle('red');
    header.classList.toggle('green');
} else {
    header.classList.toggle('green');
    header.classList.toggle('red');
  }
});
