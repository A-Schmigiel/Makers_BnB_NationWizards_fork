from lib.request import Request
import datetime

# parameters:
# -- id
# -- request_sender
# -- space_owner
# -- message_content
# -- space_requested
# -- dates_requested
# -- accepted (bool)

class RequestRepository():
    def __init__(self, connection):
        self.connection = connection
    
    def create_request(self, request):
        rows = self.connection.execute('INSERT INTO requests (request_sender, space_owner, message_content, space_requested, dates_requested, accepted) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', [request.request_sender, request.space_owner, request.message_content, request.space_requested, request.dates_requested, request.accepted])
        row = rows[0]
        request.id = row["id"]
        return request
    
    def get_all_requests(self): 
        rows = self.connection.execute('SELECT * from requests')
        requests = []
        for row in rows:
            item = Request(row["id"], row["request_sender"], row["space_owner"], row['message_content'], row["space_requested"], row["dates_requested"], row["accepted"])
            requests.append(item)
        return requests
    
    def get_all_requests_for_user(self, user_id):
        rows = self.connection.execute('SELECT * from requests WHERE space_owner = %s OR request_sender = %s', [user_id, user_id])
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
        self.connection.execute('DELETE FROM requests WHERE id = %s', [id])

    def approve_request(self, request):
        self.connection.execute('UPDATE requests SET accepted = True WHERE id = %s', [request.id])
        return None
    
    def deny_request(self, request):
        self.connection.execute('UPDATE requests SET accepted = False WHERE id = %s', [request.id])
        return None
    
    def get_all_booked_nights(self, dates_range):
        start_date = dates_range[0]
        end_date = dates_range[1]
        all_nights_requested = []
        td=datetime.timedelta(days=1)
        while start_date <= end_date:
            all_nights_requested.append(start_date.isoformat())
            start_date += td
        all_nights_requested.pop(-1)
        return all_nights_requested

    # def decline_conflicting_dates(self, space_id, nights_booked):
    #     # nights_booked = ['2025-05-20','2025-05-22']
    #     for date in nights_booked:
    #         self.connection.execute(
    #             "UPDATE requests set accepted = FALSE WHERE accepted ISNULL AND space_requested = %s AND DATE %s = ANY (dates_requested)", [1, str(date)])
