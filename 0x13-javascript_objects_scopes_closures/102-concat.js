#!/usr/bin/node
const io = require('io');
const file1 = io.readFileSync(process.argv[2]);
const file2 = io.readFileSync(process.argv[3]);
io.writeFileSync(process.argv[4], file1);
io.appendFileSync(process.argv[4], file2);
