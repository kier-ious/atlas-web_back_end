const express = require('express');
const router = require('./routes/index');

const app = express();
const port = 1245;

app.use(express.json());
app.use('/',router);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

module.exports = app;
