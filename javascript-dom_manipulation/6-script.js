const toDisplay = document.getElementById('character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then((response) => response.json())
    .then((data) => {
        toDisplay.textContent = data.name;
        })
    .catch((e) => {
        toDisplay.textContent = 'Failed to load name';
    });