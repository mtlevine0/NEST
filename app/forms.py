from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class AuthForm(Form):
    pass_input = StringField('pass_input', validators=[DataRequired()])
