from lib.user import User
import re

# parameters:
# -- id
# -- username
# -- email
# -- password

# functions:
# create
# sign in

class UserRepository():
    def __init__(self, connection):
        self.connection = connection
    
    def is_valid(self, password):
        spec_char = ['!', '@', '£', '$', '%', '&']
        return len(password) > 7 and any(char in password for char in spec_char)

    def create_user(self, user):
        if '@' not in user.email or '.' not in user.email or user.email.endswith('.'):
            raise ValueError("Please input a valid email")
        if not self.is_valid(user.password):
            raise ValueError("Password must be 8 or more characters and contain at least one special character")
        if user.password != user.confirm_password:
            raise ValueError("Passwords must match")
        rows = self.connection.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id', [user.username, user.email, user.password])
        row = rows[0]
        user.id = row["id"]
        return user
    
    def get_all_users(self):
        rows = self.connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["email"], row['password'])
            users.append(item)
        return users
    
    def get_user(self, id):
        rows = self.connection.execute(
            'SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["username"], row["email"], row["password"])
    
    def remove_user(self, id):
        self.connection.execute('DELETE FROM users WHERE id = %s', [id])

    # Adding sign in method
    def sign_in(self, email, password):
        rows = self.connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s', [email, password]
        )
        if not rows:
            return None
        row = rows[0]
        return User(row["id"], row["username"], row["email"], row["password"])
    
    