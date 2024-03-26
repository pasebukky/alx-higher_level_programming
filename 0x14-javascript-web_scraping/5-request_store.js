#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const fs = require('fs');
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
