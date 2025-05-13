from lib.request import Request

# parameters:
# -- id
# -- request_sender
# -- space_owner
# -- message_content
# -- space_requested
# -- dates_requested
# -- accepted (bool)

# functions:
# create request
# get all [sent]
# get all [recieved]
# view request

class RequestRepository():
    def __init__(self, connection):
        self.connection = connection
    
    def create_request(self, request):
        rows = self.connection.execute('INSERT INTO requests (request_sender, space_owner, message_content, space_requested, dates_requested, accepted) VALUES (%s, %s, %s, %s, %s) RETURNING id', [request.request_sender, request.space_owner, request.message_content, request.space_requested, request.dates_requested, request.accepted])
        row = rows[0]
        request.id = row["id"]
        return request
    
    def get_all_requests(self): # need to specify the sending/recieving parties
        rows = self.connection.execute('SELECT * from requests')
        requests = []
        for row in rows:
            item = Request(row["id"], row["request_sender"], row["space_owner"], row['message_content'], row["space_requested"], row["dates_requested"], row["accepted"])
            requests.append(item)
        return requests
    
    def get_request(self, id):
        rows = self.connection.execute(
            'SELECT * from requests WHERE id = %s', [id])
        row = rows[0]
        return Request(row["id"], row["request_sender"], row["space_owner"], row['message_content'], row["space_requested"], row["dates_requested"], row["accepted"])
    
    def remove_request(self, id):
        self.connection.execute('DELETE FROM requests WHERE id = %s')

