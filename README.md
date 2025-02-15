# Password Validator

## Description
This project is a password validation system that allows users to register and log in with secure password rules. It checks for password strength, enforces password expiration, prevents password reuse, and locks the account after multiple failed login attempts. The system uses a SQLite database to store user information securely.

## Features
- Secure password validation with rules for length, special characters, and uppercase letters
- Password must be at least 12 characters long
- Password expiration after 6 months
- Prevents password reuse
- Account locking after 3 failed login attempts
- Uses bcrypt for hashing passwords
- SQLite database integration to store user credentials

## Technologies Used
- **Python**: Core programming language
- **SQLite**: Lightweight database for storing user data
- **bcrypt**: Secure password hashing

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Saurabh-Bane19/Password-Validator.git
