#!/usr/bin/node
/* 2-statuscode.js */

const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
