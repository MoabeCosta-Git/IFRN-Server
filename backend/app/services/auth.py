from werkzeug.security import check_password_hash
from app.models.usuario import Usuario

def autenticar(email, senha):
    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not check_password_hash(usuario.senha, senha):
        raise ValueError("Credenciais inválidas")
    return usuario