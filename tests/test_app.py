from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("This is the homepage.")

#===TESTS FOR /SPACES===
"""
When I request a GET method on /spaces
I get a list of spaces back.
"""
def test_get_spaces(test_web_address, page, db_connection):
    db_connection.seed("seeds/makersbnb.sql")  # changed the seed file name after making single seed file for all tables
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/spaces")
    h5_tags = page.locator("h5")
    expect(h5_tags).to_have_text(["Green Lodge", "Hobbitsville"])

# def test_create_user()
    
#===TESTS FOR /LISTSPACE===










#===TESTS FOR /LOGIN===
"""
When I log in with valid credentials
I am redirected to the /spaces page
"""
def test_login_success(test_web_address, page, client, db_connection):
    # Seed the database with a user whose password is 'password123'
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/login")
    response = client.post(
        "/login",
        data={"username": "john_doe", "password": "password123"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    






##===TESTS FOR /LOGOUT===