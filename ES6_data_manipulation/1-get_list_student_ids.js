export default function getListStudentsIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const studentsIds = students.map((student) => student.id);
  return studentsIds;
}
