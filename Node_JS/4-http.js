const http = require('http');

// Create the HTTP server
const app = http.createServer((req, res) => {
  // Set the respomse header
  res.writeHead(200, {'Content-Type': 'text/plain' });

  // Send the response w/ the message "Hello Holberton School!"
  res.end('Hello Holberton School!');
});

// Port to listen on
app.listen(1245);

// Export the app var
module.exports = app;
