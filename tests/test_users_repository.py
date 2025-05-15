from lib.users_repository import UserRepository
from lib.user import User
import pytest

def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    new_user = User(None, "newuser", "new@gmail.com", "securepw!", "securepw!")
    created_user = repo.create_user(new_user)

    assert created_user.id is not None
    assert created_user.username == "newuser"
    assert created_user.email == "new@gmail.com"
    assert created_user.password == "securepw!"


# fail user attempting invalid email
def test_create_user_invalid_email(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    new_user = User(None, "newuser", "new.gmail.com", "securepw!", "securepw!")
    with pytest.raises(ValueError) as excinfo:
        repo.create_user(new_user)
        assert str(excinfo.value) == "Passwords must match"

# fail user attempting invalid password
def test_create_user_invalid_password(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    new_user = User(None, "newuser", "new@gmail.com", "securepw", "securepw")
    with pytest.raises(ValueError) as excinfo:
        repo.create_user(new_user)
    assert str(excinfo.value) == "Password must be 8 or more characters and contain at least one special character"

# fail user mismatch passwords
def test_create_user_mismatched_passwords(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    new_user = User(None, "newuser", "new@gmail.com", "securepw", "wrongpw!")
    with pytest.raises(ValueError) as excinfo:
        repo.create_user(new_user)
        assert str(excinfo.value) == "Passwords must match"


# retrieving the list of all users 
def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    users = repo.get_all_users()

    assert users == [
        User(1, "john_doe", "johndoe@gmail.com", "password123"),
        User(2, "jane_doe", "janedoe@gmail.com", "password456")
    ]

#Getting the specific user by their id
def test_get_user_by_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    user = repo.get_user(1)
    assert user == User(1, "john_doe", "johndoe@gmail.com", "password123")


# When a user is removed from the system it no longer exists
def test_remove_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    repo.remove_user(1)
    users = repo.get_all_users()

    assert users == [User(2, "jane_doe", "janedoe@gmail.com", "password456")]


#User can log in if the email and password match
def test_sign_in_success(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    user = repo.sign_in("johndoe@gmail.com", "password123")

    assert user == User(1, "john_doe", "johndoe@gmail.com", "password123")

#User unable to login as the password doesn't match
def test_sign_in_failure(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    user = repo.sign_in("johndoe@gmail.com", "wrongpw")
    assert user is None