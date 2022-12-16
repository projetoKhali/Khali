from Settings import AUTO_GEN_PW_SIZE as tamanho_senha
from string import ascii_letters, digits, punctuation
from random import choice

# Retorna uma senha aleatoria 
def gerar_senha():

    # executa join 'tamanho_senha' vezes escolhendo um caractere aleatório dentro dos caracteres permitidos
    return ''.join(choice(ascii_letters + digits + punctuation) for _ in range(tamanho_senha))

