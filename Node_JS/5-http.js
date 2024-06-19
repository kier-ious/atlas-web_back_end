const http = require('http');
const countStudents = require('./3-read_file_async');
const host = 'localhost';
const port = 1245;
const url = require('url');


const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === `/students`) {
    // Get db file path from cmd line args

    const dbPath = process.argv[2];

    if (!dbPath) {
      // Setting status code to show internal server error
      res.statusCode = 500;
      res.end('Error: Database file path not provided');
    } else {
      // Call function to get the list of students from CSV
      countStudents(dbPath)
        .then((output) => {
          res.write('This is the list of our students');
          res.end(output);
        })
        .catch(error => {
          res.statusCode = 500;
          res.end(`Error: ${error.message}`);
        });
    }
  } else {
    res.statusCode = 404;
    res.end('Error 404: Not Found')
  }
});

// Listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the app variable
module.exports = app;
