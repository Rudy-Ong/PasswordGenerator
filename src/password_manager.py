import random
import string

class password_length_error(Exception):
    """Custom exception for invalid password length"""

    pass


class PasswordManager:
    min_length = 4
    max_length = 32

    @staticmethod
    def generate_password(password_length: int | None = 0) -> str:
        # Validate type early so pytest catches TypeError when a non-int is passed
        if password_length is not None and not isinstance(password_length, int):
            raise TypeError("password_length must be an integer")
        # Validate length constraints
        elif password_length == 0:
            password_length = random.randint(4,32)
        elif password_length < PasswordManager.min_length:
            raise password_length_error("Password length must be at least 4")
        elif password_length > PasswordManager.max_length:
            raise password_length_error("Password length must not exceed 32")
        
        # Character groups include small letters, capital letters, numbers, and special characters
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        numbers = string.digits
        special_characters = string.punctuation

        groups = [small_letters, capital_letters, numbers, special_characters]

        # Ensure at least one character from each group
        password_chars = [
            random.choice(small_letters),
            random.choice(capital_letters),
            random.choice(numbers),
            random.choice(special_characters),
        ]

        # Randomly choose from the 4 groups until reach length n
        while len(password_chars) < password_length:
            group = random.choice(groups)
            password_chars.append(random.choice(group))

        # Shuffle to avoid predictable order
        random.shuffle(password_chars)

        # Print the final password as a string
        print("Generate Random Password: " + "".join(password_chars))

        # Return the final password
        return "".join(password_chars)
