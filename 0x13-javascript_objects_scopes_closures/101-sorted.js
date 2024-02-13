#!/usr/bin/node

const originalDict = require('./101-data').dict;

const newDict = {};
for (const userId in originalDict) {
  const count = originalDict[userId];
  if (newDict[count]) {
    newDict[count].push(userId);
  } else {
    newDict[count] = [userId];
  }
}
console.log(newDict);
