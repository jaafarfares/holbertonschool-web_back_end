var sinon = require('sinon');

const sendPaymentRequestToApi = require('./3-payment.js');
const utils = require('./utils');


describe('sendPaymentRequestToApi', () => {
  it("spy the api method", () => {
    sinon.spy(utils, 'calculateNumber');
  })
});
