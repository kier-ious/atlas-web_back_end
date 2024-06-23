const request = require('request');
const chai = require('chai');
const chaiHttp = require('chai-http');
const expect = chai.expect;

chai.use(chaiHttp);

describe('Cart page', function() {
  it('Correct status code when :id is a number?', function(done) {
      request('http://localhost:7865/cart/12', function (error, response) {
          if (error) return done(error);
          expect(response.statusCode).to.equal(200);
          done();
      });
  });

  it('Correct status code when :id is NOT a number (=> 404)?', function(done) {
      request('http://localhost:7865/cart/hello', function (error, response) {
          if (error) return done(error);
          expect(response.statusCode).to.equal(404);
          done();
      });
  });
});
