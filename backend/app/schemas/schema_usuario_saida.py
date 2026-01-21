from .. import ma
from ..models.usuario import Usuario

class UsuarioSaida(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        fields = ("id", "nome", "email", "perfil")