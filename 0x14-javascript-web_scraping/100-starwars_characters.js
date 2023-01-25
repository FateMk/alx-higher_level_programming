#!/usr/bin/node 
/* 100-starwars_characters.js */

const request = require('request');
let filmID = process.argv[2];
let reqUrl = 'https://swapi-api.alx-tools.com/api/' + filmID;

request.get(reqUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (body) {
    body = JSON.parse(body);
    console.log(body.characters);
  }
});
