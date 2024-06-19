// Task 2
const fs = require('fs');
const readline = require('readline');

async function countStudents(path) {
  try {
    // Creating a readable stream for the db file
    const fileStream = fs.createReadStream(path);
    const rl = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity
    });

    const counts = {};
    const lists = {};
    let totalStudents = 0;

    // Proocess each line of the file
    for await (const line of rl) {
      const [firstName, , , field] = line.split(',');

      // Skip dem empty lines
      if (firstName) {
        totalStudents++;

        // Update counts for each field
        counts[field] = (counts[field] || 0) + 1;

        // Update list of student names for the field
        if (!lists[field]) {
          lists[field] = [];
        }
        lists[field].push(firstName);
      }
    }

    // Closing readline interface
    rl.close();

    console.log(`Number of students: ${totalStudents}`);
    for (const field in counts) {
      console.log(`Number of students in ${field}: ${counts[field]}`);
    }

    return { totalStudents, counts, lists };
  } catch (error) {
    console.error('Error: Cannot load the database');
    throw error;
  }
}

module.exports = countStudents;
