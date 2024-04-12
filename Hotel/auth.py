from flask import Blueprint, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from . import models



bp = Blueprint('auth','static', 'styles', __name__, url_prefix='/auth')

#Crear Formulario 
class RegistrarForm(FlaskForm):
    username =StringField("Nombre de Usuario: ")
    password =StringField("Password: ")
    submit =SubmitField("Registrar: ")


#Registrar Usuario
@bp.route('/register', methods =['GET', 'POST'])
def register():
    form = RegistrarForm
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        if len(username) >= 4 and len(username) <= 25 and password == password and len(password) >=8:
            return render_template('auth/Register.html')

        else:
            error = "Nombre de Usuario o Contraseña no Validos "

            return render_template('auth/Register.html', error = error)
        
    return render_template('auth/Register.html', form = form)

@bp.route('/login')
def login():
    return render_template('auth/login.html')

