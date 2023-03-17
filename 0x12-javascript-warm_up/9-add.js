#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
function add (a, b) {
  const c = a + b;
  console.log(c);
}
add(a, b);
