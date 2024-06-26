// Task 3
const fs = require('fs');
const readline = require('readline');


async function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    // Initialize vars to store students and field counts
    const students = [];
    const fieldCounts = {};
    const fieldLists = {};

    try {
      // Create a read stream from the file path
      const fileStream = fs.createReadStream(filePath);
      // Create an interface for reading the stream line by line
      const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
      });

      // // Initialize a flag to skip the header line
      // let isHeader = true;

      // Event listener for reading each line
      rl.on('line', (line) => {
          const student = line.split(',').map(field => field.trim());
          if (student.length >= 4) {
            students.push(student);
          }
        }
      );


      // Evemt listener for when the stream ends
      rl.on('close', () => {
        const totalStudents = students.length - 1;
        console.log(`Number of students: ${totalStudents}`);

        // Iterate over the students array & populate fieldCounts & fieldLists
        students.forEach(student => {
          const [firstName, , , field] = student;
          fieldCounts[field] = (fieldCounts[field] || 0) + 1;
          if (!fieldLists[field]) {
            // fieldCounts[field] = 0;
            fieldLists[field] = [];
          }
          // fieldCounts[field] += 1;
          fieldLists[field].push(firstName);
        });


        // Log the # of students in each field & their first names
        const output = `Number of students: ${totalStudents}\n` +
        Object.keys(fieldCounts).map(field => {
          return `Number of students in ${field}: ${fieldCounts[field]}.
          List: ${fieldLists[field].join(', ')}`;
        }).join('\n');

        // Resolve the promise after promising
        resolve(output);
      });

      // Error event listener to handle file stream errors
      fileStream.on('error', (error) => {
        reject(new Error('Cannot load the database'));
      });

    } catch (error) {
      console.error(`Error: Cannot load the database`);
      // Reject the promise if theres an error
      reject(error);
    }
  });
}

module.exports = countStudents;
