const button = document.getElementById("add_item");
const ul = document.getElementsByClassName("my_list");

button.addEventListener('click', function() {
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul[0].appendChild(li);
});
