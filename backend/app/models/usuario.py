from app.extensions import db
from app.models.enums import Perfil

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    perfil = db.Column(db.Enum(Perfil, native_enum=False), nullable=False)
