// Task 1
const readline = require('readline');

// Create an interface for reeading in standard input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

// Have prompt and ask user for their name
rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
  // Logging users name
  console.log(`Your name is: ${name}`);
  // Close the rl interface
  rl.close();
});

// Special lil event listener for when the interface is closed
rl.on('close', () => {
  // Send off for closing message
  console.log('This important software is now closing');
});
