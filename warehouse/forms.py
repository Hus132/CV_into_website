from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    first_name = StringField('first name', validators=[DataRequired(),Length(min=2,max=50)])
    last_name = StringField('last name', validators=[DataRequired(), Length(min=2,max=50)])
    email = StringField('Email',validators=[DataRequired(),Email(),Length(max=120)])
    message = TextAreaField('message', validators=[DataRequired(),Length(max=120)])
    submit = SubmitField('Submit')