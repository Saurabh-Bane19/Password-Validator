Password Validator

Description

This project is a password validation system that allows users to register and log in with secure password rules. It checks for password strength, enforces password expiration, prevents password reuse, and locks the account after multiple failed login attempts. The system uses a SQLite database to store user information securely.

Features

Secure password validation with rules for length, special characters, and uppercase letters

Password must be at least 12 characters long

Password expiration after 6 months

Prevents password reuse

Account locking after 3 failed login attempts

Uses bcrypt for hashing passwords

SQLite database integration to store user credentials

Technologies Used

Python: Core programming language

SQLite: Lightweight database for storing user data

bcrypt: Secure password hashing

Installation

Clone the repository:

git clone https://github.com/Saurabh-Bane19/Password-Validator.git

Navigate to the project directory:

cd Password-Validator

Set up a virtual environment:

python -m venv venv

Activate the virtual environment:

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Usage

To test password validation and user login attempts, run the following command:

python test_password_validation_failed_attempts.py

Expected Behavior:

Users can register and attempt login.

If the password is incorrect three times, the account gets locked.

Password strength rules are enforced.

Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.