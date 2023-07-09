#!/usr/bin/node
const axios = require('axios').default;

/**
 * Get the name of the character
 * @param {String} character_url url of the character in the API
 */
function getName (character_url) {
  axios.get(character_url)
    .then(response => {
      console.log(response.data.name);
    });
}

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(response => {
    response.data.characters.forEach(character => {
      getName(character);
    });
  });
