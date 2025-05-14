from lib.space import Space

# Valid space with all fields
def test_space_is_valid_when_all_fields_are_present():
    space = Space(1, "Green Lodge", "A lodge that is green", 100.0, "2025-05-30", 1)
    assert space.is_valid() == True

# Invalid when name is missing
def test_space_is_invalid_when_name_is_blank():
    space = Space(1, "", "A lodge that is green", 100.0)
    assert space.is_valid() == False

# Invalid when description is missing
def test_space_is_invalid_when_description_is_blank():
    space = Space(1, "Green Cabin", "", 120.0)
    assert space.is_valid() == False

# Invalid when cost is missing
def test_space_is_invalid_when_cost_is_blank():
    space = Space(1, "Green Cabin", "A cozy green cabin", "")
    assert space.is_valid() == False

# Invalid when cost is not a positive number
def test_space_is_invalid_when_cost_is_negative():
    space = Space(1, "Green Cabin", "A cozy green cabin", -50)
    assert space.is_valid() == False

# generate_errors returns single error
def test_generate_errors_for_blank_name():
    space = Space(1, "", "A cabin", 100.0)
    assert space.generate_errors() == "Name can't be blank"

# generate_errors returns multiple errors
def test_generate_errors_for_multiple_blank_fields():
    space = Space(1, "", "", "")
    assert space.generate_errors() == "Name can't be blank, Description can't be blank, Cost must be a positive number"

# generate_errors returns None when space is valid
def test_generate_errors_returns_none_for_valid_space():
    space = Space(1, "Forest Hut", "Peaceful retreat", 150.0)
    assert space.generate_errors() is None

# Test equality between spaces
def test_spaces_are_equal_when_data_matches():
    space1 = Space(1, "Forest Hut", "Peaceful retreat", 150.0)
    space2 = Space(1, "Forest Hut", "Peaceful retreat", 150.0)
    assert space1 == space2

# Test __repr__ returns readable string
def test_space_repr_format():
    space = Space(1, "Green Cabin", "A cozy green cabin", 120.0)
    assert repr(space) == "Space(id=1, name=Green Cabin, description=A cozy green cabin, cost=120.0)"