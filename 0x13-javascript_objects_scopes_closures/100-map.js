#!/usr/bin/node
const list = require('./100-data.js');

let i = 0;
const array = list.list;
console.log(array);
const map1 = array.map(x => x * i++);
console.log(map1);
