#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;
  printCharactersInOrder(characters, 0);
});

function printCharactersInOrder (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request.get(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const character = JSON.parse(body);
    console.log(character.name);
    printCharactersInOrder(characters, index + 1);
  });
}
