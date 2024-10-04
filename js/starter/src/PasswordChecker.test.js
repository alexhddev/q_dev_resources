import {test, describe} from 'node:test';
import assert from 'node:assert/strict';
import { checkPassword, checkPasswordAndThrowReason } from './PasswordChecker.js';

describe('checkPassword function', () => {
  test('returns true for valid password', () => {
    assert.strictEqual(checkPassword('ValidP@ss1'), true);
  });

  test('returns false for password shorter than 8 characters', () => {
    assert.strictEqual(checkPassword('Short1!'), false);
  });

  test('returns false for password longer than 20 characters', () => {
    assert.strictEqual(checkPassword('ThisPasswordIsWayTooLong123!'), false);
  });

  test('returns false for password without uppercase letter', () => {
    assert.strictEqual(checkPassword('lowercase123!'), false);
  });

  test('returns false for password without lowercase letter', () => {
    assert.strictEqual(checkPassword('UPPERCASE123!'), false);
  });

  test('returns false for password without digit', () => {
    assert.strictEqual(checkPassword('NoDigits!'), false);
  });

  test('returns false for password without special character', () => {
    assert.strictEqual(checkPassword('NoSpecialChar123'), false);
  });

  test('returns false for non-string input', () => {
    assert.strictEqual(checkPassword(12345), false);
    assert.strictEqual(checkPassword(null), false);
    assert.strictEqual(checkPassword(undefined), false);
    assert.strictEqual(checkPassword({}), false);
  });
});

describe('checkPasswordAndThrowReason function', () => {
  test('returns true for valid password', () => {
    assert.strictEqual(checkPasswordAndThrowReason('ValidP@ss1'), true);
  });

  test('throws error for password shorter than 8 characters', () => {
    assert.throws(() => checkPasswordAndThrowReason('Short1@'), {
      message: 'Password must be at least 8 characters long'
    });
  });

  test('throws error for password longer than 20 characters', () => {
    assert.throws(() => checkPasswordAndThrowReason('ThisPasswordIsWayTooLong123@'), {
      message: 'Password must be at most 20 characters long'
    });
  });

  test('throws error for password without uppercase letter', () => {
    assert.throws(() => checkPasswordAndThrowReason('lowercase123@'), {
      message: 'Password must contain at least one uppercase letter'
    });
  });

  test('throws error for password without lowercase letter', () => {
    assert.throws(() => checkPasswordAndThrowReason('UPPERCASE123@'), {
      message: 'Password must contain at least one lowercase letter'
    });
  });

  test('throws error for password without digit', () => {
    assert.throws(() => checkPasswordAndThrowReason('NoDigits@'), {
      message: 'Password must contain at least one digit'
    });
  });

  // test for ! char:
  test('throws error for password containing the ! character', () => {
    assert.throws(() => checkPasswordAndThrowReason('NoSpecialChar123!'), {
      message: 'Password cannot contain the ! character'
    });
  })

  test('throws error for password without special character', () => {
    assert.throws(() => checkPasswordAndThrowReason('NoSpecialChar123'), {
      message: 'Password must contain at least one special character'
    });
  });

  test('throws error for non-string input', () => {
    assert.throws(() => checkPasswordAndThrowReason(12345), {
      message: 'Password must be a string'
    });
  });
});
