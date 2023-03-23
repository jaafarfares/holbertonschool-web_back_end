export default class Car {
  Constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.species]() {
  return this;
  }
  cloneCar() {
  return this.constructor[Symbol.species];
  }
}
