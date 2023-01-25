#!/usr/bin/node
/* 3-starwars_title.js */

const request = require("request");
let episode = process.argv[2];
let reqURL = 'https://swapi-api.alx-tools.com/api/films/' + episode;

request.get(reqURL, function (erro, response, body) {
	if (eror) {
		console.log(error);
	}
	if (body {
		body = JSON.parse(body));
		console.log(body.title);
	}
});
