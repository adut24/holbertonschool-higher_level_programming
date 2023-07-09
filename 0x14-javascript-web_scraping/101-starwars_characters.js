#!/usr/bin/node
const axios = require('axios').default;

/**
 * Get the name of the character
 * @param {String} character_url url of the character in the API
 */
async function getName(character_url) {
  const response = await axios.get(character_url);
  console.log(response.data.name);
}

const displayData = async () => {
  try {
    const filmId = process.argv[2];
    const response = await axios.get(`https://swapi-api.hbtn.io/api/films/${filmId}`);
    const characters = response.data.characters;

    await Promise.all(characters.map(character => getName(character)));
  } catch (err) {
    console.log('Found error');
  }
};

displayData();
