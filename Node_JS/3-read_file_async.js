// Task 3
const fs = require('fs').promises;
const readline = require('readline');


async function countStudents(path) {
  try {
    // Read file asynchronously
    const data = await fs.readFile(path, 'utf8');
    processFileData(data);
  } catch (error) {
    console.error('Error: Cannot load the database');
  }
}

function processFileData(data) {
  // Split data into lines and remove trailing white space
  const lines = data.trim().split('\n')
}
