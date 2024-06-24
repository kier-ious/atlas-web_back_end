const request = require('request');
const { expect } = require('chai');
const app = require('./api.js');

// chai.use(chaiHttp);
// const { expect } = chai;

describe('Payment System', () => {
    describe('GET /', () => {
        it('should return 200 and welcome message', (done) => {
            request('http://localhost:7865/', (error, response, body) => {
                if (error) return done(error);
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome to the payment system');
                done();
            });
        });
    });

    describe('GET /cart/:id', function() {
        it('should return 200 when :id is a number', (done) => {
            const id = 12;
            request(`http://localhost:7865/cart/${id}`, (error, response, body) => {
                if (error) return done(error);
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal(`Payment methods for cart ${id}`);
                done();
            });
        });

        it('should return 404 when :id is NOT a number', (done) => {
            request('http://localhost:7865/cart/hello', (error, response, body) => {
                if (error) return done(error);
                expect(response.statusCode).to.equal(404);
                done();
            });
        });
    });
});
// adding comment
