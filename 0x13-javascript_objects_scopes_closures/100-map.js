#!/usr/bin/node
const list = require('./100-data').list;
const array = [];
for (let i = 0; list[i]; i++) {
  array.push(list[i] * i);
}
console.log(list);
console.log(array);
