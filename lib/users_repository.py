from lib.user import User

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
    
    def create_user(self, user):
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
        self.connection.execute('DELETE FROM users WHERE id = %s')

