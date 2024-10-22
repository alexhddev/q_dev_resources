package com.barosanu;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PasswordCheckerTest {

    private PasswordChecker passwordChecker;

    @BeforeEach
    void setUp() {
        passwordChecker = new PasswordChecker();
    }

    @Test
    void testValidPassword() {
        assertTrue(passwordChecker.checkPassword("Valid1PassAAA!"));
    }

    @Test
    void testPasswordTooShort() {
        assertFalse(passwordChecker.checkPassword("Short1!"));
    }

    @Test
    void testPasswordTooLong() {
        assertFalse(passwordChecker.checkPassword("ThisPasswordIsWayTooLong1!"));
    }

    @Test
    void testPasswordNoUppercase() {
        assertFalse(passwordChecker.checkPassword("lowercase1!"));
    }

    @Test
    void testPasswordNoLowercase() {
        assertFalse(passwordChecker.checkPassword("UPPERCASE1!"));
    }

    @Test
    void testPasswordNoDigit() {
        assertFalse(passwordChecker.checkPassword("NoDigits!"));
    }

    @Test
    void testPasswordNoSpecialChar() {
        assertFalse(passwordChecker.checkPassword("NoSpecialChar1"));
    }

    @Test
    void testValidPasswordWithThrowReason() {
        assertTrue(passwordChecker.checkPasswordAndThrowReason("Valid1Pass!"));
    }

    @Test
    void testPasswordTooShortWithThrowReason() {
        Exception exception = assertThrows(IllegalArgumentException.class, () ->
                passwordChecker.checkPasswordAndThrowReason("Short1!")
        );
        assertEquals("Password must be at least 8 characters long", exception.getMessage());
    }

    @Test
    void testPasswordTooLongWithThrowReason() {
        Exception exception = assertThrows(IllegalArgumentException.class, () ->
                passwordChecker.checkPasswordAndThrowReason("ThisPasswordIsWayTooLong1!")
        );
        assertEquals("Password must be at most 20 characters long", exception.getMessage());
    }

    @Test
    void testPasswordNoUppercaseWithThrowReason() {
        Exception exception = assertThrows(IllegalArgumentException.class, () ->
                passwordChecker.checkPasswordAndThrowReason("lowercase1!")
        );
        assertEquals("Password must contain at least one uppercase letter", exception.getMessage());
    }

    @Test
    void testPasswordNoLowercaseWithThrowReason() {
        Exception exception = assertThrows(IllegalArgumentException.class, () ->
                passwordChecker.checkPasswordAndThrowReason("UPPERCASE1!")
        );
        assertEquals("Password must contain at least one lowercase letter", exception.getMessage());
    }

    @Test
    void testPasswordNoDigitWithThrowReason() {
        Exception exception = assertThrows(IllegalArgumentException.class, () ->
                passwordChecker.checkPasswordAndThrowReason("NoDigits!")
        );
        assertEquals("Password must contain at least one digit", exception.getMessage());
    }

    @Test
    void testPasswordNoSpecialCharWithThrowReason() {
        Exception exception = assertThrows(IllegalArgumentException.class, () ->
                passwordChecker.checkPasswordAndThrowReason("NoSpecialChar1")
        );
        assertEquals("Password must contain at least one special character", exception.getMessage());
    }
}
