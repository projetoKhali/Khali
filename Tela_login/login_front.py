from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
from Settings import RESOURCES_PATH, co0

def run():

    #criando janela
    janela = tk.Tk()
    janela.title('')
    janela.geometry('1300x670') #aqui coloco o tamanho da tela, largura x altura
    janela.configure(background=co0)
    janela.resizable(width=FALSE, height=FALSE)

    #criar diretório para a imagem de login
    # def verificar_arquivo():
    #     caminho = 'C:/Users/User/PycharmProjects/API_TANIA/Khali'
    #     arquivo = caminho + 'Logo_small2.png'
    #     if not os.path.exists(caminho):
    #         os.makedirs(caminho)
    #     if not os.path.exists(arquivo):
    #         open(arquivo, 'w')
    #     return arquivo
    #
    # verificar_arquivo()

    #criar imagem e distribuir pro intereior do label essa imagem
    path = ".\\" + RESOURCES_PATH + "\Logo_small2.png"
    print(path)
    img = PhotoImage(file=path) #imagem que vai ser colocada na tela, tem que estar com formato gif
    print(img)
    label_imagem = tk.Label(janela, image=img)
    label_imagem.place(relx = 0.5, rely = 0.2, anchor = 'center') #creio que 0.5 seja 50% da janela

    #*****CAIXAS DE ENTRADA*****
    en_email = tk.Entry(janela, bd=2, font=("Calibri", 15), justify=LEFT) #bd é a borda
    en_email.place(relx = 0.5, rely = 0.4, anchor = 'center')
    email = en_email.get() #email

    en_senha = tk.Entry(janela, bd=2, font=("Calibri", 15), justify=LEFT)
    en_senha.place(relx = 0.5, rely = 0.5, anchor = 'center')
    senha = en_senha.get()

    #criando textos (Email, Senha e Login)
    label_email = tk.Label(janela, text = 'E-mail', font = ("Calibri,15"), background = co0)
    label_email.place(relx = 0.40, rely = 0.4, anchor = 'center')

    label_senha = tk.Label(janela, text = 'Senha', font = ("Calibri,15"), background = co0)
    label_senha.place(relx = 0.40, rely = 0.5, anchor = 'center')

    #*****BOTÃO DE LOGIN*****
    botao_login = tk.Button(janela, text = 'Entrar', font = ("Calibri,15"))
    botao_login.place(relx = 0.50, rely = 0.57, anchor = 'center')

    #dividindo a janela
    # frame_cima = Frame(janela, width=1300, height=50, bg=co0, relief='flat')
    # frame
    # janela.mainloop()
    return janela
