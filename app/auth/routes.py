from . import auth
from flask import render_template, redirect, flash
from .forms import LoginForm
import app

#Dependencia para auth
from flask_login import current_user, login_user, logout_user

#Primera ruta: Login
@auth.route('/login',
            methods = ['GET','POST'])
def login():
    f = LoginForm()
    if f.validate_on_submit():
        #Vamos a seleccionar el cliente con el username
        c=app.models.Cliente.query.filter_by(username = f.username.data).first()
        if c is None or not c.check_password(f.password.data):
            flash('No mano!')
            return redirect('/auth/login')

        else:
            login_user(c,True)
            flash('Welcome!')
            return redirect('/productos/listar')
    return render_template ('login.html',
                        f=f)


#Segunda ruta: Logout
@auth.route('/logout', 
            methods = ['GET'])
def logout():
    logout_user()
    return redirect('/auth/login')