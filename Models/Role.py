# Representa uma Função / um tipo de Usuário
class Role:

    # O nome da função
    name:str = ""

    # As permissões que esse tipo de Usuário possui 
    permissions = None
    ratings = None

    # Cria um novo tipo de Usuário
    def __init__(self, n, p, r):
        self.name = n
        self.permissions = p
        self.ratings = r

# Lista de Funções existentes
ROLES = [
    Role("ADM",             [ 0, 1, 2, ], []),

    # 1 por Grupo
    Role("Lider do Grupo",  [ 3, 4, 5, 6, 7, 8], [3]),
    Role("Cliente",         [ 9 ], [4]),

    # 1 por Time
    Role("Lider Técnico",   [8, 9, 10 ], [3, 4, 5]),
    Role("Product Owner",   [8, 9, 10 ], [3, 4, 5]),

    # 0+ por Time
    Role("Developer",       [8, 9, 10 ], [3, 4, 5])
]

# Retorna a função com id solicitado
def get_role (id:int):

    id = int(id)

    # Se o id fornecido é menor que 0 ou (maior ou igual) ao tamanho da lista de Funções: Função não existe
    if id < 0 or id >= len(ROLES):
        return None

    # Retorna a Função de index 'id'
    return ROLES[id]

# Retorna o nome da função com id solicitado
def get_role_name (id:int):
    role = get_role(int(id))
    if role is None:
        return None
    return role.name

