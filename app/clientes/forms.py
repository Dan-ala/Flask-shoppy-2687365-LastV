from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import InputRequired,DataRequired,Email

class ClienteForm():
    username = StringField('Ingrese un usuario: ',
                           validators=[InputRequired(message="Debe ingresar un usuario!")])
    email = EmailField('Email address', [DataRequired(), Email(message='Ingrese su Email correctamente')])


class NewCustomerForm(FlaskForm,ClienteForm):
    password = PasswordField('Ingrese una contraseña: ',
                              validators=[InputRequired(message="Debe registar una contraseña")])
   
    submit = SubmitField('Registar')

class EditClienteForm(FlaskForm,ClienteForm):
    submit = SubmitField('Registrar')