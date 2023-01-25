#!/usr/bin/node
/* 3-starwars_title.js */

const request = require('request');
const episodeId = process.argv[2];
const url = 'http://swapi.co/api/films/' + episodeId;

request (url, function(err, res, body) {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).title);
});
