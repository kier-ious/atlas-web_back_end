const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('return 4 when inputs are only 1 or 3', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('return 5 when inputs are only 1 or 3.7', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('return 5 when inputs are only 1.2 or 3.7', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('return 6 when inputs are only 1.5 or 3.7', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
