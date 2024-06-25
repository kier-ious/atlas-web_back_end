// Task 10, Deep equality & Post integration testing
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 7865;
const host = 'localhost';

app.use(bodyParser.json());

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

app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.post('/login', (req, res) => {
  const { username } = req.body;
  res.send(`Welcome ${username}`);
});

app.listen(port, () => {
  console.log(`API available on ${host} port ${port}`);
});

module.exports = app;
// Adding comment
