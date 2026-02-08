from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.schemas.usuario import UsuarioEntrada, UsuarioSaida
from app.schemas.auth import LoginSchema
from app.services.usuarios import criar_usuario
from app.services.auth import autenticar

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

usuario_saida = UsuarioSaida()

@auth_bp.post("/register")
def register():
    data = UsuarioEntrada().load(request.get_json() or {})

    usuario = criar_usuario(data)
    login_user(usuario)

    return jsonify({
        "mensagem": "Usuário criado com sucesso",
        "usuario": usuario_saida.dump(usuario)
    }), 201


@auth_bp.post("/login")
def login():
    data = LoginSchema().load(request.get_json() or {})

    usuario = autenticar(data["email"], data["senha"])
    login_user(usuario)

    return jsonify({
        "mensagem": "Login realizado",
        "usuario": usuario_saida.dump(usuario)
    }), 200


@auth_bp.post("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"mensagem": "Logout realizado"}), 200
