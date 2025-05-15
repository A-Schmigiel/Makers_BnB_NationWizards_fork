from lib.request import Request
from lib.requests_repository import RequestRepository
from datetime import date


#create request
def test_create_request(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = RequestRepository(db_connection)

    new_request = Request(None, 1, 2,"new message content", 1, [date(2025, 10, 25), date(2025, 10, 30)], False)
    created_request = repo.create_request(new_request)

    assert created_request.id is not None
    assert created_request.request_sender == 1
    assert created_request.space_owner == 2
    assert created_request.message_content == "new message content"
    assert created_request.space_requested == 1
    assert created_request.dates_requested == [date(2025, 10, 25), date(2025, 10, 30)]
    assert created_request.accepted == False
    
# test to get all requests

def test_get_all_requests(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = RequestRepository(db_connection)

    requests = repo.get_all_requests()

    assert len(requests) == 4
    assert requests[0].message_content == "Is this available?"
    assert requests[1].accepted is True

#tests to return using a specific id

def test_get_request_by_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = RequestRepository(db_connection)

    request = repo.get_request(1)

    assert request.id == 1
    assert request.request_sender == 1
    assert request.space_owner == 2
    assert request.message_content == "Is this available?"
    assert request.space_requested == 1
    assert request.dates_requested == [date(2025, 6, 15), date(2025, 6, 20)]
    assert request.accepted is False

#tests to remove using id

def test_remove_request(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = RequestRepository(db_connection)

    repo.remove_request(1)
    requests = repo.get_all_requests()

    assert len(requests) == 3
    assert all(r.id != 1 for r in requests)