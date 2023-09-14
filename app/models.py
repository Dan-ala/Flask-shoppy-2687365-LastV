from datetime import datetime;
from flask_login import UserMixin
from app import db
from app import login
from werkzeug.security import generate_password_hash,check_password_hash;

#Creación de modelos o entidades

#tabla de clientes
class Cliente(UserMixin, db.Model):
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key= True)
    username=db.Column(db.String(100), unique= True)
    email=db.Column(db.String(120), unique= True)
    password=db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, clave):
        return check_password_hash(self.password,clave)


#Con este decorador asigno de db el id del usuario que se logeo
@login.user_loader
def load_user(id):
    return Cliente.query.get(id)


#Tabla de productos

class Producto(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer, primary_key= True)
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Numeric(precision=10, scale=2))
    imagen=db.Column(db.String(100))
    
    

#Tabla de ventas

class Venta(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer, primary_key= True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    cliente_id=db.Column(db.ForeignKey('clientes.id'))
    

#Tabla detalles 
class Detalle(db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer, primary_key= True)
    producto_id=db.Column(db.ForeignKey('productos.id'))
    venta_id=db.Column(db.ForeignKey('ventas.id'))   