import getListStudents from './0-get_list_students';

export default function updateStudentGradeByCity(students) {
  const filterStudents = students.filter((student) => student.location === city);
  const updatedStudents = filterStudents.map((student) => {
    const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
    const grade = gradeObj ? gradeObj.grade : 'N/A';
    return { ...student, grade };
  });
  return updatedStudents;
}
