from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class SignUp(FlaskForm):
    first_name = StringField("First Name", 
                            validators=[DataRequired()])
    last_name = StringField("Last Name", 
                            validators=[DataRequired()])
    preferred_name = StringField("Preferred Name")
    
    email = StringField("Email", 
                        validators=[DataRequired(), Email(granular_message=True)])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

class Login(FlaskForm):
    email = StringField("Email", 
                        validators=[DataRequired(), Email(granular_message=True)])
    password = PasswordField('Password',
                             validators=[DataRequired()]) #EQUAL TO SQL Query for password
    submit = SubmitField('Login')
    