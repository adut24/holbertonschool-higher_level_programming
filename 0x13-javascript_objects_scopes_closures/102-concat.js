#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  fs.writeFileSync(process.argv[4], data, (err));
});
fs.readFile(process.argv[3], 'utf8', (err, data) => {
  fs.appendFileSync(process.argv[4], data, (err));
});
