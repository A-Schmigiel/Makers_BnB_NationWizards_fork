from lib.space import Space
from datetime import datetime

# Valid space with all fields
def test_create_space():
    space = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night=100.00, user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    
    assert space.id == 1
    assert space.name == "Green Lodge"
    assert space.description == "A lodge that is green"
    assert space.price_per_night == 100.00
    assert space.user_id == 1
    assert space.dates_booked == ["2025-05-20", "2025-05-30"]

#Space is valid
def test_is_valid_with_valid_data():
    space = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night=100.00, user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    
    assert space.is_valid() == True

#Space is invalid when name is blank
def test_is_valid_with_blank_name():
    space = Space(id=1, name="", description="A lodge that is green", 
                price_per_night=100.00, user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    
    assert space.is_valid() == False

#Space is invalid when description is blank
def test_is_valid_with_blank_description():
    space = Space(id=1, name="Green Lodge", description="", 
                price_per_night=100.00, user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    
    assert space.is_valid() == False

#Space is invalid when price_per_night is blank
def test_is_valid_with_blank_price_per_night():
    space = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night="", user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    
    assert space.is_valid() == False

#Space is invalid when user_id is blank
def test_is_valid_with_blank_user_id():
    space = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night=100.00, user_id="", dates_booked=["2025-05-20", "2025-05-30"])
    
    assert space.is_valid() == False

#Space is invalid when dates_booked is blank
def test_is_valid_with_blank_dates_booked():
    space = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night=100.00, user_id=1, dates_booked=[])
    
    assert space.is_valid() == False

#generate_errors for missing name
def test_generate_errors_with_missing_name():
    space = Space(id=1, name="", description="A lodge that is green", 
                price_per_night=100.00, user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    
    errors = space.generate_errors()
    assert "Name can't be blank" in errors

#generate_errors for missing description
def test_generate_errors_with_missing_description():
    space = Space(id=1, name="Green Lodge", description="", 
                price_per_night=100.00, user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    
    errors = space.generate_errors()
    assert "Description can't be blank" in errors

#generate_errors for missing price_per_night
def test_generate_errors_with_missing_price_per_night():
    space = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night="", user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    
    errors = space.generate_errors()
    assert "Price per night can't be blank" in errors

#generate_errors for missing user_id
def test_generate_errors_with_missing_user_id():
    space = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night=100.00, user_id="", dates_booked=["2025-05-20", "2025-05-30"])
    
    errors = space.generate_errors()
    assert "User ID can't be blank" in errors

#generate_errors for missing dates_booked
def test_generate_errors_with_missing_dates_booked():
    space = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night=100.00, user_id=1, dates_booked=[])
    
    errors = space.generate_errors()
    assert "Dates Booked can't be blank" in errors

#equality of two identical Space objects
def test_space_equality():
    space1 = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night=100.00, user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    space2 = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night=100.00, user_id=1, dates_booked=["2025-05-20", "2025-05-30"])

    assert space1 == space2

#inequality of two different Space objects
def test_space_inequality():
    space1 = Space(id=1, name="Green Lodge", description="A lodge that is green", 
                price_per_night=100.00, user_id=1, dates_booked=["2025-05-20", "2025-05-30"])
    space2 = Space(id=2, name="Hobbitsville", description="A place for small people", 
                price_per_night=150.00, user_id=2, dates_booked=["2025-06-01", "2025-06-10"])

    assert space1 != space2