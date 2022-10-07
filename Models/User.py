
from Settings import USERS_PATH

# Define o objeto "Usuário"
class User:

    id:int       = ""
    name:str     = ""       # O nome do usuário
    email:str    = ""       # O email do usuário
    group_id:int = None     # A TURMA que o usuário pertence
    team_id:int  = None     # O TIME que o usuário pertence dentro da turma
    role_id:int  = None     # A função do usuário no time
    password:int = None     # A senha criptografada do usuário

    # Método construtor para criar um novo usuário
    def __init__(self, _id, _name:str, _email:str, _group_id:int, _team_id:int, _role_id:int, _pw:str):

        # Ao criar um usuário, os parametros passados serão registrados ao valor das variáveis
        self.id         = _id
        self.name       = _name
        self.email      = _email
        self.group_id   = _group_id
        self.team_id    = _team_id
        self.role_id    = _role_id
        self.password   = _pw

# Cria um Usuário e salva na database
def create_user (name, email, group_id, team_id, role_id, password):
    from CSV.CSVHandler import add_unique_csv_autoid
    return add_unique_csv_autoid(USERS_PATH, [name, email, group_id, team_id, role_id, password])