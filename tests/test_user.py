from lib.user import User

#checking if it is a valid user
def test_user_is_valid_when_all_fields_are_present():
    user = User(1, "john_doe", "johndoe@gmail.com", "password123")
    assert user.is_valid() == True

#invalid when username is missing
def test_user_is_invalid_when_username_is_blank():
    user = User(1, "", "johndoe@gmail.com", "password123")
    assert user.is_valid() == False

# invalid when email is missing
def test_user_is_invalid_when_email_is_blank():
    user = User(1, "john_doe", "", "password123")
    assert user.is_valid() == False

# invalid when password is missing
def test_user_is_invalid_when_password_is_blank():
    user = User(1, "john_doe", "johndoe@gmail.com", "")
    assert user.is_valid() == False

# generate_errors returns single error
def test_generate_errors_for_blank_username():
    user = User(1, "", "test@gmail.com", "password")
    assert user.generate_errors() == "username can't be blank"

# generate_errors for multiple fields
def test_generate_errors_for_multiple_blank_fields():
    user = User(1, "", "", "")
    assert user.generate_errors() == "username can't be blank, email can't be blank, password can't be blank"

# generate_errors returns None for valid user
def test_generate_errors_returns_none_for_valid_user():
    user = User(1, "jane_doe", "janedoe@gmail.com", "password456")
    assert user.generate_errors() is None

# Test equality between users
def test_users_are_equal_when_data_matches():
    john_doe = User(1, "john_doe", "a@a.com", "password123")
    user2 = User(1, "john_doe", "a@a.com", "password123")
    assert john_doe == user2

#Test __repr__ returns readable string
def test_user_repr_format():
    user = User(1, "john_doe", "a@a.com", "password123")
    assert repr(user) == "user(1, john_doe, a@a.com, password123)"