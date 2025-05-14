from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FloatField
from wtforms.validators import DataRequired, Email

class MyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class ListSpacesForm(FlaskForm):
    space_name = StringField('Name', validators=[DataRequired()])
    space_description = StringField('Description', validators=[DataRequired()])
    space_price_per_night = FloatField('Price Per Night', validators=[DataRequired()])
    submit = SubmitField('Submit')

