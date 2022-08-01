#!/usr/bin/node
const array = process.argv;
if (array.length === 2 || array.length === 3) {
  console.log('0');
} else {
  array.sort();
  console.log(array[array.length - 2]);
}
