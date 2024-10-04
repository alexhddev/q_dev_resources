import { checkPassword, checkPasswordAndThrowReason } from '../src/PasswordChecker.js'

const result = checkPassword('Abcdefghijklmnopqrstuvwxyz');

console.log(result);