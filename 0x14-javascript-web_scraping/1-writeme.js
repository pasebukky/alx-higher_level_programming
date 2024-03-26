#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
