from .. import db
from datetime import datetime
from .enums import StatusTarefa, Categoria, Campus

class Tarefa(db.Model):
    __tablename__ = "tarefas"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.Enum(Categoria), nullable=False)
    criacao = db.Column(db.Datetime, default=datetime.utcnow, nullable=False)
    prazo = db.Column(db.Datetime, nullable=False)
    campus = db.Column(db.Enum(Campus), default="IFRN-Zona Norte")
    solicitante_id = db.Column(db.Integer, db.Foreignkey('usuario.id'),nullable=False)
    prestador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    status = db.Column(db.Enum(StatusTarefa), default=StatusTarefa.pendente, nullable=False)