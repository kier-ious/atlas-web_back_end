const { readDatabase } = require('../utlis');

class studentController {
  static async getAllStudents(req, res) {
    try {
      const data = await readDatabase('./database.csv');
      const students = {};

      data.forEach(student => {
        const [firstname, lastname, age, field] = student;
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(`${firstname} ${lastname}`);
      });

      let response = 'This is the list of our students';
      for (const [field, name] of Object.entries(students)) {
        response += `Number of students in ${filed}: ${names.length}.
        List: ${names.join(', ')}`;
      }

      res.status(200).send(response);
    } catch (error) {
      res.status(500).send(error.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const major = req.params.major.toUpperCase();
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter muct be CS or SWE');
    }

    try {
      const data = await readDatabase('./database.csv');
      const students = data
        .filter(student => student[3] === major)
        .map(student => `${student[0]} ${student[1]}`);

      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (error) {
      res.status(500).send(error.message);
    }
  }
}

module.exports = studentController;
