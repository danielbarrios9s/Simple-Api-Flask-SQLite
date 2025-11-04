from flask import Flask
from blueprints.blueprints_users import users_bp
from services.database import db


def create_app():
    app = Flask(__name__)

    """Configuracion de la base de datos"""
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
    
    """Instancia de la base de datos """
    db.init_app(app) 
    with app.app_context():
        db.create_all()  # crea las tablas al iniciar
           
    #registro de los blue prints 
    app.register_blueprint(users_bp)

    return app

"""Generamos un punto de acceso a la aplicacion en el puerto 5000"""

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
    