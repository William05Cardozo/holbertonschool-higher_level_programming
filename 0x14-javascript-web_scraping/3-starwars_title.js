#!/usr/bin/node
const request = require('request');
const fargs = process.argv;
request('https://swapi-api.hbtn.io/api/films/' + fargs[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
