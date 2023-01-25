#!/usr/bin/node
/* 0-redme.js */

const request = require('request');
let url = process.argv[2];

request.readFile (url, 'utf8', function (error, body) {
 if (error) {
  console.log(error);
 } else {
  console.log(body);
 }
});
