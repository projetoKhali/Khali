from CSV.CSVHandler import *
from Front import WindowManager
from Utils.Gerar_Senha import gerar_senha
from Models.User import User, to_user, create_user
from Models.Group import Group
from Models import Team

import Settings as settings
from Models.Role import *

CURRENT_USER : User = None

# Efetua o login de Usuário e, se efetuado com sucesso, retorna o User logado 
def login (email, senha):

    # Acessa o usuário que corresponde ao email fornecido na database
    try:
        user_data = find_data_csv(settings.USERS_PATH, email)
        hashed_pw = user_data["password"]

    # em caso de erro, retorna o erro 0 - dado não encontrado
    except:
        print("Authentication.login -- Dado não encontrado")
        return 0

    # importa a biblioteca de criptografia
    import bcrypt

    # compara a senha fornecida com a senha criptografada salva na database
    if not bcrypt.checkpw(senha.encode(), hashed_pw.encode()):

        # caso a comparação retorne False, significa que as senhas não são iguais
        # retorna o código de erro 1 - dado invalido
        print("Authentication.login -- Dado inválido")
        return 1

    # comparação de senhas retorna True, login retornará o Usuário
    print("Authentication.login -- login sucesso")

    global CURRENT_USER
    CURRENT_USER = to_user(user_data)

    WindowManager.next_state()

    return CURRENT_USER

# Define que não não tem usuário logado e envia para a tela de login
def sair():
    global CURRENT_USER
    CURRENT_USER = None
    from Front.WindowManager import reset
    reset()

# Efetua o Cadastro de um novo Usuário e, se efetuado com sucesso, o armazena na database .csv
def register (name, email, group_id, team_id, role_id, custom_password = None, log = True):

    # Verifica se o Nome do Usuário fornecido é válido. Cancela o processo caso não seja.
    if not validate_user_name (name):
        print(COLS[2] + 'Authentication.Register -- Erro ao cadastrar usuario: Nome fornecido não é válido' + COLS[0])
        return

    # Verifica se o Email fornecido é válido. Cancela o processo caso não seja.
    if not validate_user_email (email):
        print(COLS[2] + 'Authentication.Register -- Erro ao cadastrar usuario: Email fornecido não é válido' + COLS[0])
        return

    # Verifica se o Grupo fornceido é válido. Cancela o processo caso não seja.
    # if not Group.exists_group (group_id):
    #     print(COLS[2] + f'Authentication.Register -- Erro: Grupo de id {group_id} não existe' + COLS[0])
    #     return

    # Verifica se o Time fornecido é válido. Cancela o processo caso não seja.
    if not Team.exists_team (team_id):
        print(COLS[2] + f'Authentication.Register -- Erro: Time de id {team_id} não existe' + COLS[0])
        return
    # if Team.get_team(team_id).group_id != group_id:
    #     print(COLS[2] + f'Authentication.Register -- Erro: Time de id {team_id} não é do grupo {group_id} do usuário sendo cadastrado' + COLS[0])
    #     return

    # Verifica se a Função fornecida é válida. Cancela o processo caso não seja.
    if not get_role(role_id) is not None:
        print(COLS[2] + f'Authentication.Register -- Erro: Função de id {role_id} não existe' + COLS[0])
        return

    # Inicializa variável senha para armazenamento
    password = str(custom_password)
    if password is None:

        # Atualiza a senha toda vez que uma senha gerada é inválida
        while not validate_user_password(password):
            password = gerar_senha()

    print (f'Authentication.register -- Novo usuário cadastrado. Email: {email}, senha: {password}')

    # Importa bcrypt para criptografar a senha
    import bcrypt

    # Codifica a senha para utf-8: b'senha'
    encoded_password = password.encode('utf-8')

    # Gera um Hash da senha utilizando 'hashpw' com a senha codificada e um 'salt' gerado com o bcrypt
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

    # Cria o Usuário com as informações especificadas        !! decodifica senha antes de salvar: remove b' e ' da string !! 
    user = User(name, email, group_id, team_id, role_id, hashed_password.decode('utf-8'))

    # Adiciona o usuário para a database
    id = create_user(
        user.name,
        user.email,
        user.group_id,
        user.team_id,
        user.role_id,
        user.password
    )

    if settings.SEND_EMAIL_ON_REGISTER:
        # from Utils import sistema_email
        # sistema_email.enviar_email(name, email, password)
        from Utils.sistema_envio_email import envio_email
        # Envia email com os dados le login automaticamente para o usuário
        envio_email(name, email, password)

    return id


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
