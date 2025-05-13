import datetime
from lib.space import Space

# parameters:
# -- id
# -- name
# -- description
# -- price_per_night
# -- user_id (owner)
# -- dates_available

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
        # created_date = datetime.datetime.today()
        # space.dates_available = [created_date + datetime.timedelta(days=x) for x in range(90)]
        rows = self.connection.execute('INSERT INTO spaces (name, description, price_per_night, user_id, dates_available) VALUES (%s, %s, %s, %s, %s) RETURNING id', [space.name, space.description, space.price_per_night, space.user_id, space.dates_available])
        row = rows[0]
        space.id = row["id"]
        return space
    
    def get_all_spaces(self):
        rows = self.connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row['price_per_night'], row['user_id'], row['dates_available'])
            spaces.append(item)
        return spaces
    
    def get_space(self, id):
        rows = self.connection.execute(
            'SELECT * from spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price_per_night"], row["user_id"], row['dates_available'])
    
    def remove_space(self, id):
        self.connection.execute('DELETE FROM spaces WHERE id = %s')

    def check_calendar(self):
        pass

