from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField

#dari wtforms ( framework python untuk validasasi )
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(Form):
    # datarequire tidak membiarkan user mengkosongkan area
    #Leng minimum dan makximum pengisian text
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(),Email()] )
    password = PasswordField('password',validators=[DataRequired()] )
    confirm_password = PasswordField('confirm password',validators=[DataRequired(), EqualTo('password')] )
    submit = SubmitField('sign up')

class LoginForm(Form):

    email = StringField('email', validators=[DataRequired(),Email()] )
    password = PasswordField('password',validators=[DataRequired()] )
    remember = BooleanField('remember me')
    submit = SubmitField('login')
