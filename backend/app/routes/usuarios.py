from flask import Blueprint, request, jsonify
from app.schemas.usuario import UsuarioEntrada, UsuarioSaida, UsuarioUpdateSchema
from app.services.usuarios import criar_usuario
from flask_login import login_required, current_user
from app.extensions import db

usuario_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")

usuario_saida = UsuarioSaida()

@usuario_bp.get("/me")
@login_required
def me():
    return jsonify(usuario_saida.dump(current_user)), 200

@usuario_bp.patch("/me")
@login_required
def atualizar_me():
    data = UsuarioUpdateSchema().load(request.get_json() or {})
    current_user.nome = data["nome"]
    db.session.commit()
    return jsonify(usuario_saida.dump(current_user)), 200