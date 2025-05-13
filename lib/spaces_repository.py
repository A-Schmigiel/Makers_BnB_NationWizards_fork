from lib.space import Space

# parameters:
# -- id
# -- name
# -- description
# -- price_per_night (cost)
# -- user_id (owner)

# -- <<dates_available>>  -- need to add

# functions:
# -- create
# -- list
# -- show space
# -- delete space
# -- get availability status

class spaceRepository():
    def __init__(self, connection):
        self.connection = connection
    
    def create_space(self, space):
        rows = self.connection.execute('INSERT INTO spaces (name, description, price_per_night, user_id) VALUES (%s, %s, %s, %s) RETURNING id', [space.name, space.description, space.price_per_night, space.user_id])
        row = rows[0]
        space.id = row["id"]
        return space
    
    def get_all_spaces(self):
        rows = self.connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row['price_per_night'], row['user_id'])
            spaces.append(item)
        return spaces
    
    def get_space(self, id):
        rows = self.connection.execute(
            'SELECT * from spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price_per_night"], row["user_id"])
    
    def remove_space(self, id):
        self.connection.execute('DELETE FROM spaces WHERE id = %s')

    def check_calendar(self):
        pass
