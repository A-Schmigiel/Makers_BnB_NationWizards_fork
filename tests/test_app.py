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
    # Seed test data
    db_connection.seed("seeds/makersbnb.sql")

    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name='username']", "john_doe")
    page.fill("input[name='password']", "password123")
    page.click("button[type='submit']")
    page.wait_for_url(f"http://{test_web_address}/spaces") 

    page.goto(f"http://{test_web_address}/spaces")
    h5_tags = page.locator("h5")
    expect(h5_tags).to_have_text(["Green Lodge", "Hobbitsville"])

    
#===TESTS FOR /LISTSPACE===

# def test_list_spaces_success(web_client, db_connection):
#     db_connection.seed("seeds/makersbnb.sql")

#     login_response = web_client.post(
#         "/login",
#         data={"username": "john_doe", "password": "password123"},
#         follow_redirects=True,
#     )

#     print(login_response.data.decode())  # See if it contains login errors

#     assert login_response.status_code == 200
#     assert b"Spaces" in login_response.data

#===TESTS FOR /LOGIN===
"""
When I log in with valid credentials
I am redirected to the /spaces page
"""
def test_login_success(test_web_address, page, web_client, db_connection): # <- this needs to be web_client instead of client-- refer to conftest.py
    # Seed the database with a user whose password is 'password123'
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/logindb_connection")
    response = web_client.post(
        "/login",
        data={"username": "john_doe", "password": "password123"},
        follow_redirects=True,
    )
    assert response.status_code == 200

#Invalid login tests

# def test_login_failure(web_client, db_connection):
#     # Seed the database with a known user
#     db_connection.seed("seeds/makersbnb.sql")

#     # Attempt to log in with an incorrect password
#     response = web_client.post(
#         "/login",
#         data={"username": "john_doe", "password": "wrongpassword"},
#         follow_redirects=True,
#     )

#     # Check that the login failed gracefully
#     assert response.status_code == 200  # Should stay on login page
#     assert b"Invalid credentials" in response.data
    
# ##===TESTS FOR /LOGOUT===
def test_logout_success(web_client, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    
    response = web_client.post(
        "/login",
        data={"username": "john_doe", "password": "password123"},
        follow_redirects=True,
    )
    
    assert response.status_code == 200
    
    response = web_client.get('/logout', follow_redirects=True)
    
    assert response.status_code == 200 
    assert b"Log in" in response.data 
    assert response.request.path == '/login'