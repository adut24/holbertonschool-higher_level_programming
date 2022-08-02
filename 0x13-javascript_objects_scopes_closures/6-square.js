#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    let square = '';
    for (let i = 0; i < this.height; i++) {
      square = '';
      for (let j = 0; j < this.width; j++) {
        square += c;
      }
      console.log(square);
    }
  }
};
