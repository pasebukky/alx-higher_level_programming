#!/usr/bin/node
// Script that display the status code of a GET request

const request = require('request');
request.get(process.argv[2], (error, response) => {
  if (err) {
    console.error(error);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
