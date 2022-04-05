#!/usr/bin/node
const num = Number(process.argv[2]);
let str = 'X';
if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i < num; i++) {
    str = str + 'X';
  }
  for (let k = 0; k < num; k++) {
    console.log(str);
  }
}
