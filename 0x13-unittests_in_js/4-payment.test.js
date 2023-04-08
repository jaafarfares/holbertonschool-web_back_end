const mocha = require('mocha');
const { expect, assert } = require('chai');
const sinon = require('sinon');

const utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const { spy } = require('sinon');

describe('sendPaymentRequestToApi', () => {
  it('should call calculateNumber', () => {
    const stub = sinon.stub(utils, 'calculateNumber');
    stub.returns(10);
    const spyy = sinon.spy(console, 'log');
    const req = sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(spyy.calledOnceWithExactly('The total is: 10'));
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(req);

    stub.restore();
    spyy.restore();
  });
});
