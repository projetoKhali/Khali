# Importa a biblioteca de geração de valores aleatorios
import random

# Importa a biblioteca de utilidades para strings
import string

# Importa do arquivo Settings a variavel que define o tamanho da senha autogerada
from Settings import AUTO_GEN_PW_SIZE as tamanho_senha

# Retorna uma senha aleatoria 
def gerar_senha():

    # Edit: 'tamanho_senha' movido para arquivo Settings

    # Inicializa uma string contendo os caracteres que serão escolhidos aleatoriamente
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Inicializa a string que armazenará a senha autogerada
    senha_segura = ""

    # Executa o próximo código 'tamanho_senha' vezes
    # Edit: 'i' (index do loop) substituido por '_' (Throw Away Variable)
    for _ in range(tamanho_senha):

        # Escolhe um caractere aleatorio em 'caracteres' e adiciona a 'senha_segura'
        senha_segura += random.choice(caracteres)

    # # Edit: print movido para o escopo do método (ctrl + ; para debugar | PYCHARM: ctrl + /)
    # print(senha_segura)

    # Ao finalizar o loop, retorna a senha_segura que foi gerada
    return senha_segura

# Edit: removido testes