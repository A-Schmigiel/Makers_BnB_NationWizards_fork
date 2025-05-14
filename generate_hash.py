from flask_bcrypt import Bcrypt
#Generate hashed password for test user john_doe
bcrypt = Bcrypt()
password = "password123"  # Replace with the password you want to hash
hashed = bcrypt.generate_password_hash(password).decode('utf-8')
print(hashed)

#Generate hashed password for test user jane_doe
bcrypt = Bcrypt()
password = "password456"  # Replace with the password you want to hash
hashed = bcrypt.generate_password_hash(password).decode('utf-8')
print(hashed)