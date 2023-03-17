#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const a = parseInt(argv[2]);
function fact (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
console.log(fact(a));
