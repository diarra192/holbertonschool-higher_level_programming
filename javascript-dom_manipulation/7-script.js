document.addEventListener('DOMContentLoaded', function () {
  // URL from which to fetch the data
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  // Fetch the data from the URL
  fetch(url)
      .then(response => response.json())  // Parse the JSON from the response
      .then(data => {
          // Select the HTML ul element with id 'list_movies'
          const listMovies = document.getElementById('list_movies');

          // Iterate through each movie in the data results
          data.results.forEach(movie => {
              // Create a new li element
              const movieItem = document.createElement('li');
              // Set the text content of the li element to the movie's title
              movieItem.textContent = movie.title;
              // Append the new li element to the ul
              listMovies.appendChild(movieItem);
          });
      })
      .catch(error => {
          console.error('Error fetching movies:', error);
      });
});
