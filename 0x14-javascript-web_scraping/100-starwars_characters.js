#!/usr/bin/node
const axios = require('axios').default;
function getName (url) {
  axios.get(url)
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
