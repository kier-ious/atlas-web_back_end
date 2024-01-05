export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Getter for NAME
  get size() {
    return this._size;
  }

  // Getter for CODE
  get location() {
    return this._location;
  }

  // Cast NUMBER
  valueOf() {
    return this._size;
  }

  // Cast to STRING
  toString() {
    return this._location;
  }
}
