var assert = require('assert');


const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should equal 3 when 1 + 2', function () {
    assert.equal(calculateNumber(1, 2), 3);
  });
});
