#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  const arg = argv.sort((a, b) => b - a);
  const x = arg[3];
  console.log(x);
}
