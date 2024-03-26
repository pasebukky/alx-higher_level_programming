#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const todos = JSON.parse(body);
  const completedTasksByUser = {};
  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });
  console.log(completedTasksByUser);
});
