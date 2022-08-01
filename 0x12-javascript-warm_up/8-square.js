#!/usr/bin/node
let square = '';
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      square += 'X';
    }
    square += '\n';
  }
  square = square.slice(0, -1);
  if (square.length !== 0) {
    console.log(square);
  }
}
