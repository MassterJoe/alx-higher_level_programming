#!/usr/bin/node
const process = require('process');
let count = 0;
for (const i in process.argv) {
  count = count + 1;
}
if (count < 3) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
