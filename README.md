# NonComplexPasswordGenerator (NCPG)

Welcome to NonComplexPasswordGenerator (NCPG) - your solution for creating strong and secure passwords that are easy to remember. NCPG allows you to customize the composition of your passwords by giving you control over the characters, words, special characters, and numbers used.

## Getting Started

### Installation

Clone repo using Git Clone:

Install NCPG using pip:

`pip install noncomplexpasswordgenerator`

### Basic Usage

To use NCPG, import the `PasswordGenerator` class and create an instance:

pythonCopy code

`from noncomplexpasswordgenerator import PasswordGenerator

# Create an instance of the PasswordGenerator

password_gen = PasswordGenerator()`

### Generating a Password

Generate a password by specifying the desired length and character sets:

pythonCopy code

`# Generate a password with default settings
password = password_gen.generate_password(length=12)

# Generate a password with custom settings

password_custom = password_gen.generate_password(
length=16,
use_lowercase=True,
use_uppercase=True,
use_numbers=True,
use_special_characters=True,
use_words=True,
)`

## Customization Options

You have control over various aspects of password generation:

- `use_lowercase`: Include lowercase letters (default: True).
- `use_uppercase`: Include uppercase letters (default: True).
- `use_numbers`: Include numbers (default: False).
- `use_special_characters`: Include special characters (default: True).
- `use_words`: Include common words for better memorization (default: True).

### Example

pythonCopy code

`# Customized password with uppercase, numbers, and special characters
custom_password = password_gen.generate_password(
    length=15,
    use_lowercase=True,
    use_uppercase=True,
    use_numbers=True,
    use_special_characters=True,
    use_words=False,
)`

## Conclusion

NCPG provides a balance between password strength and memorability, allowing you to create strong passwords tailored to your preferences. Experiment with the customization options to find the perfect combination for your needs.

Feel free to explore additional features and options offered by NCPG to enhance your password generation experience.

Happy password creating! 🚀
