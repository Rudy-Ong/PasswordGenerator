# Password Generator

A python package that generates passwords based on user-defined length.
This tool generates password that are mixed of uppercase letters, lowercase letters, digits and special characters. Maximum length of password that can be generated is 128 characters.

## Installation
1. Fork and Clone the repository:
   ```bash
   git clone https://github.com/Rudy-Ong/PasswordManager.git
   cd PasswordManager
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
Define the length of the password you want to generate (maximum 128 characters).
To generate a password, you can use the following code snippet:
'''python
from password_generator import generate_password
password = generate_password(password_length=12)
print(password)
'''
This will generate a random password with length of 12 characters.

## Testing

### Run Tests with Verbose Output
To run the tests, use the following command:
```bash
python tests/test_password_generator.py -v
``` 

### Generate Coverage Report
```bash
pytest --cov=src --cov-report=html tests/
``` 

View the HTML report:
```bash
open htmlcov/index.html
```

## File Structure
```
SystemDevelopment5th/
├── src/
│   ├── __init__.py
│   ├── PasswordManager.py    # Password Manager implementation
├── tests/
│   ├── __init__.py
│   └── test_password_manager.py   # Test suite
├── .gitignore
├── .coveragerc                    # Coverage configuration
├── setup.cfg                      # Program configuration
├── requirements.txt               # Required packages  
└── README.md
```
## License

This project is for educational purposes.