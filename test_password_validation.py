import bcrypt
import sqlite3

# Connect to SQLite database
try:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    print("Connected to the database.")
except Exception as e:
    print(f"Error connecting to database: {e}")

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

    except Exception as e:
        print(f"Error during login: {e}")

# Test with wrong and correct passwords
login_user("newuser", "123456")  # Incorrect password example
login_user("newuser", "incorrectPassword")  # Incorrect password again
login_user("newuser", "incorrectPassword")  # Another incorrect attempt
login_user("newuser", "securePassword123")  # Correct password example after failed attempts

# Check the updated status of the user (lock status and failed attempts)
cursor.execute("SELECT * FROM users WHERE username = ?", ("newuser",))
user_data = cursor.fetchone()
print(f"Updated user data: {user_data}")

# Close the database connection
conn.close()
