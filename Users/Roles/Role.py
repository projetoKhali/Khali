
# Representa uma Função / um tipo de Usuário
from random import getrandbits


class Role:

    # O nome da função
    name:str = ""

    # As permissões que esse tipo de Usuário possui 
    permissions = None

    # Cria um novo tipo de Usuário
    def __init__(self, n, p):
        self.name = n
        self.permissions = p

# Lista de Funções existentes
ROLES = [
    Role("ADM", { }),

    # 1 por Grupo
    Role("Lider do Grupo", { }),
    Role("Cliente", { }),

    # 1 por Time
    Role("Lider Técnico", { }),
    Role("Product Owner", { }),

    # 0+ por Time
    Role("Developer", { })
]

# Retorna a função com id solicitado
def get_role (id:int):

    # Se o id fornecido é menor que 0 ou (maior ou igual) ao tamanho da lista de Funções: Função não existe
    if id < 0 or id >= len(ROLES):
        return None

    # Retorna a Função de index 'id'
    return ROLES[id]

# Retorna o nome da função com id solicitado
def get_role_name (id:int):
    role = get_role(id)
    if role is None:
        return None
    return role.name

