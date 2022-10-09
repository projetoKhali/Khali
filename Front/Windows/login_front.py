from tkinter import *
from Settings import RESOURCES_PATH, co0

def run():

    #criando janela
    janela = Tk()
    janela.title('')
    janela.geometry('1300x670') #aqui coloco o tamanho da tela, largura x altura
    janela.configure(background=co0)
    janela.resizable(width=True, height=True)

    #criar imagem e distribuir pro intereior do label essa imagem
    # path = "\Logo_big.gif"
    img = PhotoImage(file=".\\" + RESOURCES_PATH + "\Logo_small.png") #imagem que vai ser colocada na tela, tem que estar com formato gif
    label_imagem = Label(janela, image=img, background=co0)
    label_imagem.photo = img
    label_imagem.place(relx = 0.5, rely = 0.25, anchor = 'center') #creio que 0.5 seja 50% da janela

    #criando textos (Email, Senha e Login)
    label_login=Label(master=janela,
    text='E-mail ', fg='#1a1d1a', bg='#fae8e8', font=('Calibre', 15), justify=LEFT)
    label_login.place(relx=0.419, rely=0.4, anchor = 'center')

    label_senha=Label(master=janela,
    text='Senha ', fg='#1a1d1a', bg='#fae8e8', font=('Calibre', 15), justify=LEFT)
    label_senha.place(relx=0.419, rely=0.5, anchor = 'center')
    
    # entry email
    en_email = Entry(janela, bd=2, font=("Calibri", 15), justify=LEFT) #bd é a borda
    en_email.place(relx = 0.52, rely = 0.4, anchor = 'center')

    # entry senha
    en_senha = Entry(janela, bd=2, font=("Calibri", 15), justify=LEFT)
    en_senha.place(relx = 0.52, rely = 0.5, anchor = 'center')

    # # label email 
    # label_email = Label(janela, text = 'E-mail', font = ("Calibri,15"), background = co0)
    # label_email.place(relx = 0.40, rely = 0.4, anchor = 'center')

    # # label senha 
    # label_senha = Label(janela, text = 'Senha', font = ("Calibri,15"), background = co0)
    # label_senha.place(relx = 0.40, rely = 0.5, anchor = 'center')

    #*****BOTÃO DE LOGIN*****
    def send_login():
        email = en_email.get()
        senha = en_senha.get()
        from Users.Authentication import login
        login(email=email, senha=senha)

    botao_login = Button(janela, text = 'Entrar', font = ("Calibri,15"), width=10, height=1, command=send_login, bg='#d9d9d9', activebackground='#c5a8b0', fg='#1a1d1a')
    botao_login.place(relx = 0.50, rely = 0.6, anchor = 'center')

    #dividindo a janela
    # frame_cima = Frame(janela, width=1300, height=50, bg=co0, relief='flat')
    # frame
    # janela.mainloop()
    return janela
