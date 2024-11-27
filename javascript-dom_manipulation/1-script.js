// Select the element with the id 'red_header'
const redHeaderButton = document.getElementById('red_header');

// Add a click event listener to the element
redHeaderButton.addEventListener('click', function() {
    // Select the header element using document.querySelector
    const headerElement = document.querySelector('header');
    // Set the text color of the header element to red
    headerElement.style.color = '#FF0000';
});
