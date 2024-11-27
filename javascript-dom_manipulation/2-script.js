// Select the element with the id 'red_header'
const redHeaderButton = document.getElementById('red_header');

// Add a click event listener to the element
redHeaderButton.addEventListener('click', function() {
    // Select the header element using document.querySelector
    const headerElement = document.querySelector('header');
    // Add the class 'red' to the header element
    headerElement.classList.add('red');
});
