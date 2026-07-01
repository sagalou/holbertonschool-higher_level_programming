#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const uniqueArgs = [...new Set(args)];
uniqueArgs.sort((a, b) => b - a);
console.log(uniqueArgs[1] !== undefined ? uniqueArgs[1] : 0);