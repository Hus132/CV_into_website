from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField  #to allow string fields in the form
from wtforms.validators import DataRequired, Length, Email, EqualTo #to import the validation requirements


#registration form
#validators is a list of required conditions to be met.
class RegistrationForm(FlaskForm): #inherits from Flaskform
    username= StringField('Username',
                          validators=[DataRequired(),Length(min=2,max=20)]) #
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField("password",validators=[DataRequired()])
    confirm_password = PasswordField("confirm password",
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

#login form
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField("password",validators=[DataRequired()])
    remember = BooleanField('Remember me')
    confirm_password = PasswordField("confirm password",
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField ('Login in')