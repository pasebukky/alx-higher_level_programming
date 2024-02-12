#!/usr/bin/node

const count = process.argv[2];

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(count);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
