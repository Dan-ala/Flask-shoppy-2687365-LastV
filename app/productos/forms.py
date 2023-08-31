from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired,NumberRange


class NewProductForm(FlaskForm):
    nombre = StringField('Ingrese producto: ',
                         validators=[InputRequired(message="uyyy mano paila")])
    precio = IntegerField('Ingrese precio:',validators= [InputRequired(message="Precio Requerido"),NumberRange(message="Manooo muy alto el precio",min=10000, max=100000)])
    imagen=FileField(validators=[FileRequired
                                 (message="Mano suba una imagen!!  .°.😂😂"),
                                 FileAllowed([ 'jpg','png'],
                                 message="Solo se admiten imagenes"
                                 )] ,
                                 label="Ingrese una imagene")
    submit = SubmitField('Registrar')