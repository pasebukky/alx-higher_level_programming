#!/usr/bin/node
// Script that display the status code of a GET request

const request = require('request');
request.get(process.argv[2], (err, response) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
