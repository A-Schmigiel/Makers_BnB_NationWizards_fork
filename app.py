import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from dotenv import load_dotenv  # helps manage secret key
from flask_bcrypt import Bcrypt
from forms import MyForm 

# Create a new Flask app
app = Flask(__name__)


#This is the start of the login and password security content
#  Hardcoded secret key 
app.config['SECRET_KEY'] = '072bb84cfdff08af0c1d8cd67f3be65bba12485bf0e9ea4dae5a49dc83260663'

bcrypt = Bcrypt(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        if bcrypt.check_password_hash(hashed_password, password):
            match_message = "Password hash matches input password."
        else:
            match_message = "Password hash did not match input."
        return (
            f'Hello, {username}!<br>'
            f'Email: {email}<br>'
            f'{match_message}'
        )
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
# This is the end of the block for the login and password security content


# == Your Routes Here ==

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



