from .. import db
from datetime import datetime
from .enums import StatusTarefa, Categoria, Campus

class Tarefa(db.Model):
    __tablename__ = "tarefas"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.Enum(Categoria, native_enum=False), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    prazo = db.Column(db.Datetime, nullable=False)
    campus = db.Column(db.String(100), default="IFRN-Zona Norte", nullable=False)
    solicitante_id = db.Column(db.Integer, db.ForeignKey('usuario.id'),nullable=False)
    prestador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    status = db.Column(db.Enum(StatusTarefa, native_enum=False), default=StatusTarefa.pendente, nullable=False)