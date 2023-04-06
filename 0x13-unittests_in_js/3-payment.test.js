var assert = require('assert');
var chai = require('chai');
var expect = chai.expect;
var sinon = require('sinon');



const sendPaymentRequestToApi = require('./3-payment.js');


describe('sendPaymentRequestToApi', () => {
  it("spy the api method", function() {
    sinon.spy(sendPaymentRequestToApi);
  })
});
