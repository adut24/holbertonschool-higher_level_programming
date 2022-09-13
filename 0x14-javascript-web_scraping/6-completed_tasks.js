#!/usr/bin/node
const axios = require('axios').default;
const dict = {};
axios.get(process.argv[2])
  .then(function (response) {
    response.data.forEach(function (task) {
      if (task.completed) {
        if (dict[task.userId] === undefined) {
          dict[task.userId] = 0;
        }
        dict[task.userId] += 1;
      }
    });
    console.log(dict);
  });
