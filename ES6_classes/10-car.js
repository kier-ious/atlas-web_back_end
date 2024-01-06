const cloneSymbol = Symbol('clone');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    this[cloneSymbol] = this.cloneCar.bind(this);
  }

  // Getter for BRAND
  get brand() {
    return this._brand;
  }

  // Getter for MOTOR
  get motor() {
    return this._motor;
  }

  // Getter for COLOR
  get color() {
    return this._color;
  }

  // Static method to for cloning the car
  static cloneCar() {
    const { _brand, _motor, _color } = this;
    return new Car(_brand, _motor, _color);
  }
}
