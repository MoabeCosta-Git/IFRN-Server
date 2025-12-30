import enum

class StatusTarefa(enum.Enum):
    pendente = "Pendente"
    em_andamento = "Em andamento"
    concluido = "Concluído"

class Categoria(enum.Enum):
    preventiva = "Manutenção preventiva"
    defeito = "Defeito/Mal funcionamento"

class Campus(enum.Enum):
    zn = "IFRN-Zona Norte"