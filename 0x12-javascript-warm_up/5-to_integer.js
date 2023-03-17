#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (parseInt(argv[2])) {
  console.log('My number:' + ' ' + argv[2]);
} else {
  console.log('Not a number');
}
