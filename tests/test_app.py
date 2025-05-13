from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")


"""
When I request a GET method on /spaces
I get a list of spaces back.
"""
def test_get_spaces(db_connection, web_client):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    # We make a GET request to the /spaces endpoint
    get_response = web_client.get("/spaces", data={
        'spaces': 'A green lodge, Hobbitsville'
    })

    expected = (
    "space(1, Green Lodge, A lodge that is green, $100.00, 1)\n"
    "space(2, Hobbitsville, A place for small people, $200.00, 2)"
)
    assert get_response.data.decode('utf-8') == expected