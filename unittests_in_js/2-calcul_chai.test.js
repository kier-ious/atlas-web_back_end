const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calulateNumber', () => {
  describe('SUM', () => {
    it('return 6 when inputs are only 1.4 and 4.5', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });

  describe('SUBTRACT', () => {
    it('return -4 when inputs are only 1.4 and 4.5', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
  });

  describe('DIVIDE', () => {
    it('return 0.2 when inputs are only 1.4 or 4.5', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('return "Error" when inputs are only 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });
});
