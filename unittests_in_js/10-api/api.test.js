const chai = require('chai');
const request = require('request');
const expect = chai.expect;
const app = require('./api.js');

describe('Cart page', function() {
    it('Correct status code and result?', function(done) {
        request('http://localhost:7865/', function (error, response, body) {
            // if (error) return done(error);
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});

describe('Payment System', () => {
    describe('GET /', () => {
        it('Returns "Welcome to the payment system"', (done) => {
            request('http://localhost:7865/', (error, response, body) => {
                // if (error) return done(error);
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome to the payment system');
                done();
            });
        });
    });
});

describe('GET /cart/:id', () => {
    it('Returns Payment methods for cart number', (done) => {
        const id = 12;
        request(`http://localhost:7865/cart/${id}`, (error, response, body) => {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal(`Payment methods for cart ${id}`);
            done();
        });
    });

    it('Return 404 when :id is NOT a number', (done) => {
        request('http://localhost:7865/cart/hello', (error, response, body) => {
            // if (error) return done(error);
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});

describe('Payment methods endpoint', () => {
  describe('GET /available_payments', () => {
    it('Returns correct payment methods object', (done) => {
      request('http://localhost:7865/available_payments', { json: true }, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        });
        done();
      });
    });
  });
});

describe('Login endpoint POST /login', () => {
  it('Returns welcome message with userName', (done) => {
      const userName = 'Betty';
      request.post({
          url: 'http://localhost:7865/login',
          json: true,
          body: { userName }
      }, (error, response, body) => {
          expect(response.statusCode).to.equal(200);
          expect(body).to.equal(`Welcome ${userName}`);
          done();
      });
  });
});
