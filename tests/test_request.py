from lib.request import Request
from datetime import date

# Valid request with all fields
def test_request():
    request = Request(id=1, request_sender=1, space_owner="2", message_content="Is this available?", space_requested="1", dates_requested= [date(2025, 6, 15), date(2025, 6, 20)], accepted = "False")
    
    assert request.request_sender == 1
    assert request.space_owner == "2"
    assert request.message_content == "Is this available?"
    assert request.space_requested == "1"
    assert request.dates_requested == [date(2025, 6, 15), date(2025, 6, 20)]
    assert request.accepted == "False"


#Test for invalid request
def test_invalid_request():
    request = Request(id=1, request_sender=None, space_owner="", message_content= None, 
                space_requested=None, dates_requested= None, accepted = None)
    
    assert not request.is_valid()  # Request should be invalid
    errors = request.generate_errors()
    assert "Request sender can't be blank" in errors
    assert "Space owner can't be blank" in errors
    assert "Message content can't be blank" in errors
    assert "Space requested can't be blank" in errors
    assert "Dates requested can't be blank" in errors
    assert "Accepted can't be blank" in errors

# if fields are empty
def test_empty_fields():
    request = Request(id=1,request_sender=None,space_owner="",message_content="",space_requested="",dates_requested=[],accepted=None)
    
    assert not request.is_valid()  
    errors = request.generate_errors()
    assert "Request sender can't be blank" in errors
    assert "Space owner can't be blank" in errors
    assert "Message content can't be blank" in errors
    assert "Space requested can't be blank" in errors
    assert "Dates requested can't be blank" in errors
    assert "Accepted can't be blank" in errors

#Valid Request with accepted = True
def test_valid_request_accepted_true():
    request = Request(id=2,request_sender=2,space_owner="1",message_content="Is this pet friendly?",space_requested="2",dates_requested=[date(2025, 7, 1), date(2025, 7, 5)],accepted=True)
    
    assert request.request_sender == 2
    assert request.space_owner == "1"
    assert request.message_content == "Is this pet friendly?"
    assert request.space_requested == "2"
    assert request.dates_requested == [date(2025, 7, 1), date(2025, 7, 5)]
    assert request.accepted is True

#test for Equality
def test_request_equality():
    request1 = Request(id=1,request_sender=1,space_owner="2",message_content="Is this available?",space_requested="1",dates_requested=[date(2025, 6, 15), date(2025, 6, 20)],accepted=False)

    request2 = Request(id=1,request_sender=1,space_owner="2",message_content="Is this available?",space_requested="1",dates_requested=[date(2025, 6, 15), date(2025, 6, 20)],accepted=False)

    assert request1 == request2 

#test for Inequality
def test_request_inequality():
    request1 = Request(id=1,request_sender=1,space_owner="1",message_content="Is this available?",space_requested="1",dates_requested=[date(2025, 6, 15), date(2025, 6, 20)],accepted=False)

    request2 = Request(id=2,request_sender=2,space_owner="1",message_content="Is this available?",space_requested="1",dates_requested=[date(2025, 6, 15), date(2025, 6, 20)],accepted=False)

    assert request1 != request2 