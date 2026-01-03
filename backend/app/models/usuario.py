from app import db
from datetime import datetime
from .enums import Perfil

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    perfil = db.Column(db.Enum(Perfil), nullable=False)