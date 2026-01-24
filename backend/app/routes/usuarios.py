from flask import Blueprint, request, jsonify
from ..schemas.usuario_schema import UsuarioEntrada, UsuarioSaida
from ..services.usuario_services import criar_usuario

usuario_bp = Blueprint("usuarios", __name__)

@usuario_bp.post("/")
def criar():
    data = UsuarioEntrada().load(request.json)
    usuario = criar_usuario(data)
    return UsuarioSaida().dump(usuario),201