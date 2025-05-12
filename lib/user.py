# parameters:
# -- id
# -- username
# -- email
# -- password

class User():
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
    
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
            errors.append("email can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)