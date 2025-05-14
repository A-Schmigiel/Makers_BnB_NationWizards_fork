from lib.spaces_repository import SpaceRepository
from lib.space import Space
from datetime import date

def test_create_space(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)

    new_space = Space(None, "new_space", "new_description","100.00", 1, ['2025-10-25', '2025-10-30'])
    created_space = repo.create_space(new_space)

    assert created_space.id is not None
    assert created_space.name == "new_space"
    assert created_space.description == "new_description"
    assert created_space.price_per_night == "100.00"
    assert created_space.user_id == 1
    assert created_space.dates_booked == ['2025-10-25', '2025-10-30']
    

# retrieving the list of all spaces 
def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)

    spaces = repo.get_all_spaces()

    assert spaces == [
        Space(1, 'Green Lodge', 'A lodge that is green', 100.00, 1, [date(2025, 5, 20), date(2025, 5, 30)]),
        Space(2, 'Hobbitsville', 'A place for small people', 200.00, 2, [date(2025, 6, 1), date(2025, 6, 10)])
    ]

#Getting the specific space by their id
def test_get_space_by_id(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)

    spaces = repo.get_space(1)
    assert spaces == Space(1, 'Green Lodge', 'A lodge that is green', 100.00, 1, [date(2025, 5, 20), date(2025, 5, 30)])


# When a space is removed from the system it no longer exists
def test_remove_space(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)

    repo.remove_space(1)
    spaces = repo.get_all_spaces()

    assert spaces == [Space(2, 'Hobbitsville', 'A place for small people', 200.00, 2, [date(2025, 6, 1), date(2025, 6, 10)])]


# when booking a space
def test_book_space(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)

    repo.book_space(1, date(2025, 6, 15))
    updated_space = repo.get_space(1)

    assert date(2025, 6, 15) in updated_space.dates_booked