# parameters:
# -- id
# -- username
# -- email
# -- password

class User():
    def __init__(self, id, username, email, password, confirm_password=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password #added this line

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    
    
    def __eq__(self, value):
        return self.__dict__ == value.__dict__
    
    def __repr__(self):
        return f"user({self.id}, {self.username}, {self.email}, {self.password})"
    
    def is_valid(self):
        if self.username == None or self.username == "":
            return False
        if self.email == None or self.email == '':
            return False
        if self.password == None or self.password == '':
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.username == None or self.username == "":
            errors.append("username can't be blank")
        if self.email == None or self.email == '':
            errors.append("email can't be blank")
        if self.password == None or self.password == '':
            errors.append("password can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)