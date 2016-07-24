from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class AuthForm(Form):
    pass_input = StringField('pass_input', validators=[DataRequired()])
    
    

class PublishForm(Form):
    text = StringField('text', validators=[DataRequired()])
    email = StringField('email')
    expirationTime = StringField('expirationTime')
    sdCounter = StringField('sdCounter')
    password = StringField('password')