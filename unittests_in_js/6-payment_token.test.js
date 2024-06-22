// 6 test
const chai = require('chai');
const expect = chai.expect;
const getPaymentTokenFromAPI = require('./6-payment_token.js');
const { get } = require('request');
const { response } = require('express');

describe('getPaymentTokenFromAPI', () => {
  it('Should return a successful response when its true', (done) => {
    getPaymentTokenFromAPI(true)
    .then((response) => {
      expect(response).to.deep.equal({data: 'Successful response from the API'});
      done();
    })
    .catch((error) => {
      done(error);
    });
  });
});
