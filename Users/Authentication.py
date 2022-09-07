
# Insira imports aqui para utilizá-los sem incluir no namespace (ao importar Users, NÃO importará também estes imports)
from string import punctuation
from CSV.CSVHandler import *
from Users.Gerar_Senha import gerar_senha
from Users.User import User

import Settings as settings
from .Roles.Role import *

#region Users

# TODO: global current_user

# TODO: Login method
def login (email, senha=0):
    a = find_data_csv(settings.USERS_PATH, email)
    #descriptografar
    print(a["senha"])


# Efetua o Cadastro de um novo Usuário e, se efetuado com sucesso, o armazena na database .csv
def register (name, email, group_id, team_id, role_id):

    # Verifica se o Nome do Usuário fornecido é válido. Cancela o processo caso não seja.
    if not validate_user_name (name):
        print(COLS[2] + 'Authentication.Register -- Erro ao cadastrar usuario: Nome fornecido não é válido' + COLS[0])
        return

    # Verifica se o Email fornecido é válido. Cancela o processo caso não seja.
    if not validate_user_email (email):
        print(COLS[2] + 'Authentication.Register -- Erro ao cadastrar usuario: Email fornecido não é válido' + COLS[0])
        return

    # Verifica se o Grupo fornceido é válido. Cancela o processo caso não seja.
    if not exists_group (group_id):
        print(COLS[2] + f'Authentication.Register -- Erro: Grupo de id {group_id} não existe' + COLS[0])
        return

    # Verifica se o Time fornecido é válido. Cancela o processo caso não seja.
    if not exists_team (team_id):
        print(COLS[2] + f'Authentication.Register -- Erro: Time de id {team_id} não existe' + COLS[0])
        return

    # Verifica se a Função fornecida é válida. Cancela o processo caso não seja.
    if not exists_role (role_id):
        print(COLS[2] + f'Authentication.Register -- Erro: Função de id {role_id} não existe' + COLS[0])
        return

    # Gera uma senha aleatória para o Usuário
    password = gerar_senha()

    # Verifica se a Senha fornecida é válida. TODO: gerar outra caso invalida
    if not validate_user_password(password):
        print(COLS[2] + f'Authentication.Register -- Erro: Senha inválida para cadastro' + COLS[0])
        return

    # Importa bcrypt para criptografar a senha
    import bcrypt

    # Codifica a senha para utf-8: b'senha'
    encoded_password = password.encode('utf-8')

    # Gera um Hash da senha utilizando 'hashpw' com a senha codificada e um 'salt' gerado com o bcrypt
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

    # 🤔 is this really needed?                     !! decodifica a senha antes de salvar: remove b' e ' da string !! 
    user = User(name, email, group_id, team_id, role_id, hashed_password.decode('utf-8'))

    # Adiciona o usuário para a database
    add_unique_csv_autoid(settings.USERS_PATH, get_user_fields(user))


# Retorna uma lista com as informações de um Usuário
def get_user_fields (user:User):
    return [
        user.name,
        user.email,
        get_group_name(user.group_id),
        get_team_name(user.team_id),
        get_role_name(user.role_id),
        user.password
    ]

#endregion

#region User Register Validation

# Retorna True se o nome especificado é valido e False se não
def validate_user_name(name:str):

    # Nome fornecido é INVALIDO se descumprir qualquer uma das seguintes condições:
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


def validate_user_password(password:str):

    # Senha fornecida é INVALIDA se descumprir qualquer uma das seguintes condições:
    # Numero de caracteres é maior ou igual ao minimo predefinido -> PASSWORD_MIN_MAX[0] 
    # Numero de caracteres é menor que o maximo predefinido       -> PASSWORD_MIN_MAX[1]
    if len(password) < settings.PASSWORD_MIN_MAX[0] or len(password) >= settings.PASSWORD_MIN_MAX[1]:
        return False

    # Importa a biblioteca de utilidades para strings
    import string

    # Cria 3 variaveis booleanas para as categorias: letras, digitos, caracteres especiais
    letters, digits, punctuations = False, False, False

    # Verifica cada digito da senha
    for char in password:

        # Se o caractere é letters, mude o valor da booleana para True
        if char in string.ascii_letters:
            print(char + " is letters")
            letters = True

        # Se o caractere é digits, mude o valor da booleana para True
        if char in string.digits:
            print(char + " is digits")
            digits = True

        # Se o caractere é punctuations, mude o valor da booleana para True
        if char in string.punctuation:
            print(char + " is punctuations")
            punctuations = True

    # Após o loop, retorna Verdadeiro caso as 3 booleanas sejam True
    return (letters and digits and punctuations)

#endregion

#region Grupos

# Cria e armazena um novo Grupo com o nome fornecido
def create_group (name:str):
    return add_unique_csv_autoid(settings.GROUPS_PATH, [name])

# Verifica se um Grupo com o id forneido existe armazenado no banco de dados
def exists_group (id:int):
    return find_data_by_id_csv(settings.GROUPS_PATH, id) is not None 

# retorna o nome do Grupo que corresponde ao id especificado 
def get_group_name (id:int):
    return find_data_by_id_csv(settings.GROUPS_PATH, id)['name'] 

#endregion

#region Times

# Cria e armazena um novo Time com o nome fornecido
def create_team (name:str, group:int):
    return add_unique_csv_autoid(settings.TEAMS_PATH, [group, name])

# Verifica se um Time com o id forneido existe armazenado no banco de dados
def exists_team (id:int):
    return find_data_by_id_csv(settings.TEAMS_PATH, id) is not None 

# retorna o nome do Time que corresponde ao id especificado 
def get_team_name (id:int):
    return find_data_by_id_csv(settings.TEAMS_PATH, id)['name'] 

#endregion

#region Funções

def exists_role (id:int):
    return get_role(id) is not None

#endregion
