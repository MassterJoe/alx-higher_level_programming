#!/usr/bin/node
const SquareK = require('./5-square.js');
class Square extends SquareK {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = "";
      for (let j = 0; this.width; j++) {
        row += 'C';
      }
	console.log(row);
    }
  }
}
module.exports = Square;
