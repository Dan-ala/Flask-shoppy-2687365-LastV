from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField(label='Nombre usuario ',
                           validators=[InputRequired(message="Nombre requerido")])
    
    password = PasswordField(label='Password',
                             validators=[InputRequired(message='Password requerida')])
    
    submit = SubmitField("Login")