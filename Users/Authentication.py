
# Insira imports aqui para utilizá-los sem incluir no namespace (ao importar Users, NÃO importará também estes imports)
from CSV.CSVHandler import *
from Users.User import User

import Settings as settings
from .Roles.Role import *

#region Users

# TODO: global current_user

# TODO: Login method

# Efetua o Cadastro de um novo Usuário e, se efetuado com sucesso, o armazena na database .csv
def register (name, email, group_id, team_id, role_id):

    # Verifica se o nome do Usuário é válido
    if not validate_user_name(name):
        print('Erro ao cadastrar usuario: Nome fornecido não é válido')
        return

    # Verifica se o email fornecido é valido
    if not validate_user_email(email):
        print('Erro ao cadastrar usuario: Email fornecido não é válido')
        return

    # TODO: validate_group_id
    if not exists_group(group_id):
        print(f'Erro: grupo de id {group_id} não existe')
        return

    # TODO: validate_team_id
    if not exists_team(team_id):
        print(f'Erro: time de id {team_id} não existe')
        return

    # TODO: validate_role_id
    if not exists_role(role_id):
        print(f'Erro: função de id {role_id} não existe')
        return

    # 🤔 is this really needed?
    user = User(name, email, group_id, team_id, role_id)

    # Adiciona o usuário para a database
    add_line_csv(settings.USERS_PATH, get_user_fields(user))


# Retorna uma lista com as informações de um Usuário
def get_user_fields (user:User):
    return list({
        user.name,
        user.email,
        get_group_name(user.group_id),
        get_team_name(user.team_id),
        get_role(user.role_id)
    })

#endregion

#region User Register Validation

# Retorna True se o nome especificado é valido e False se não
def validate_user_name(name:str):

    # Nome fornecido é INVALIDO se descumprir pelo menos uma das seguintes condições:
    # Numero de caracteres é maior ou igual ao minimo predefinido -> USER_NAME_MIN_MAX[0] 
    # Numero de caracteres é menor que o maximo predefinido       -> USER_NAME_MIN_MAX[1]
    if len(name) < settings.USER_NAME_MIN_MAX[0] or len(name) >= settings.USER_NAME_MIN_MAX[1]:
        return False

    # Cria uma variavel string para armazenar o caractere anterior no proximo loop
    last_char = ""

    # Pra cada caractere no nome fornecido
    for char in name:

        # Se o caractere atual não for uma letra
        if not char.isalpha():

            # Se o caractere atual for um espaço 
            if char == " ":

                # Se o caractere anterior tambem for um espaço
                if char == last_char:

                    # Nome invalido
                    return False

                # Caractere anterior não é espaço, caractere atual é valido
                continue

            # Caractere atual não é letra e não é espaço, nome invalido
            return False

        # Caractere é letra

    # Saiu do loop sem encontrar nenhum caractere invalido, consequentemente, o nome é valido
    return True



# Retorna True se o email especificado é valido e False se não
def validate_user_email(email:str):

    # Importa (localmente dentro do escopo da função) a biblioteca 're' 
    # que corresponde a funcionalidade de regex (Regular Expressions)
    import re

    # Define o padrão regex a ser comparado: Deve conter exatamente um '@' e um '.' após o '@'
    email_regex_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")

    # Compara o email especificado utilizando o padrão regex e retorna o resultado
    return email_regex_pattern.match(email)


#endregion

#region Grupos

# Cria e armazena um novo Grupo com o nome fornecido
def create_group (name:str):
    return add_line_csv(settings.GROUPS_PATH, {name})

# Verifica se um Grupo com o id forneido existe armazenado no banco de dados
def exists_group (id:int):
    return id < line_len_csv(settings.GROUPS_PATH) - 1

# retorna o nome do Grupo que corresponde ao id especificado 
def get_group_name (id:int):
    read_line_csv(settings.GROUPS_PATH, id)

#endregion

#region Times

# Cria e armazena um novo Time com o nome fornecido
def create_team (name:str):
    return add_unique_csv_autoid(settings.TEAMS_PATH, {name})

# Verifica se um Time com o id forneido existe armazenado no banco de dados
def exists_team (id:int):
    return find_data_csv(settings.TEAMS_PATH, id) is not None 

# retorna o nome do Time que corresponde ao id especificado 
def get_team_name (id:int):
    return find_data_csv(settings.TEAMS_PATH, id)['name'] 

#endregion

#region Funções

def exists_role (id:int):
    return get_role(id) is not None

#endregion
