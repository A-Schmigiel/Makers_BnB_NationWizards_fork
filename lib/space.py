# parameters:
# -- id
# -- name
# -- description
# -- cost

class Space():
    def __init__(self, id, name, description, cost):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
    
    def __eq__(self, value):
        return self.__dict__ == value.__dict__
    
    def __repr__(self):
        return f"space({self.id}, {self.name}, {self.description}, {self.cost})"
    
    def is_valid(self):
        if self.name == None or self.name == "":
            return False
        if self.description == None or self.description == '':
            return False
        if self.cost == None or self.cost == '':
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.name == None or self.name == "":
            errors.append("name can't be blank")
        if self.description == None or self.description == '':
            errors.append("Description can't be blank")
        if self.cost == None or self.cost == '':
            errors.append("Cost can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
