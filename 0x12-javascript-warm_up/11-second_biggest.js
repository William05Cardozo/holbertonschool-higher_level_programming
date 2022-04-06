#!/usr/bin/node
const numb = process.argv.length;
const array = [];
let a;
for (a = 2; a < numb; a++) {
  array.push(Number(process.argv[a]));
}
if (array.length > 1) {
  const second = array.sort(function (a, b) { return b - a; });
  console.log(second[1]);
} else {
  console.log('0');
}
