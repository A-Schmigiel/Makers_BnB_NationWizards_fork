import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import SpaceRepository
# helps manage secret key
from flask_bcrypt import Bcrypt
from forms import MyForm
# repositories
from lib.spaces_repository import Space
from lib.requests_repository import Request
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
    connection = get_flask_database_connection(app)                # <-- New code!
    repository = SpaceRepository(connection)                        # <-- New code!
    repository.get_all_spaces()
    spaces = repository.get_all_spaces()
    return "\n".join(str(space) for space in spaces)
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




#############################################################

# import os
# from flask import Flask, request, render_template
# from lib.database_connection import get_flask_database_connection
# from dotenv import load_dotenv  # helps manage secret key
# from flask_bcrypt import Bcrypt
# from forms import MyForm 
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin

# from lib.users_repository import userRepository
# from lib.user import User 

# # Testing code below
# # Setting up app
# load_dotenv() 
# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev-secret")

# bcrypt = Bcrypt(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

# # password = 'mysecretpassword'
# # hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

# # Flask login setup
# @login_manager.user_loader
# def load_user(user_id):
#     db = get_flask_database_connection()
#     repo = userRepository(db)
#     try:
#         return repo.get_user(int(user_id))
#     except:
#         return None
    
# #Forms

# class LoginForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     submit = SubmitField("Login")

# #Routes
# @app.route("/", methods=["GET"])
# def root():
#     return redirect(url_for("login"))

# @app.route("/index", methods=["GET"])
# @login_required
# def get_index():
#     return render_template("index.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         db = get_flask_database_connection()
#         repo = userRepository(db)
#         user = repo.sign_in(form.email.data, form.password.data)
#         if user:
#             login_user(user)
#             flash("Logged in successfully.", "success")
#             return redirect(url_for("get_index"))
#         else:
#             flash("Invalid email or password.", "danger")
#     return render_template("login.html", form=form)

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     flash("You have been logged out.", "info")
#     return redirect(url_for("login"))

# # #This is the start of the login and password security content
# # #  Hardcoded secret key 

# # These lines start the server if you run this file directly
# # They also start the server configured to use the test database
# # if started in test mode.
# if __name__ == '__main__':
#     app.run(debug=True, port=int(os.environ.get('PORT', 5001)))



