from app.extensions import db
from app.models.tarefa import Tarefa
from app.models.enums import StatusTarefa, Categoria
from datetime import datetime

def criar_tarefa(data, usuario_id):
    prazo = data["prazo"]

    tarefa = Tarefa(
        titulo=data["titulo"],
        descricao=data["descricao"],
        categoria=Categoria[data["categoria"]],
        prazo=datetime.combine(prazo, datetime.min.time()),
        solicitante_id=usuario_id,
        status=StatusTarefa.pendente
    )
    db.session.add(tarefa)
    db.session.commit()
    return tarefa

def aceitar_tarefa(tarefa, usuario_id):
    if tarefa.prestador_id:
        raise ValueError("Tarefa já aceita")
    
    if tarefa.solicitante_id == usuario_id:
        raise ValueError("Você não pode aceitar sua própria tarefa")

    tarefa.prestador_id = usuario_id
    tarefa.status = StatusTarefa.em_andamento
    db.session.commit()
    return tarefa

