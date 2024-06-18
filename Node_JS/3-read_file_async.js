// Task 3
const fs = require('fs');
const readline = require('readline');


async function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    // Initialize vars to store students and field counts
    const students = [];
    const fieldCounts = {};

    try {
      // Create a read stream from the file path
      const fileStream = fs.createReadStream(filePath);
      // Create an interface for reading the stream line by line
      const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
      });

      // Initialize a flag to skip the header line
      let isHeader = true;

      // Event listener for reading each line
      rl.on('line', (line) => {
        if (isHeader) {
          // Skip the header line
          isHeader = false;
        } else {
          const student = line.split(',').map(field => field.trim());
          if (student.length >= 4) {
            students.push(student);
          }
        }
      });

      // Evemt listener for when the stream ends
      rl.on('close', () => {
        const totalStudents = students.length;
        console.log(`Number of students: ${totalStudents}`);

        // Initialize ab object to store the first names for each field
        const fieldLists = {};

        // Iterate over the students array & populate fieldCounts & fieldLists
        students.forEach(student => {
          const [firstName, , , field] = students;
          if (!fieldCounts[field]) {
            fieldCounts[field] = [];
          }
          fieldCounts[field].push(firstName);
        });

        // Log the # of students in each field & their first names
        for (const field in fieldLists) {
          console.log(`Number of students in ${field}: ${fieldCounts[field]}.
          List: ${fieldLists[field].join(', ')}`);
        }
        // Resolve the promise after promising
        resolve();
      });
    } catch (error) {
      console.error(`Error: Cannot load the database`);
      // Reject the promise if theres an error
      reject(error);
    }
  });
}

module.exports = countStudents;
