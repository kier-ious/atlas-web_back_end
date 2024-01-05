export default class Building {
  constructor(sqft) {
    if (!this.evacuationWarningMessage && this.constructor !== Building) {
      throw new TypeError('Class extending Building must override evac');
    }
    this._sqft = sqft;
  }

  // Getter for SQFT
  get sqft() {
    return this._sqft;
  }
}
