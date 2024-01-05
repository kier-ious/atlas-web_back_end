export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // Getter and Setter for CODE
  get code() {
    return this._code;
  }

  set code(newCode) {
    this._code = newCode;
  }

  // Getter and Setter for NAME
  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = newName;
  }

  // Method to display full currency information
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
