#!/usr/bin/node
const fs = require('fs');
const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, 'utf8', err => {
      if (err) {
        console.log(err);
      }
    });
  });
