document.addEventListener('DOMContentLoaded', function () {
  // URL from which to fetch the data
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  // Fetch the data from the URL
  fetch(url)
      .then(response => response.json())  // Parse the JSON from the response
      .then(data => {
          // Select the HTML element with id 'character'
          const characterDiv = document.getElementById('character');
          // Set the text content of the element to the character's name
          characterDiv.textContent = data.name;
      })
      .catch(error => {
          console.error('Error fetching character:', error);
      });
});
