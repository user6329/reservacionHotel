from flask import Blueprint, render_template

bp = Blueprint('hotel', __name__, url_prefix='/hotel')

@bp.route('/')
def index():
    return 

@bp.route('/create')
def create():
    return 'Reserva'

@bp.route('/nosotros')
def Nosotros():
    return render_template('Nosotros.html')

