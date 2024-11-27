document.addEventListener('DOMContentLoaded', function () {
  // URL from which to fetch the data
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Fetch the greeting in French
  fetch(url)
      .then(response => response.json())  // Parse the JSON from the response
      .then(data => {
          // Select the HTML element with id 'hello'
          const helloDiv = document.getElementById('hello');
          // Set the text content of the element to the fetched 'hello' translation
          helloDiv.textContent = data.hello;
      })
      .catch(error => {
          console.error('Error fetching the greeting:', error);
      });
});
