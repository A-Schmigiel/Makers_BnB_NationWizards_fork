import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
import datetime
import calendar
# helps manage secret key
from flask_bcrypt import Bcrypt
from forms import MyForm
# repositories
from lib.spaces_repository import SpaceRepository
from lib.requests_repository import RequestRepository
from lib.users_repository import UserRepository
# classes
from lib.space import Space
from lib.request import Request
from lib.user import User



# Create a new Flask app
app = Flask(__name__)


# #This is the start of the login and password security content
# #  Hardcoded secret key 
# app.config['SECRET_KEY'] = '072bb84cfdff08af0c1d8cd67f3be65bba12485bf0e9ea4dae5a49dc83260663'

# bcrypt = Bcrypt(app)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = MyForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         email = form.email.data
#         password = form.password.data

#         hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

#         if bcrypt.check_password_hash(hashed_password, password):
#             match_message = "Password hash matches input password."
#         else:
#             match_message = "Password hash did not match input."
#         return (
#             f'Hello, {username}!<br>'
#             f'Email: {email}<br>'
#             f'{match_message}'
#         )
    
#     return render_template('index.html', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)
# This is the end of the block for the login and password security content


# == Your Routes Here ==

@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app) 
    repository = SpaceRepository(connection)        
    repository.get_all_spaces()
    spaces = repository.get_all_spaces()
    return render_template('spaces.html', spaces=spaces)

@app.route('/spaces/<int:id>', methods=['GET'])
def show_listing(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.get_space(id)
    # valid_dates = [i.isoformat() for i in space.dates_available]                # <<=== still working on a solution for full integration of dates list into calendar
    return render_template('booking.html', space=space)

@app.route('/spaces/<int:id>', methods=['POST'])
def request_booking(id):
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    request_repository = RequestRepository(connection)
    space = space_repository.get_space(id)
    request_sender = 1                                      # <====  current_user.id??  requires login records? -- will need rephrased, but this allows for testing and access in the meantime.
    space_owner = space.user_id
    message_content = request.form["request_message"]
    space_requested = space.id
    dates_requested = request.form["daterange"]
    new_request = Request(None, request_sender, space_owner, message_content, space_requested, dates_requested)
    if not new_request.is_valid():
        return render_template('booking.html', request=new_request, errors=new_request.generate_errors()), 400
    request = request_repository.create_request(new_request)
    return redirect(f"/requests")


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))



