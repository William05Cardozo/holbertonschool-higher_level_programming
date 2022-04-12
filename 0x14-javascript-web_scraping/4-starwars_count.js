#!/usr/bin/node
const request = require('request');
const fargs = process.argv;
request(fargs[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let count = 0;
  const id = JSON.parse(body).results;
  for (let i = 0; i < id.length; i++) {
    const character = id[i].characters.find((c) => {
      return (c.match(/18/));
    });
    if (character !== undefined) {
      count++;
    }
  }
  console.log(count);
});
