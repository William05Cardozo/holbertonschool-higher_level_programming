#!/usr/bin/node
const request = require('request');
const fargs = process.argv;

request(fargs[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const js = JSON.parse(body);
    const list = {};
    for (let i = 0; i < js.length; i++) {
      if (i.completed === true) {
        if (list[i.userId] === undefined) {
          list[i.userId] = 0;
        }
        list[i.userId] += 1;
      }
    }
    console.log(list);
  }
});
