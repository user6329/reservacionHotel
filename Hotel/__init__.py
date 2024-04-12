from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    #configuracion de todo el Proyecto 
    app.config.from_mapping(
        DEBUG = True,
        SECRETE_KEY = 'DEV',
        SQLALCHEMY_DATABASE_URI = "sqlite:///Hotellist.db"
    )


    db.init_app(app)

    #Registrar Blueprint
    from . import hotel
    app.register_blueprint(hotel.bp)

    from . import auth
    app.register_blueprint(auth.bp,)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/nosotros')
    def Nosotros():
        return render_template('Nosotros.html')
    


    #migrar la base datos 
    with app.app_context():
        db.create_all()
    
    return app
    
