const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Welcome to Holberton School, what is your name?\n', (answer) => {
  process.stdout.write(`Your name is: ${answer}\n`);
  process.stdout.write('This important software is now closing\n');
  rl.close();
});
