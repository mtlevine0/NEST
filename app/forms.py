from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class AuthForm(Form):
    pass_input = StringField('pass_input', validators=[DataRequired()])
    uid = StringField('uid_input', validators=[DataRequired()])
