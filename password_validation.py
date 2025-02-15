import re
from datetime import datetime, timedelta
import bcrypt

# List of common passwords (this could be expanded or loaded from a file)
common_passwords = ["123456", "password", "123456789", "qwerty", "abc123", "letmein", "welcome", "admin", "password1"]

# Example of a stored previous password hash and last change date (in a real system, this would be fetched from the database)
previous_password_hash = b"$2b$12$7GzDlB0StgwuMWSrCNpsbeFfeubbKuqVC/aPn9KOA.j7tK1vH/ioG"  # Example hash
last_password_change = datetime(2024, 8, 1)  # Date the password was last changed

# Function to simulate password hashing (you can replace this with actual bcrypt comparison in a real system)
def check_password_hash(password, stored_hash):
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

# Function to validate password strength and ensure password rules
def validate_password(username, password):
    current_date = datetime.now()

    # Check if password length is at least 12 characters
    if len(password) < 12:
        return "Password should be at least 12 characters long."
    
    # Check for special characters, numbers, and uppercase letters
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    
    # Check against common passwords
    if password in common_passwords:
        return "Password is too common. Please choose a stronger password."
    
    # Ensure password doesn't contain the username
    if username.lower() in password.lower():
        return "Password cannot contain your username."
    
    # Check if password needs to be updated (changed every 6 months)
    if current_date - last_password_change < timedelta(days=180):
        return "Your password needs to be updated every 6 months."
    
    # Ensure the user cannot reuse their previous password
    if check_password_hash(password, previous_password_hash):
        return "You cannot reuse your previous password."

    # If all checks pass
    return "Password is strong."

# Example usage
username = "newuser"
password = "Secure@123"
validation_message = validate_password(username, password)
print(validation_message)
