class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this.validateString(name, 'name');
    this._length = this.validateNumber(length, 'length');
    this._students = this.validateStudents(students, 'students');
  }

  // Getter and Setter for name
  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = (newName);
  }

  // Getter and Setter for length
  get length() {
    return this._length;
  }

  set length(newLength) {
    this._length = (newLength);
  }

  // Getter and Setter for students
  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._students = (newStudents);
  }

}
