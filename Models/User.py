from CSV.CSVHandler import *
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
    def __init__(self, _name:str, _email:str, _group_id:int, _team_id:int, _role_id:int, _pw:str, _id:int=None):

        # Ao criar um usuário, os parametros passados serão registrados ao valor das variáveis
        self.id         = _id
        self.name       = _name
        self.email      = _email
        self.group_id   = _group_id
        self.team_id    = _team_id
        self.role_id    = _role_id
        self.password   = _pw

# Converte um dicionario em objeto da classe User
def to_user(user_data):
    return User(
        user_data['name'],
        user_data['email'],
        (lambda x: int(x) if x is not '' else x)(user_data['group_id']),
        (lambda x: int(x) if x is not '' else x)(user_data['team_id']),
        (lambda x: int(x) if x is not '' else x)(user_data['role_id']),
        user_data['password'],
        (lambda x: int(x) if x is not '' else x)(user_data['id']),
    )

# Cria um Usuário e salva na database
def create_user (name, email, group_id, team_id, role_id, password):
    return add_unique_csv_autoid(USERS_PATH, [name, email, group_id, team_id, role_id, password])

# retorna o Usuário que corresponde ao id especificado 
def get_user (id:int):
    return to_user(find_data_by_id_csv(USERS_PATH, int(id)))

# Retorna todos os Usuários to time especificado
def get_users_of_team (team_id):
    return [to_user(x) for x in find_data_list_by_field_value_csv(USERS_PATH, 'team_id', team_id)]

# Retorna todos os Usuários to grupo especificado
def get_users_of_group (group_id):
    return [to_user(x) for x in find_data_list_by_field_value_csv(USERS_PATH, 'group_id', group_id)]


