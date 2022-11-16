from tkinter import *
from Settings import RESOURCES_PATH, co0

def run():

    # criando janela
    from Front.WindowManager import create_window
    janela = create_window(co0)

        #*****BOTÃO DE LOGIN*****
    def send_login():
        email = en_email.get()
        senha = en_senha.get()
        from Authentication import login
        login(email=email, senha=senha)

    # criar imagem e distribuir pro intereior do label essa imagem
    # path = "\Logo_big.gif"
    
    # criando frame das labels e entry
    frame_login = Frame(janela, background=co0)
    frame_login.place(relx= 0.5, rely= 0.4, anchor= "center")

    # criando frame que contêm outros frames
    frame_entrada = Frame(frame_login, background=co0)
    frame_entrada.grid(row=1, column= 0, pady= 4)

    # criando framde do botão
    frame_botao = Frame(frame_login)
    frame_botao.grid(row=2, column= 0, pady= 4)

    # criando frame da imagem
    frame_imagem = Frame(frame_login)
    frame_imagem.grid(row= 0, column= 0, pady= 4)

    # imagem
    img = PhotoImage(file=".\\" + RESOURCES_PATH + "\Logo_small.png") #imagem que vai ser colocada na tela, tem que estar com formato gif
    label_imagem = Label(frame_imagem, image=img, background=co0)
    label_imagem.photo = img
    label_imagem.grid(row= 0, column= 0) #creio que 0.5 seja 50% da janela

    # label senha
    label_login=Label(master= frame_entrada,
    text='E-mail: ', fg='#1a1d1a', bg='#fae8e8', font=('Calibre', 15), justify=LEFT)
    label_login.grid(row= 0, column= 0, pady= 2)

    # entry email
    en_email = Entry(frame_entrada, bd=2, font=("Calibri", 15), justify=LEFT) #bd é a borda
    en_email.grid(row= 0, column= 1)

    # label senha
    label_senha=Label(master= frame_entrada,
    text='Senha: ', fg='#1a1d1a', bg='#fae8e8', font=('Calibre', 15), justify=LEFT)
    label_senha.grid(row=1, column = 0, pady= 2)

    # entry senha
    en_senha = Entry(frame_entrada, bd=2, font=("Calibri", 15), justify=LEFT,show="*")
    en_senha.grid(row = 1, column= 1)

    # ******Botão de login*******
    botao_login = Button(frame_botao, text = 'Entrar', font = ("Calibri,15"), width=10, height=1, command=send_login, bg='#d9d9d9', activebackground='#c5a8b0', fg='#1a1d1a')
    botao_login.grid(row = 0, column= 0)

    # dividindo a janela
    return janela
