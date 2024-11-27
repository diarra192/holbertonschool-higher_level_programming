// Select the element with the id 'toggle_header'
const toggleHeaderButton = document.getElementById('toggle_header');

// Add a click event listener to the element
toggleHeaderButton.addEventListener('click', function() {
    // Select the header element using document.querySelector
    const headerElement = document.querySelector('header');
    // Check current class of the header and toggle accordingly
    if (headerElement.classList.contains('red')) {
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    } else {
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    }
});
