#!/usr/bin/node
const request = require('request');

request.get({ url: process.argv[2] }, function (error, response, body) {
  if (error) console.error(error);
  let count = 0;
  const movies = JSON.parse(body).results;
  for (let i = 0; i < movies.length; i++) {
    for (let j = 0; j < movies[i].characters.length; j++) {
      if (titlelist[i].characters[j].split('/')[5] === '18') {
        count++;
        break;
      }
    }
  }
  console.log(count);
});
