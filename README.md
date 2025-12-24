![Github Logo](https://img.shields.io/badge/github-repo-blue?logo=github) ![Coverage100%](https://img.shields.io/badge/coverage-100%25-orange)
# Password Generator

A python package that generates passwords based on user-defined length.
This tool generates password that are mixed of uppercase letters, lowercase letters, digits and special characters. Maximum length of password that can be generated is 128 characters.

## Installation
1. Fork and Clone the repository:
   ```bash
   git clone https://github.com/Rudy-Ong/PasswordGenerator.git
   cd PasswordGenerator
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
Define the length of the password you want to generate (4-32 characters).
To generate a password, you can use the following code snippet:

```bash
import PasswordGenerator
PasswordGenerator.generate_password() # Automatically generates 4-32 random characters
```

If we want to specify number of characters e.g., 12 characters, use below codes:
```bash
import PasswordGenerator
PasswordGenerator.generate_password(12)
```

![Output Example](/generate_example.png?raw=true "Output Example")

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
│   ├── PasswordGenerator.py    # Password Generator implementation
├── tests/
│   ├── __init__.py
│   └── test_password_generator.py   # Test suite
├── .gitignore
├── .coveragerc                    # Coverage configuration
├── setup.cfg                      # Program configuration
├── requirements.txt               # Required packages  
└── README.md
```
## License

This project is for educational purposes.
