// Task 9, Regex Integration testing
const express = require('express');
const app = express();
const port = 7865;

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
  const id = req.params.id;
  res.send(`Payment methods for: ${id}`);
});

app.listen(7865, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
