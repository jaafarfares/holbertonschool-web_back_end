const request = require('request');
let chai = require('chai');


describe('testiing', () => {
    describe('GET /', () => {
        it('Code: 200 | Body: Welcome to the payment system', (done) => {
            const options = {
                url: 'http://localhost:7865',
                method: 'GET',
            };
            request(options, function (error, response, body) {
                chai.expect(response.statusCode).to.equal(200);
                chai.expect(body).to.equal('Welcome to the payment system');
                done();
        
            });    });
    });
    describe('GET /cart/12', () => {
        it('responds with 200 and "Welcome to the payment system" in the body',  (done) => {
          const options = {
            url: 'http://localhost:7865/cart/12',
            method: 'GET',
          };
    
          request(options, function (error, response, body) {
            chai.expect(response.statusCode).to.equal(200);
            chai.expect(body).to.equal('Payment methods for cart 12');
            done();
          });
        });
      });
});
