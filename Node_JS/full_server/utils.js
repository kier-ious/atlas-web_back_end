const fs = require('fs').promises;
const readline = require('readline');

async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    const lines = data.split('\n').filter(Boolean);
    const students = lines.map(line => line.split(',').map(field => field.trim()));

    return students;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = { readDatabase };
