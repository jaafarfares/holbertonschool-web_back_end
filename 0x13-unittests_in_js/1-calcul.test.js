var assert = require('assert');


const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
    describe('type SUM', () => {
    it('should equal 3 when 1 + 2', () => {
        assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
        assert.strictEqual(calculateNumber('SUM', 2, -2), 0);
        assert.strictEqual(calculateNumber('SUM', 1, -4), -3);
    
      });
    });
    it('should equal 3 when 5 - 2', function () {
        assert.strictEqual(calculateNumber('SUBTRACT', 5, 2), 3);
        assert.strictEqual(calculateNumber('SUBTRACT', 3, 2), 1);
        assert.strictEqual(calculateNumber('SUBTRACT', 6, 0), 6);
    
      });
    it('should equal 3 when 6 / 2', function () {
        assert.strictEqual(calculateNumber('DIVIDE', 6, 2), 3);
        assert.strictEqual(calculateNumber('DIVIDE', 3, 1), 3);
        assert.strictEqual(calculateNumber('DIVIDE', 5, 2), 2.5);
        assert.strictEqual(calculateNumber('DIVIDE', 1, 1), 1);
    
      });
});
