
# Define o objeto "Usuário"
class User:

    # O nome do usuário
    name:str = ""

    # O email do usuário
    email:str = ""

    # A TURMA que o usuário pertence
    group_id:int = None

    # O TIME que o usuário pertence dentro da turma
    team_id:int = None

    # A função do usuário no time
    role_id:int = None

    # Método construtor para criar um novo usuário
    def __init__(self, _name:str, _email:str, _group_id:int, _team_id:int, _role_id:int):

        # Ao criar um usuário, os parametros passados serão registrados ao valor das variáveis
        self.name       = _name
        self.email      = _email
        self.group_id   = _group_id
        self.team_id    = _team_id
        self.role_id    = _role_id

    def __init__(self, _fields):
        try:
            self.name       = _fields[0]
            self.email      = _fields[1]
            self.group_id   = _fields[2]
            self.team_id    = _fields[3]
            self.role_id    = _fields[4]
        except:
            print("Erro ao criar usuário")

    # retorna uma array com as informações do usuário
    def fields(self):
        return [ self.name, self.email, self.team_id, self.role_id ]

