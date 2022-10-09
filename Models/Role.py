# Representa uma Função / um tipo de Usuário
class Role:
    
    # Cria um novo tipo de Usuário
    def __init__(self, _name, _permissions_reg, _permissions_rate, _permissions_view=None):
        self.name = _name
        self.permissions_reg = _permissions_reg
        self.permissions_rate = _permissions_rate
        self.permissions_view = _permissions_view

# Lista de Funções existentes
ROLES = [
    #       permissions:         REG              RATE
    Role("ADM",             [0, 1, 2      ], [             ]),

    # 1 por Grupo
    Role("Líder do Grupo",  [3, 4, 5, 6, 7], [3            ]),
    Role("Cliente",         [             ], [4            ]),

    # 1 por Time
    Role("Líder Técnico",   [             ], [3, 4, 5      ]),
    Role("Product Owner",   [             ], [3, 4, 5      ]),

    # 0+ por Time
    Role("Developer",       [             ], [3, 4, 5      ])
]

# Retorna a função com id solicitado
def get_role (id:int):

    id = int(id)

    # Se o id fornecido é menor que 0 ou (maior ou igual) ao tamanho da lista de Funções: Função não existe
    if id < 0 or id >= len(ROLES):
        return None

    # Retorna a Função de index 'id'
    return ROLES[id]

def get_role_id (name:str):
    for i, role in enumerate(ROLES):
        if role.name == name:
            return i
    return None

# Retorna o nome da função com id solicitado
def get_role_name (id:int):
    role = get_role(int(id))
    if role is None:
        return None
    return role.name

