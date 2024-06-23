// Task 8, Basic Integration testing
const express = require('express');
const app = express();
const port = 7865;

app.get('/', (req, resolve) => {
  resolve.send('Welcome to the payment system');
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;

// adding a comment becaue I stopped the server
