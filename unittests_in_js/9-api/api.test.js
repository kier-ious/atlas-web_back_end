const request = require('request');
const { expect } = require('chai');

describe('Cart page', function() {
    describe('GET /cart/:id', function() {
        it('should return 200 when :id is a number', function(done) {
            const id = 12;
            request(`http://localhost:7865/cart/${id}`, function (error, response) {
                if (error) return done(error);
                expect(response.statusCode).to.equal(200);
                done();
            });
        });
    });

    it('should return 404 when :id is NOT a number', function(done) {
        chai.request('http://localhost:7865/cart/hello', function (error, response) {
            if (error) return done(error);
            expect(response.statusCode).to.have.status(404);
            done();
        });
    });
});
