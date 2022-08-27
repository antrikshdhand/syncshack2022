from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SignUp(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired])
    last_name = StringField("Last Name", validators=[DataRequired])
    preferred_name = StringField("Preferred Name")
    email = StringField("Email")