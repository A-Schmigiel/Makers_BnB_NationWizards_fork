# parameters:
# -- id
# -- name
# -- description
# -- ppn (cost)
# -- user_id (owner)

# -- <<dates_available>>  -- need to add


class Space():
    def __init__(self, id, name, description, ppn, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.ppn = ppn
        self.user_id = user_id
    
    def __eq__(self, value):
        return self.__dict__ == value.__dict__
    
    def __repr__(self):
        return f"space({self.id}, {self.name}, {self.description}, {self.ppn}, {self.user_id})"
    
    def is_valid(self):
        if self.name == None or self.name == "":
            return False
        if self.description == None or self.description == '':
            return False
        if self.ppn == None or self.ppn == '':
            return False
        if self.user_id == None or self.user_id == '':
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.name == None or self.name == "":
            errors.append("name can't be blank")
        if self.description == None or self.description == '':
            errors.append("Description can't be blank")
        if self.ppn == None or self.ppn == '':
            errors.append("ppn can't be blank")
        if self.user_id == None or self.user_id == '':
            errors.append("User ID can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
