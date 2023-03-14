#!/usr/bin/node
// a function that prints the number of arguments already printed and the new argument value

let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
