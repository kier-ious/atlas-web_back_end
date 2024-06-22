const chai = require('chai');
const sinon = require('sinon');
const expect = chai.expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', () => {
  let calculateNumberSpy;

  beforeEach(() => {
    calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  });

  afterEach(() => {
    calculateNumberSpy.restore();
  });

  it('should call Utils.calculateNumber with SUM 100, 20',function () {
    sendPaymentRequestToApi(100, 20);
    expect(calculateNumberSpy.calledOnce).to.be.true;
    expect(calculateNumberSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  });
});
