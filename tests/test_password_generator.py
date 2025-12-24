"""
Test program for Password Generator class
"""

# Import required modules
import pytest
import string
from password_generator import PasswordGenerator, password_length_error
import importlib.util
from pathlib import Path


# Test class for PasswordGenerator
class TestPasswordGenerator:
    def test_package_version_available(self):
        init_path = Path(__file__).resolve().parent.parent / "src" / "__init__.py"
        spec = importlib.util.spec_from_file_location("passwordgenerator_init", init_path)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
        assert module.__version__

    def test_generate_password_none(self):
        """Test password generation with default length (None)"""
        password = PasswordGenerator.generate_password()
        assert 4 <= len(password) <= 32

    def test_generate_password_four(self):
        """Test password generation with minimum length"""
        password = PasswordGenerator.generate_password(password_length=4)
        assert len(password) == 4

    def test_generate_password_eight(self):
        """Test password generation with length eight"""
        password = PasswordGenerator.generate_password(password_length=8)
        assert len(password) == 8

    def test_generate_password_sixteen(self):
        """Test password generation with length sixteen"""
        password = PasswordGenerator.generate_password(password_length=16)
        assert len(password) == 16

    def test_generate_password_thirtytwo(self):
        """Test password generation with maximum length"""
        password = PasswordGenerator.generate_password(password_length=32)
        assert len(password) == 32

    def test_small_letters(self):
        """Test password contains at least one small letter"""
        password = PasswordGenerator.generate_password(password_length=10)
        for c in password:
            if c.islower():
                check = True
        if not check:
            pytest.raises(
                AssertionError,
                match="Password must contain at least one lowercase letter",
            )
        else:
            assert check

    def test_capital_letters(self):
        """Test password contains at least one capital letter"""
        password = PasswordGenerator.generate_password(password_length=10)
        for c in password:
            if c.isupper():
                check = True
        if not check:
            pytest.raises(
                AssertionError,
                match="Password must contain at least one uppercase letter",
            )
        else:
            assert check

    def test_numbers(self):
        """Test password contains at least one number"""
        password = PasswordGenerator.generate_password(password_length=10)
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
        password = PasswordGenerator.generate_password(password_length=10)
        for c in password:
            if c in string.punctuation:
                check = True
        if not check:
            pytest.raises(
                AssertionError,
                match="Password must contain at least one special character",
            )
        else:
            assert check

    def test_generate_password_short(self):
        """Test password generation if the length is too short"""
        with pytest.raises(
            password_length_error, match="Password length must be at least 4"
        ):
            PasswordGenerator.generate_password(password_length=3)

    def test_generate_password_long(self):
        """Test password generation if the length is too long"""
        with pytest.raises(
            password_length_error, match="Password length must not exceed 32"
        ):
            PasswordGenerator.generate_password(password_length=33)

    def test_invalid_type(self):
        """Test password generation with invalid type"""
        with pytest.raises(TypeError):
            PasswordGenerator.generate_password(password_length="eight")
