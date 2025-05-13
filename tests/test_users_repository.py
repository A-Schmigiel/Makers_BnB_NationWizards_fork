from lib.users_repository import userRepository
from lib.user import User

"""
We can render the index page
"""
def test_add_and_get(db_connection):
    db_connection.seed("seeds/users.sql")
    repo = userRepository(db_connection)
    user = repo.all()
    assert user == [
        User (1, 'abc@abc.com', 'password1'),
        User (2, 'def@abc.com', 'password2')
    ]