from flask import Flask, render_template;
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy;
from flask_migrate import Migrate;
#El punto es para archivo en la mis a carpet
from .config import Config
from .mi_blueprint import mi_blueprint
from app.productos import productos
from flask_bootstrap import Bootstrap
from app.clientes import clientes
from app.auth import auth


#Creacón y configuración de la app

#Creación del objeto
app = Flask(__name__)

#Para definir a que base de datos nos vamos a conectar
app.config.from_object(Config)
bootstrap= Bootstrap(app)
login = LoginManager(app)

#Configurar y registrar blueprints
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)
app.register_blueprint(clientes)
app.register_blueprint(auth)

#Establecer una configuración para sql admin
#Crear los objetos de sqlalchemy y migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import Producto, Venta, Cliente, Detalle


@app.route("/prueba")
def funcionprueba():
    return render_template("prueba.html")