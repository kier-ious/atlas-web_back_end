export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Getter for NAME
  get name() {
    return this._name;
  }

  // Getter for CODE
  get code() {
    return this._code;
  }

  // Default string description
  toString() {
    return `[object ${this._code}]`;
  }
}
