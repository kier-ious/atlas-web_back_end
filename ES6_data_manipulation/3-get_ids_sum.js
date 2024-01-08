export default function getStudentIdsSum(student) {
  const sumOfIds = students.reduce((total, student) => total + student.id);
  return sumOfIds;
}
