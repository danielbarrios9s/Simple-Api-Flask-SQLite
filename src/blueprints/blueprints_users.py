import sys
sys.path.append("src/models")

from flask import Blueprint, request, jsonify
from models.users_model import Users
from services.database import db

users_bp = Blueprint("users",__name__, url_prefix="/users") #creamos una instacia de la clase Blueprint
usuario_prueba= Users("daniel","daniel@gmail.com","13","daniel123")
"""RUTAS CONTENIDAS DENTRO DEL BLUE PRINT"""

@users_bp.route("/", methods=["GET"])
def list_users():
    """devolver un arrego en formato json con todos los usuarios y su id"""
    try:
        users = Users.query.all()
        return jsonify([{"nombre": u.nombre, "correo": u.correo, "edad": u.edad} for u in users]), 200
    except Exception as e:
        return jsonify({"status":"error", 
                        "error message":str(e)}), 500

@users_bp.route("/validateUser", methods=["GET","POST"])
def validate_user():
    """validar si el suario esta en la base de datos y tiene credenciales correctas"""
    return jsonify({"mensaje":"usuario validado"}), 200

@users_bp.route("/newuser", methods=["GET","POST"])
def create_user():
    """Recibir un json con la informacion del usuario y devolver un json con un mensaje de validacion y conogo http """
    return jsonify({"mensaje":"usuario registrado"}), 200

@users_bp.route("/deleteuser", methods=["GET","POST"])
def delete_user():
    """Recibir un json con la informacion del usuario y en caso de que exista eliminarlo retonar JSON con mensaje y http code"""
    return jsonify({"mensaje":"Usuario eliminado"}), 200

@users_bp.route("/seed", methods=["GET"])
def seed_users():
    try:
        user1 = Users("Carlos", "carlos@ejemplo.com", "34", "1234")
        user2 = Users("Lucía", "lucia@ejemplo.com", "34", "abcd")
        
        db.session.add_all([user1, user2])
        db.session.commit()
        
        return jsonify({"message": "Usuarios de ejemplo agregados"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

