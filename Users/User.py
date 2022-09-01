
# Define o objeto "Usuário"
class User:

    # O nome do usuário
    name = ""

    # O email do usuário
    email = ""

    # A TURMA que o usuário pertence
    group_id = None

    # O TIME que o usuário pertence dentro da turma
    team_id = None

    # A função do usuário no time
    role_id = None

    # Método construtor para criar um novo usuário
    def __init__(self, _name, _email, _group_id, _team_id, _role_id):

        # Ao criar um usuário, os parametros passados serão registrados ao valor das variáveis
        self.name       = _name
        self.email      = _email
        self.group_id   = _group_id
        self.team_id    = _team_id
        self.role_id    = _role_id

    # retorna uma array com as informações do usuário
    def fields(self):
        return [ self.name, self.email, self.team_id, self.role_id ]
