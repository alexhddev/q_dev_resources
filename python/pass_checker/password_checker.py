import re

def validate_password(password):
    if len(password) < 8:
        return False

    if len(password) > 16:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    # check for special chars:
    special_chars = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"
    if not any(char in special_chars for char in password):
        return False

    return True


def validate_password_and_raise_reason(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

    if len(password) > 16:
        raise ValueError("Password must not exceed 16 characters")

    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit")

    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter")

    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter")

    # check for special chars:
    special_chars = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"
    if not any(char in special_chars for char in password):
        raise ValueError(f"Password must contain at least one special character from: {special_chars}")

    return True  # Password is valid if no exceptions were raised



def validate_password_and_raise_reason_regex(password):
    # Check length
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if len(password) > 16:
        raise ValueError("Password must not exceed 16 characters")

    # Check for at least one digit
    if not re.search(r"\d", password):
        raise ValueError("Password must contain at least one digit")

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter")

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter")

    # Check for special characters
    special_chars = r"[!@#$%^&*()-_=+\[{\]}\|;:'\",<.>/?`~]"
    if not re.search(special_chars, password):
        raise ValueError(f"Password must contain at least one special character from: !@#$%^&*()-_=+[{{}}]\\|;:'\",<.>/?`~")

    return True  # Password is valid if no exceptions were raised
