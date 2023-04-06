var sinon = require('sinon');
var chai = require('chai');


const sendPaymentRequestToApi = require('./3-payment.js');
const utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    it('should call calculateNumber and log the correct message', () => {
      const stub = sinon.stub(utils, 'calculateNumber');
      stub.returns(10);
      const spyy = sinon.spy(console, 'log');
      const response = sendPaymentRequestToApi(100, 20);
  
      chai.expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
      chai.expect(spyy.calledOnceWithExactly('The total is: 10'));
      chai.expect(utils.calculateNumber('SUM', 100, 20)).to.equal(response);
  
      stub.restore();
      spyy.restore();
    });
  });
  
