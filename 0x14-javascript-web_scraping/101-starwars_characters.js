#!/usr/bin/node
const axios = require('axios').default;
function getName (url) {
  return axios.get(url)
    .then(response => {
      console.log(response.data.name);
    });
}

const displayData = async () => {
  try {
    const response = await axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2]);
    for (const character of response.data.characters) {
      await getName(character);
    }
  } catch (err) {
    console.log('Found error');
  }
};

displayData();
