// Select the element with the id 'update_header'
const updateHeaderButton = document.getElementById('update_header');

// Add a click event listener to the element
updateHeaderButton.addEventListener('click', function() {
    // Select the header element using document.querySelector
    const headerElement = document.querySelector('header');
    // Update the text content of the header element
    headerElement.textContent = 'New Header!!!';
});
