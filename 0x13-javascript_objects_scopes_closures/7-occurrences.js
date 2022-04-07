#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let occurences = 0; occurences < list.length; occurences++) {
    if (list[occurences] === searchElement) {
      count += 1;
    }
  }
  return (count);
};
