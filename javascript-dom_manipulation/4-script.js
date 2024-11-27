// Select the element with the id 'add_item'
const addItemButton = document.getElementById('add_item');

// Add a click event listener to the element
addItemButton.addEventListener('click', function() {
    // Select the ul element with the class 'my_list'
    const list = document.querySelector('.my_list');
    // Create a new li element
    const newItem = document.createElement('li');
    // Set the text content of the new li element
    newItem.textContent = 'Item';
    // Append the new li element to the ul
    list.appendChild(newItem);
});
