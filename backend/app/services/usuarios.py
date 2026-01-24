from app.extensions import db
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash

def criar_usuario(data):
    if Usuario.query.filter_by(email=data["email"]).first():
        raise ValueError("E-mail já cadastrado")

    usuario = Usuario(
        nome=data["nome"],
        email=data["email"],
        senha=generate_password_hash(data["senha"]),
        perfil=data["perfil"]
    )

    db.session.add(usuario)
    db.session.commit()
    
    return usuario

