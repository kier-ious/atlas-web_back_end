const request = require('request');
const expect = require('chai').expect;

describe('Index page', () => {
  before(async () => {
    const chaiHttp = await import('chai-http');
    chai.use(chaiHttp.default);
  });

  it('Should return status code 200', (done) => {
    chai.request('http://localhost:7865')
    .get('/')
    .end((err, res) => {
      expect(res).to.have.status(200);
      done();
    });
  });

  it('Should return correct message', (done) => {
    chai.request('http://localhost:7865')
    .get('/')
    .end((err, res) => {
      expect(res.text).to.equal('Welcome to the payment system');
      done();
    });
  });
});
