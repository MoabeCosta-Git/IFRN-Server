from app.extensions import db
from app.models.tarefa import Tarefa
from app.models.enums import StatusTarefa

def criar_tarefa(data, usuario_id):
    tarefa = Tarefa(
        **data,
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

