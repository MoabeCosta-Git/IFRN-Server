from app import db
from datetime import datetime
from .enums import StatusTarefa, Categoria, Campus

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    categoria = db.Column(db.Enum(Categoria), nullable=False)
    criacao = db.Column(db.Datetime, default=datetime.utcnow, nullable=False)
    prazo = db.Column(db.Datetime, nullable=False)
    campus = db.Column(db.Enum(Campus))
    solicitante_id = db.Column(db.Integer, db.Foreignkey('usuario.id'),nullable=False)
    prestador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    status = db.Column(db.Enum(StatusTarefa), default=StatusTarefa.pendente, nullable=False)