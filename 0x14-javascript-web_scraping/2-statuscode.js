#!/usr/bin/node
/* 2-statuscode.js */

const request = require("request");
let reqURL =process.argv[1];

request (reqURL, function(error, response, body) {
	if (error) {
		console.log(error);
	}
	if (response) {
		let st = response.statusCode;
		console.log(st);
	}
});
