var assert = require('assert');


const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should equal 3 when 1 + 2', function () {
    assert.equal(calculateNumber(1, 2), 3);
    assert.equal(calculateNumber(3, 2), 5);
    assert.equal(calculateNumber(5, -2), 3);
    assert.equal(calculateNumber(1, -1), 0);

  });
});
