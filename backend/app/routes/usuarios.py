from flask import Blueprint, request, jsonify
from app.schemas.usuario import UsuarioEntrada, UsuarioSaida
from app.services.usuarios import criar_usuario

usuario_bp = Blueprint("usuarios", __name__)

@usuario_bp.post("/")
def criar():
    data = UsuarioEntrada().load(request.json)
    usuario = criar_usuario(data)
    return UsuarioSaida().dump(usuario),201