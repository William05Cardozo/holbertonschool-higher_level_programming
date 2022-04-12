#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const file = args[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) {
        return (console.log(err));
      }
    });
  }
});
