#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (argv.length > 2) {
  console.log(argv[2] + ' ' + 'is' + ' ' + argv[3]);
}
