export default class Pricing {
  /**
     *
     * @param {Number} ammount
     * @param {Currency} currency
     */
  constructor(ammount, currency) {
    this._ammount = ammount;
    this._currency = currency;
  }

  get ammount() {
    return this._ammount;
  }

  set ammount(ammount) {
    this._ammount = ammount;
  }

  get currency() {
    return this._currency;
  }

  set currency(currency) {
    this._currency = currency;
  }

  displayFullPrice() {
    return `${this._ammount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(ammount, conversionRate) {
    return ammount * conversionRate;
  }
}
