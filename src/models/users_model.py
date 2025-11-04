from services.database import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable =False)
    correo = db.Column(db.String(100),nullable =False)
    edad = db.Column(db.String(100),nullable =False)
    password = db.Column(db.String(100),nullable =False)

    def __init__(self, NOMBRE, CORREO, EDAD, PASSWORD):
        self.nombre = NOMBRE
        self.correo = CORREO
        self.edad = EDAD
        self.password =PASSWORD
