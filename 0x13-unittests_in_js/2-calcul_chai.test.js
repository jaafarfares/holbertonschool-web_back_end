var assert = require('assert');
var chai = require('chai');
var expect = chai.expect;



const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
    describe('type SUM', () => {
    it('should equal 3 when 1 + 2', () => {
        expect(calculateNumber('SUM', 2, 2)).equal(4);
        expect(calculateNumber('SUM', 2, 0)).equal(2);
        expect(calculateNumber('SUM', 2, -2)).equal(0);
        expect(calculateNumber('SUM', 2, -3)).equal(-1);

      });
    });
    it('should equal 3 when 5 - 2', function () {
        expect(calculateNumber('SUBTRACT', 5, 2)).equal(3);
        expect(calculateNumber('SUBTRACT', 2, 2)).equal(0);
        expect(calculateNumber('SUBTRACT', 2, 3)).equal(-1);
      });
    it('should equal 3 when 6 / 2', function () {
        expect(calculateNumber('DIVIDE', 2, 2)).to.equal(1);
        expect(calculateNumber('DIVIDE', 6, 2)).to.equal(3);
      });
});
