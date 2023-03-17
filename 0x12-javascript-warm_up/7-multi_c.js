#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (argv[2] && parseInt(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    const x = 'C is fun';
    console.log(x);
  }
} else {
  console.log('Missing number of occurrences');
}
