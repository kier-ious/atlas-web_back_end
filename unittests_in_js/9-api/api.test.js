const request = require('request');
const { expect } = require('chai');
const app = require('./api.js');

// chai.use(chaiHttp);
// const { expect } = chai;

describe('Cart page', function() {
    describe('GET /', function() {
        it('should return 200 and welcome message', function(done) {
            request('http://localhost:7865/', function (error, response, body) {
                if (error) return done(error);
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome to the payment system');
                done();
            });
        });
    });

    describe('GET /cart/:id', function() {
        it('should return 200 when :id is a number', function(done) {
            const id = 12;
            request(`http://localhost:7865/cart/${id}`, function (error, response) {
                if (error) return done(error);
                expect(response.statusCode).to.equal(200);
                done();
            });
        });

        it('should return 404 when :id is NOT a number', function(done) {
            request('http://localhost:7865/cart/hello', function (error, response) {
                if (error) return done(error);
                expect(response.statusCode).to.equal(404);
                done();
            });
        });
    });
});
// adding comment
