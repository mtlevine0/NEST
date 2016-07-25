from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired

class AuthForm(Form):
    password = PasswordField('password', validators=[DataRequired()])
    

class PublishForm(Form):
    myChoices = [15, 30, 45, 60]
    
    text = TextAreaField('text', validators=[DataRequired()])
    email = StringField('email')
    expiration_time = SelectField('expiration_time', choices=[(f, f) for f in myChoices])
    sdCounter = StringField('sdCounter')
    password = PasswordField('password')