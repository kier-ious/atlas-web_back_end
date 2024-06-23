const { expect } = require('chai');

describe('Cart page', function() {
  it('Correct status code when :id is a number?', function(done) {
      chai.request('http://localhost:7865/cart/12', function (error, response) {
          if (error) return done(error);
          expect(response.statusCode).to.equal(200);
          done();
      });
  });

  it('Correct status code when :id is NOT a number (=> 404)?', function(done) {
      chai.request('http://localhost:7865/cart/hello', function (error, response) {
          if (error) return done(error);
          expect(response.statusCode).to.equal(404);
          done();
      });
  });
});
