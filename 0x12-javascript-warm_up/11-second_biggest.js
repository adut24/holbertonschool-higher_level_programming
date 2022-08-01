#!/usr/bin/node
let array = process.argv;
function sorting (a, b) {
  return parseInt(a) - parseInt(b);
}
if (array.length === 2 || array.length === 3) {
  console.log('0');
} else {
  array = array.slice(2);
  array.sort(sorting);
  console.log(array[array.length - 2]);
}
