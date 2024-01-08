export default function updateStudentGradeByCity(students, city) {
  const filterStudents = students.filter((student) => student.location === city);
  const updatedStudents = filterStudents.map((student) => {
    const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
    const grade = gradeObj ? gradeObj.grade : 'N/A';
    return { ...student, grade };
  });
  return updatedStudents;
}
