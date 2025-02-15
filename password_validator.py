import bcrypt
import sqlite3

# Connect to SQLite database
try:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    print("Connected to the database.")
except Exception as e:
    print(f"Error connecting to database: {e}")

# Update the users table to include failed_attempts and is_locked columns
try:
    # Add failed_attempts and is_locked columns if not already present
    cursor.execute('''ALTER TABLE users ADD COLUMN failed_attempts INTEGER DEFAULT 0''')
    cursor.execute('''ALTER TABLE users ADD COLUMN is_locked INTEGER DEFAULT 0''')
    conn.commit()
    print("Database schema updated successfully.")
except sqlite3.OperationalError as e:
    print(f"Error updating database schema (probably already exists): {e}")

# Create users table if it doesn't exist
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password_hash TEXT,
                        failed_attempts INTEGER DEFAULT 0,
                        is_locked INTEGER DEFAULT 0)''')
    conn.commit()
    print("Table created (if not exists).")
except Exception as e:
    print(f"Error creating table: {e}")

# Function to register a new user
def register_user(username, password):
    try:
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        # Insert new user into the database
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        print(f"User {username} registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    except Exception as e:
        print(f"Error registering user: {e}")

# Example of registering a user
register_user("newuser", "securePassword123")

# Check the database to see if the user was inserted
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Users in the database:")
for row in rows:
    print(row)

# Close the database connection
conn.close()
