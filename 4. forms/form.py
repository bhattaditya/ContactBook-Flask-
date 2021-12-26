"""
RegistrationForm and LoginForm are inheriting FlaskForm so that their objects can be created and referenced later.
"""
from  flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    """
    username (str): username will have minimum length 5 and maximum 10. It's a required field.
    email (str): entered email should be of Email type and its a required field.
    password : Password type 
    confirm_passsword: this password should be equal to above password field.
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    """
    email (str): entered email should be of Email type and its a required field.
    password : Password type 
    remember : return true if checkbox is selected otherwise returns false
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')