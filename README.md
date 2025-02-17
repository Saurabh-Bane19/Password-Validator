Password Validator 🔐
Description 📜
This project is a password validation system designed to ensure users adhere to secure password practices. 
It includes functionality for validating password strength, enforcing password expiration, preventing password reuse, and locking accounts after multiple 
failed login attempts. The system uses an SQLite database to securely store user credentials and track login attempt data, including the number of failed 
attempts and account lock status.

Features ⚙️

Password Strength Validation:

 Minimum password length of 12 characters. 🔑
 Must contain at least one uppercase letter. 🅰️
 Must contain at least one number. 🔢
 Must contain at least one special character (e.g., !@#$%^&*). 🔣
 Prevents the use of common passwords (e.g., "password", "123456"). 🚫

Password Expiration:

 Passwords must be updated every 6 months. ⏳

Password Reuse Prevention:

 Users cannot reuse their previous password. 🔒

Account Locking:

 Accounts are locked after 3 consecutive failed login attempts. 🔐

SQLite Database Integration:

 Stores user information, including username, password hash, and login attempt details. 💾

bcrypt:

 Securely hashes passwords before storing them in the database. 🛡️

Technologies Used 💻

 Python: Core programming language for the application logic. 🐍
 bcrypt: Library for securely hashing passwords. 🔐
 SQLite: Lightweight database for storing user credentials and login attempt details. 🗃️

Installation ⚡
 1. Clone the repository:

   git clone https://github.com/Saurabh-Bane19/Password-Validator.git

 2. Navigate to the project directory:

   cd Password-Validator

 3. Set up a virtual environment:
   
   python -m venv venv

 4. On Windows:

   venv\Scripts\activate

   On macOS/Linux:

   source venv/bin/activate


 5. Install dependencies:
    
    pip install -r requirements.txt

Usage 🚀

User Login with Failed Attempt Tracking 🔐

The system allows users to log in with their credentials. After 3 consecutive failed login attempts, the account will be locked. 
Below is an example of how to log in a user with tracking for failed attempts and lock status:

import bcrypt
import sqlite3

# Function to handle user login with failed attempt tracking
def login_user(username, password):
    try:
        # Fetch user data from database
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user is None:
            print("Username not found!")
            return

        user_id, db_username, db_password_hash, failed_attempts, is_locked = user

        print(f"Current failed_attempts: {failed_attempts}, is_locked: {is_locked}")  # Debugging output

        if is_locked:
            print("Account is locked. Please contact IT support.")
            return

        # Check if the password is correct
        if bcrypt.checkpw(password.encode('utf-8'), db_password_hash):
            print("Login successful!")
            # Reset failed attempts after successful login
            cursor.execute("UPDATE users SET failed_attempts = 0 WHERE id = ?", (user_id,))
            conn.commit()
        else:
            print("Incorrect password.")
            failed_attempts += 1
            if failed_attempts >= 3:
                cursor.execute("UPDATE users SET is_locked = 1 WHERE id = ?", (user_id,))
                print("Account is locked. Please contact IT support.")
            else:
                cursor.execute("UPDATE users SET failed_attempts = ? WHERE id = ?", (failed_attempts, user_id))
            conn.commit()

        # Debugging: print updated status
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        updated_user = cursor.fetchone()
        print(f"Updated user data: {updated_user}")  # Debugging output

    except Exception as e:
        print(f"Error during login: {e}")


Example Usage 📝

Test the system by logging in with both correct and incorrect passwords:

login_user("newuser", "123456")  # Incorrect password example
login_user("newuser", "incorrectPassword")  # Incorrect password again
login_user("newuser", "incorrectPassword")  # Another incorrect attempt
login_user("newuser", "securePassword123")  # Correct password example after failed attempts

Check the Updated User Status 🔍

You can check the updated user data to see the failed login attempts and whether the account is locked:

cursor.execute("SELECT * FROM users WHERE username = ?", ("newuser",))
user_data = cursor.fetchone()
print(f"Updated user data: {user_data}")

This will print the current state of the user, including failed login attempts and lock status.

Contributing 🤝

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.



