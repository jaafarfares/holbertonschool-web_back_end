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
    const newcar = this.Constructor[Symbol.species];
    return new newcar();
  }
}
