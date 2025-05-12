# parameters:
# -- id
# -- request_sender
# -- space_owner
# -- message_content
# -- space_requested
# -- dates_requested

class User():
    def __init__(self, id, request_sender, space_owner, message_content, space_requested, dates_requested):
        self.id = id
        self.request_sender = request_sender
        self.space_owner = space_owner
        self.message_content = message_content
        self.space_requested = space_requested
        self.dates_requested = dates_requested
    
    def __eq__(self, value):
        return self.__dict__ == value.__dict__
    
    def __repr__(self):
        return f"user({self.id}, {self.request_sender}, {self.space_owner}, {self.message_content}, {self.space_requested}, {self.dates_requested})"
    
    def is_valid(self):
        if self.request_sender == None or self.request_sender == "":
            return False
        if self.space_owner == None or self.space_owner == '':
            return False
        if self.message_content == None or self.message_content == '':
            return False
        if self.space_requested == None or self.space_requested == '':
            return False
        if self.dates_requested == None or self.dates_requested == '':
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.request_sender == None or self.request_sender == "":
            errors.append("request_sender can't be blank")
        if self.space_owner == None or self.space_owner == '':
            errors.append("space_owner can't be blank")
        if self.message_content == None or self.message_content == '':
            errors.append("space_owner can't be blank")
        if self.space_requested == None or self.space_requested == '':
            errors.append("space_owner can't be blank")
        if self.dates_requested == None or self.dates_requested == '':
            errors.append("space_owner can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)