#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let temp;
  for (let i = 0; i < process.argv.length; i++) {
    for (let j = i + 1; j < process.argv.length; j++) {
      if (parseInt(process.argv[i]) > parseInt(process.argv[j])) {
        temp = process.argv[i];
        process.argv[i] = process.argv[j];
        process.argv[j] = temp;
      }
    }
  }
  console.log(process.argv[process.argv.length - 2]);
}
