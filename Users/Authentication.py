from CSV.CSVHandler import *
from Front import WindowManager
from Users.envioemail import envio_email
from Users.Gerar_Senha import gerar_senha
from Users.User import User

import Settings as settings
from .Roles.Role import *

#region Users

CURRENT_USER = None

# Efetua o login de Usuário e, se efetuado com sucesso, retorna o User logado 
def login (email, senha):

    # Acessa o usuário que corresponde ao email fornecido na database
    try:
        user_data = find_data_csv(settings.USERS_PATH, email)
        hashed_pw = user_data["password"]

    # em caso de erro, retorna o erro 0 - dado não encontrado
    except:
        print("dado não encontrado")
        return 0

    # importa a biblioteca de criptografia
    import bcrypt

    # compara a senha fornecida com a senha criptografada salva na database
    if not bcrypt.checkpw(senha.encode(), hashed_pw.encode()):

        # caso a comparação retorne False, significa que as senhas não são iguais
        # retorna o código de erro 1 - dado invalido
        print("dado inválido")
        return 1

    # comparação de senhas retorna True, login retornará o Usuário
    print("login sucesso")

    global CURRENT_USER
    CURRENT_USER = User(
        user_data['name'],
        user_data['email'],
        user_data['group_id'],
        user_data['team_id'],
        user_data['role_id'],
        user_data['password']
    )

    WindowManager.next_state()

    return CURRENT_USER


# Efetua o Cadastro de um novo Usuário e, se efetuado com sucesso, o armazena na database .csv
def register (name, email, group_id, team_id, role_id, custom_password = None):

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

    # Inicializa variável senha para armazenamento
    password = str(custom_password)
    if password is None:

        # Atualiza a senha toda vez que uma senha gerada é inválida
        while not validate_user_password(password):
            password = gerar_senha()

    print (f'email: {email} | password: {password}')

    # Importa bcrypt para criptografar a senha
    import bcrypt

    # Codifica a senha para utf-8: b'senha'
    encoded_password = password.encode('utf-8')

    # Gera um Hash da senha utilizando 'hashpw' com a senha codificada e um 'salt' gerado com o bcrypt
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

    # Cria o Usuário com as informações especificadas        !! decodifica senha antes de salvar: remove b' e ' da string !! 
    user = User(name, email, group_id, team_id, role_id, hashed_password.decode('utf-8'))

    if settings.SEND_EMAIL_ON_REGISTER:
        # from Utils import sistema_email
        # sistema_email.enviar_email(name, email, password)
        from Utils.sistema_envio_email import envio_email
        # Envia email com os dados le login automaticamente para o usuário
        envio_email(name, email, password)

    # Adiciona o usuário para a database
    add_unique_csv_autoid(settings.USERS_PATH, get_user_fields(user))



# Retorna uma lista com as informações de um Usuário
def get_user_fields (user:User):
    return [
        user.name,
        user.email,
        user.group_id,
        user.team_id,
        user.role_id,
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
    if password is None or len(password) < settings.PASSWORD_MIN_MAX[0] or len(password) >= settings.PASSWORD_MIN_MAX[1]:
        return False

    # Importa a biblioteca de utilidades para strings
    import string

    # Cria 3 variaveis booleanas para as categorias: letras, digitos, caracteres especiais
    letters, digits, punctuations = False, False, False

    # Verifica cada digito da senha
    for char in password:

        # Se o caractere é letters, mude o valor da booleana para True
        if char in string.ascii_letters:
            letters = True

        # Se o caractere é digits, mude o valor da booleana para True
        if char in string.digits:
            digits = True

        # Se o caractere é punctuations, mude o valor da booleana para True
        if char in string.punctuation:
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
    if id is None:
        return True
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
    if id is None:
        return True
    return find_data_by_id_csv(settings.TEAMS_PATH, id) is not None 

# retorna o nome do Time que corresponde ao id especificado 
def get_team_name (id:int):
    return find_data_by_id_csv(settings.TEAMS_PATH, id)['name'] 

#endregion

#region Funções

def exists_role (id:int):
    return get_role(id) is not None

#endregion
