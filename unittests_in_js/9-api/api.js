// Task 9, Regex Integration testing
const express = require('express');
const app = express();
const port = 7865;
const host = 'localhost';

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
  const { id } = req.params;
  if (isNaN(id)) {
    return res.status(404).send('ID must be a number');
  }
  res.send(`Payment methods for cart ${req.params.id}`);
});

app.listen(port, () => {
  console.log(`API available on ${host} port ${port}`);
});

module.exports = app;
// Adding comment
