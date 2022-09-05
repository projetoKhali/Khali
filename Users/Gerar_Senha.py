from random import*
import string

def gerar_senha():
    tamanho_senha = 7
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_segura = ""
    for i in range(tamanho_senha):
        senha_segura += choice(caracteres)
    return senha_segura

a = gerar_senha()
print(a)