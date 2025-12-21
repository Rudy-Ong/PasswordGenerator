"""
Test program for Password Manager class
"""

# Import required modules
import sys
from pathlib import Path

# Ensure src/ is on path when running from repo root or via pytest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from password_manager import PasswordManager, password_length_error
import pytest
import string

# Test class for PasswordManager
class TestPasswordManager:
    def test_generate_password_four(self):
        """Test password generation with minimum length"""
        password_manager = PasswordManager()
        password = password_manager.generate_password(password_length=4)
        assert len(password) == 4

    def test_generate_password_eight(self):
        """Test password generation with length eight"""
        password_manager = PasswordManager()
        password = password_manager.generate_password(password_length=8)
        assert len(password) == 8

    def test_generate_password_sixteen(self):
        """Test password generation with length sixteen"""
        password_manager = PasswordManager()
        password = password_manager.generate_password(password_length=16)
        assert len(password) == 16

    def test_generate_password_thirtytwo(self):
        """Test password generation with maximum length"""
        password_manager = PasswordManager()
        password = password_manager.generate_password(password_length=32)
        assert len(password) == 32

    def test_small_letters(self):
        """Test password contains at least one small letter"""
        password = PasswordManager.generate_password(password_length=10)
        for c in password:
            if c.islower():
                check = True
        if not check:
            pytest.raises(
                AssertionError,
                match="Password must contain at least one lowercase letter"
            )
        else:
            assert check

    def test_capital_letters(self):
        """Test password contains at least one capital letter"""
        password = PasswordManager.generate_password(password_length=10)
        for c in password:
            if c.isupper():
                check = True
        if not check:
            pytest.raises(
                AssertionError,
                match="Password must contain at least one uppercase letter"
            )
        else:
            assert check

    def test_numbers(self):
        """Test password contains at least one number"""
        password = PasswordManager.generate_password(password_length=10)
        for c in password:
            if c.isdigit():
                check = True
        if not check:
            pytest.raises(
                AssertionError, match="Password must contain at least one number"
            )
        else:
            assert check

    def test_special_characters(self):
        """Test password contains at least one special character"""
        password = PasswordManager.generate_password(password_length=10)
        for c in password:
            if c in string.punctuation:
                check = True
        if not check:
            pytest.raises(
                AssertionError,
                match="Password must contain at least one special character"
            )
        else:
            assert check

    def test_generate_password_short(self):
        """Test password generation if the length is too short"""
        with pytest.raises(
            password_length_error, match="Password length must be at least 4"
        ):
            PasswordManager.generate_password(password_length=3)

    def test_generate_password_long(self):
        """Test password generation if the length is too long"""
        with pytest.raises(
            password_length_error, match="Password length must not exceed 32"
        ):
            PasswordManager.generate_password(password_length=33)

    def test_invalid_type(self):
        """Test password generation with invalid type"""
        with pytest.raises(TypeError):
            PasswordManager.generate_password(password_length="eight")
