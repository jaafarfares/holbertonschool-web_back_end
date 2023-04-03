const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Welcome to Holberton School, what is your name?\n', (answer) => {
  if (answer !== null) {
    process.stdout.write(`Your name is: ${answer}\n`);
  }
  rl.close();
});

rl.on('close', () => {
  process.stdout.write('This important software is now closing\n');
});
