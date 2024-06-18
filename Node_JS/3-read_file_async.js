// Task 3
const fs = require('fs');
const readline = require('readline');


async function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    const students = [];
    const fieldCounts = {};

    try {
      const fileStream = fs.createReadStream(filePath);
      const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
      });

      let isHeader = true;

      rl.on('line', (line) => {
        if (isHeader) {
          isHeader = false;
        } else {
          const student = line.split(',').map(field => field.trim());
          if (student.length >= 4) {
            students.push(student);
          }
        }
      });

      rl.on('close', () => {
        const totalStudents = students.length;
        console.log(`Number of students: ${totalStudents}`);

        const fields = {};

        students.forEach(student => {
          const [firstName, , , field] = students;
          if (!fieldCounts[field]) {
            fieldCounts[field] = [];
          }
          fieldCounts[field].push(firstName);
        });

        for (const field in fields) {
          console.log(`Number of students in ${field}: ${fieldCounts[field]}.
          List: ${fieldLists[field].join(', ')}`);
        }
        resolve();
      });
    } catch (error) {
      console.error(`Error: Cannot load the database`);
      reject(error);
    }
  });
}

module.exports = countStudents;
