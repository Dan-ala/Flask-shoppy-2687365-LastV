from . import productos
from flask import render_template, redirect, flash
from .forms import NewProductForm,EditProductForm
import os 
import app

#Crear las rutas del blueprint
@productos.route('/crear', methods = ["GET", "POST"])
def crear():

    p = app.models.Producto()
    form=NewProductForm()
    if form.validate_on_submit():
        #? El Formulario Va A Llenar El Nuevo Objeto Producto Automaticamente
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        #?Ubicar El Archivo Imagen En La Carpeta app/productos/imagenes
        file=form.imagen.data
        file.save(os.path.abspath(os.getcwd()+'/app/productos/imagenes/'+p.imagen
                                  ))

        flash("Producto registrado 😎")
        #?Retorna Producto Registrado
        return redirect('/productos/listar')
    return render_template("new.html", form=form)

@productos.route('/listar')
def listar():
    #? Traer Productos De La Base De Datos
    productos = app.Producto.query.all()
    #? Mostrar La Vista De Listar Enviandole Los Productos Seleccionados
    return render_template('listar.html', productos= productos)

@productos.route('/editar/<producto_id>', methods =('GET','POST'))
def editar(producto_id):
    # seleccionar el producto con el id
    p=app.models.Producto.query.get(producto_id)
    #Cargo el formulario con los atributos del producto
    form_edit=EditProductForm(obj = p)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        flash("Producto editado exitosamente")
        return redirect("/productos/listar")

    return render_template('new.html',
                           form = form_edit)

    
@productos.route('/eliminar/<producto_id>', methods =('GET','POST'))
def eliminar(producto_id):

    p=app.models.Producto.query.get(producto_id)
    #Vamos a eliminar el producto
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Producto eliminado exitosamente")
    return redirect("/productos/listar")