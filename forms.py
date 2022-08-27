from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class SignUp1(FlaskForm):
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
    submit = SubmitField('Submit')

class SignUp2(FlaskForm):
    noOfUnits = SelectField("Number of units", choices=[1, 2, 3, 4, 5],
                            validators=[DataRequired()])
    course = StringField("Degree/Course", validators=[DataRequired()])
    faculty = SelectField("Faculty", 
                        choices = [
                                    "Faculty of Arts and Social Sciences",
                                    "Faculty of Engineering",
                                    "Faculty of Medicine and Health",
                                    "Faculty of Science",
                                    "School of Architecture, Design and Planning",
                                    "University of Sydney Business School",
                                    "Conservatorium of Music",
                                    "Sydney Law Music"
                                ],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')

class SignUp3(FlaskForm):
    unit1 = StringField("Unit 1", validators=[DataRequired()])
    unit2 = StringField("Unit 2", validators=[DataRequired()])
    unit3 = StringField("Unit 3", validators=[DataRequired()])
    unit4 = StringField("Unit 4", validators=[DataRequired()])
    unit5 = StringField("Unit 5", validators=[DataRequired()])
    submit = SubmitField('Submit')

class Login(FlaskForm):
    email = StringField("Email", 
                        validators=[DataRequired(), Email(granular_message=True)])
    password = PasswordField('Password',
                             validators=[DataRequired()]) #EQUAL TO SQL Query for password
    submit = SubmitField('Login')
    
