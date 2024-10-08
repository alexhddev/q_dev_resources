import unittest
from password_checker import validate_password, validate_password_and_raise_reason

class TestPasswordValidator(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(validate_password("P@ssw0rd"))
        self.assertTrue(validate_password("C0mplex!Pass"))
        self.assertTrue(validate_password("Abcd1234!"))

    def test_short_password(self):
        self.assertFalse(validate_password("Sh0rt!"))

    def test_long_password(self):
        self.assertFalse(validate_password("ThisPasswordIsWayTooLong123!"))

    def test_no_digits(self):
        self.assertFalse(validate_password("NoDigitsHere!"))

    def test_no_uppercase(self):
        self.assertFalse(validate_password("nouppercase123!"))

    def test_no_lowercase(self):
        self.assertFalse(validate_password("NOLOWERCASE123!"))

    def test_no_special_char(self):
        self.assertFalse(validate_password("NoSpecialChar123"))

    def test_edge_cases(self):
        self.assertTrue(validate_password("Aa1!5678"))  # Minimum length
        self.assertTrue(validate_password("Aa1!567890123456"))  # Maximum length
        self.assertFalse(validate_password("Aa1!567"))  # One character short
        self.assertFalse(validate_password("Aa1!56789012345678"))  # One character long

    def test_empty_password(self):
        self.assertFalse(validate_password(""))

    def test_all_special_chars(self):
        self.assertFalse(validate_password("!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"))

    def test_various_special_chars(self):
        special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"
        for char in special_chars:
            self.assertTrue(validate_password(f"ValidPass1{char}"))

class TestPasswordValidatorWithExceptions(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(validate_password_and_raise_reason("P@ssw0rd"))
        self.assertTrue(validate_password_and_raise_reason("C0mplex!Pass"))
        self.assertTrue(validate_password_and_raise_reason("Abcd1234!"))

    def test_short_password(self):
        with self.assertRaisesRegex(ValueError, "Password must be at least 8 characters long"):
            validate_password_and_raise_reason("Sh0rt!")

    def test_long_password(self):
        with self.assertRaisesRegex(ValueError, "Password must not exceed 16 characters"):
            validate_password_and_raise_reason("ThisPasswordIsWayTooLong123!")

    def test_no_digits(self):
        with self.assertRaisesRegex(ValueError, "Password must contain at least one digit"):
            validate_password_and_raise_reason("NoDigitsHere!")

    def test_no_uppercase(self):
        with self.assertRaisesRegex(ValueError, "Password must contain at least one uppercase letter"):
            validate_password_and_raise_reason("nouppercase123!")

    def test_no_lowercase(self):
        with self.assertRaisesRegex(ValueError, "Password must contain at least one lowercase letter"):
            validate_password_and_raise_reason("NOLOWERCASE123!")

    def test_edge_cases(self):
        self.assertTrue(validate_password_and_raise_reason("Aa1!5678"))  # Minimum length
        self.assertTrue(validate_password_and_raise_reason("Aa1!567890123456"))  # Maximum length
        
        with self.assertRaisesRegex(ValueError, "Password must be at least 8 characters long"):
            validate_password_and_raise_reason("Aa1!567")  # One character short
        
        with self.assertRaisesRegex(ValueError, "Password must not exceed 16 characters"):
            validate_password_and_raise_reason("Aa1!56789012345678")  # One character long

    def test_empty_password(self):
        with self.assertRaisesRegex(ValueError, "Password must be at least 8 characters long"):
            validate_password_and_raise_reason("")

    def test_all_special_chars(self):
        with self.assertRaisesRegex(ValueError, "Password must contain at least one uppercase letter"):
            validate_password_and_raise_reason("4!@#$%^&*()-_=")

    def test_various_special_chars(self):
        special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"
        for char in special_chars:
            self.assertTrue(validate_password_and_raise_reason(f"ValidPass1{char}"))
            

if __name__ == '__main__':
    unittest.main()
