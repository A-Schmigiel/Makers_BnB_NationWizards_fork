from lib.space import Space

# parameters:
# -- id
# -- Name
# -- description
# -- cost

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
        rows = self.connection.execute('INSERT INTO spaces (name, description, cost) VALUES (%s, %s, %s) RETURNING id', [space.name, space.description, space.cost])
        row = rows[0]
        space.id = row["id"]
        return space
    
    def get_all_spaces(self):
        rows = self.connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row['cost'])
            spaces.append(item)
        return spaces
    
    def get_space(self, id):
        rows = self.connection.execute(
            'SELECT * from spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["cost"])
    
    def remove_space(self, id):
        self.connection.execute('DELETE FROM spaces WHERE id = %s')

    def check_calendar(self):
        pass
