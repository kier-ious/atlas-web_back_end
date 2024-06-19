const express = require('express');

const app = express();

// Define da roots
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// List on port 1245
const port = 1245;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Export the app variable
module.exports = app;
