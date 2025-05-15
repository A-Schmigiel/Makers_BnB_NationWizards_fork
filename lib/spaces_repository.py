import calendar
import datetime
from lib.space import Space

# parameters:
# -- id
# -- name
# -- description
# -- price_per_night
# -- user_id (owner)
# -- dates_booked

# functions:
# -- create
# -- list
# -- show space
# -- delete space
# -- get availability status

class SpaceRepository():
    def __init__(self, connection):
        self.connection = connection
    
    def create_space(self, space):
        rows = self.connection.execute('INSERT INTO spaces (name, description, price_per_night, user_id, dates_booked) VALUES (%s, %s, %s, %s, %s) RETURNING id', [space.name, space.description, space.price_per_night, space.user_id, space.dates_booked])
        row = rows[0]
        space.id = row["id"]
        return space
    
    def get_all_spaces(self):
        rows = self.connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row['price_per_night'], row['user_id'], row['dates_booked'])
            spaces.append(item)
        return spaces
    
    def get_space(self, id):
        rows = self.connection.execute(
            'SELECT * from spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price_per_night"], row["user_id"], row['dates_booked'])
    
    def remove_space(self, id):
        self.connection.execute('DELETE FROM spaces WHERE id = %s', [id])
        return None

    def book_space(self, id, new_date_booking):
        current = self.connection.execute('SELECT dates_booked FROM spaces WHERE id = %s', [id])[0]['dates_booked']
        updated = current + [new_date_booking]
        self.connection.execute('UPDATE spaces SET dates_booked = %s WHERE id = %s', [updated, id])
    
