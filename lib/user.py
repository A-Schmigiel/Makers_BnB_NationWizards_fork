from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, email, password, confirm_password=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password #added this line
        
    def get_id(self):
        return str(self.id)

    def __eq__(self, value):
        return self.__dict__ == value.__dict__

    def __repr__(self):
        return f"user({self.id}, {self.username}, {self.email}, {self.password})"

    def is_valid(self):
        if self.username is None or self.username == "":
            return False
        if self.email is None or self.email == '':
            return False
        if self.password is None or self.password == '':
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.username is None or self.username == "":
            errors.append("username can't be blank")
        if self.email is None or self.email == '':
            errors.append("email can't be blank")
        if self.password is None or self.password == '':
            errors.append("password can't be blank")
        return ", ".join(errors) if errors else None
