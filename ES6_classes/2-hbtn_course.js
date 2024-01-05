export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getter and Setter for name
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string');
      this._name = newName;
    }

  // Getter and Setter for length
  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength === 'length');
      this._length = newLength;
    }

  // Getter and Setter for students
  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (typeof newStudents === 'students');
      this._students = newStudents;
    }

}
