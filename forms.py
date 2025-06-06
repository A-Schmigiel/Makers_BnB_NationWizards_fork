from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FloatField
from wtforms.validators import DataRequired, Email
class LogInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class ListSpacesForm(FlaskForm):
    space_name = StringField('Name', validators=[DataRequired()])
    space_description = StringField('Description', validators=[DataRequired()])
    space_price_per_night = FloatField('Price Per Night e.g. £150', validators=[DataRequired()])
    space_upload_image = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CreateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(),])
    username = StringField('Username', validators=[DataRequired()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Create User')

