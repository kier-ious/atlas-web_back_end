function getStudentsByLocation(students, city) {
  const studentsInCity = students.filter((student) => student.location === city);
  return studentsInCity;
}

const city = 'San Francisco';
const studentsInCity = getStudentsByLocation(student, city);
