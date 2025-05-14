import datetime
# parameters:
# -- id
# -- name
# -- description
# -- price_per_night
# -- user_id (owner)
# -- dates_booked -- changed from dates_available


class Space():
    def __init__(self, id, name, description, price_per_night, user_id, dates_booked = []):
        self.id = id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.user_id = user_id
        self.dates_booked = dates_booked
    
    def __eq__(self, value):
        return self.__dict__ == value.__dict__
    
    def __repr__(self):
        return f"space({self.id}, {self.name}, {self.description}, {self.price_per_night}, {self.user_id}, {self.dates_booked})"
    
    def is_valid(self):
        if self.name == None or self.name == "":
            return False
        if self.description == None or self.description == '':
            return False
        if self.price_per_night == None or self.price_per_night == '':
            return False
        if self.user_id == None or self.user_id == '':
            return False
        if not self.dates_booked: # changed this
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.name == None or self.name == "":
            errors.append("Name can't be blank")
        if self.description == None or self.description == '':
            errors.append("Description can't be blank")
        if self.price_per_night == None or self.price_per_night == '':
            errors.append("Price per night can't be blank")
        if self.user_id == None or self.user_id == '':
            errors.append("User ID can't be blank")
        if not self.dates_booked: # changed this
            errors.append("Dates Booked can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
