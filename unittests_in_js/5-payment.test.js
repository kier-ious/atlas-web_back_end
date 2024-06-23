const chai = require('chai');
const sinon = require('sinon');
const expect = chai.expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi', () => {
  let consoleLogSpy;

  beforeEach(() => {
    consoleLogSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleLogSpy.restore();
  });

  it('should log "The total is: 120" and be called once for 100 and 20',function () {
    sendPaymentRequestToApi(100, 20);
    expect(consoleLogSpy.calledOnce).to.be.true;
    expect(consoleLogSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
  });

  it('should log "The total is: 20" and be called once for 10 and 10',function () {
    sendPaymentRequestToApi(10, 10);
    expect(consoleLogSpy.calledOnce).to.be.true;
    expect(consoleLogSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
  });
});
