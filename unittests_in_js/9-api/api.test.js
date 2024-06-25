const chai = require('chai');
const request = require('request');
const expect = chai.expect;
// const { expect } = require('chai');
const app = require('./api.js');

// chai.use(chaiHttp);
// const { expect } = chai;
describe('Index page', function() {
    it('Correct status code?', function(done) {
        request('http://localhost:7865/', function (error, response) {
            // if (error) return done(error);
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('Correct result?', function(done) {
        request('http://localhost:7865/', function (error, response, body) {
            // if (error) return done(error);
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
// adding comment another
