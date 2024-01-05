export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Getter for SIZE
  get name() {
    return this._name;
  }

  // Getter for LOCATION
  get code() {
    return this._code;
  }

  // Cast NUMBER
  valueOf() {
    return this._name;
  }

  // Cast to STRING
  toString() {
    return this._code;
  }
}
