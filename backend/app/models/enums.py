import enum

class StatusTarefa(enum.Enum):
    pendente = "Pendente"
    em_andamento = "Em andamento"
    concluido = "Concluído"

class Categoria(enum.Enum):
    preventiva = "Manutenção preventiva"
    defeito = "Defeito/Mal funcionamento"

class Perfil(enum.Enum):
    solicitante = "Solicitante"
    prestador = "Prestador"
    admin = "Administrador"