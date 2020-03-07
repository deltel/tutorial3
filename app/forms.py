from flask_wtf import Form 
from wtforms.fields import TextField
from wtforms.validators import DataRequired, Email

class EmailPasswordForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])