var sinon = require('sinon');

const sendPaymentRequestToApi = require('./3-payment.js');
const utils = require('./utils');


describe('sendPaymentRequestToApi', () => {
    it("calls calculateNumber with the correct arguments", () => {
      sinon.spy(utils, 'calculateNumber');
      sendPaymentRequestToApi(100, 20);
      sinon.assert.calledWith(utils.calculateNumber, 'SUM', 100, 20);
    })
  });
