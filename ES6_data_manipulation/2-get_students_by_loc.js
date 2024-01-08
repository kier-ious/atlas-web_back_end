import getListStudents from './1-get_list_student_ids';

export default function getStudentsByLocation(students, city) {
  const studentsInCity = students.filter((student) => student.location === city);
  return studentsInCity;
}

const city = 'San Francisco';
const students = getListStudents();
const studentsInCity = getStudentsByLocation(students, city);

console.log(studentsInCity);
