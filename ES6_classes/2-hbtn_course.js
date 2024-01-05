export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }

    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw new TypeError('Length must be a valid number');
    }

    if (typeof students === 'object') {
      this._students = students;
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }

  // Getter and Setter for NAME
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  // Getter and Setter for LENGTH
  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    } else {
      throw new TypeError('Length must be a valid number');
    }
  }

  // Getter and Setter for STUDENTS
  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (typeof newStudents === 'object') {
      this._students = newStudents;
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }
}
