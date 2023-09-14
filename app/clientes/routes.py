from . import clientes
from .forms import NewCustomerForm,EditClienteForm
from flask import render_template,flash,redirect,flash
import app

@clientes.route('/crear', methods=["GET","POST"])
def crear():
    c=app.models.Cliente()
    form=NewCustomerForm()
    if form.validate_on_submit():
        #Aquí el objeto llena el form
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
        flash("Cliente registrado 😎")
        return redirect('/clientes/listar')
    return render_template("newCustomers.html", form=form)

@clientes.route('/listar')
def listar():
    #Traernos los clientes de la db
    clientes = app.Cliente.query.all()
    #Mostramos los clientes a través de una lista solo los clientes seleccionados por la consulta
    return render_template('lis.html',
                           clientes=clientes)



@clientes.route('/editar/<cliente_id>', methods =('GET','POST'))
def editar_cliente(cliente_id):
    # seleccionar el producto con el id
    c=app.models.Cliente.query.get(cliente_id)
    #Cargo el formulario con los atributos del producto
    form_edit=EditClienteForm(obj = c)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(c)
        app.db.session.commit()
        flash("Cliente editado exitosamente")
        return redirect("/clientes/listar")

    return render_template('newCustomers.html',
                           form = form_edit)

    
@clientes.route('/eliminar/<cliente_id>', methods =('GET','POST'))
def eliminar(cliente_id):

    c=app.models.Cliente.query.get(cliente_id)
    #Vamos a eliminar el producto
    app.db.session.delete(c)
    app.db.session.commit()
    flash("Cliente eliminado exitosamente")
    return redirect("/clientes/listar")