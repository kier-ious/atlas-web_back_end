export default function getStudentIdsSum(students) {
  const sumOfIds = students.reduce((total, student) => total + student.id, 0);
  return sumOfIds;
}
