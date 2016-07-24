from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class AuthForm(Form):
    pass_input = StringField('pass_input', validators=[DataRequired()])
    

class PublishForm(Form):
    text = TextAreaField('text', validators=[DataRequired()])
    email = StringField('email')
    expiration_time = IntegerField('expiration_time')
    sdCounter = StringField('sdCounter')
    password = StringField('password')