#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, { json: true }, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const title = JSON.parse(body).title;
  console.log(title);
});
