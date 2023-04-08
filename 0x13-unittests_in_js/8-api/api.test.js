process.env.NODE_ENV = 'test';

//Require the dev-dependencies
let chai = require('chai');
let server = require('../server');
describe('/GET', () => {
    it('it should GET the response', (done) => {
      chai.request(server)
          .get('/book')
          .end((err, res) => {
                res.should.have.status(200);
                res.body.should.be.a('array');
                res.body.length.should.be.eql(0);
            done();
          });
    });
});
