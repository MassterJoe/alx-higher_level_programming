#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (argv[2] && parseInt(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    const x = 'X';
    console.log(x.repeat(parseInt(argv[2])));
  }
} else {
  console.log('Missing size');
}
