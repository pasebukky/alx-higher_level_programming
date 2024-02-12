#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const args = process.argv.slice(2);
  const arrangedArgs = args.map(Number).sort((a, b) => b - a);
  console.log(arrangedArgs[1]);
}
