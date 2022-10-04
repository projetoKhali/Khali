from inspect import modulesbyfile
from re import A
from tkinter import *
import Settings

# cores
co0 = "#FAE8E8"  # rosa
co1 = "#D9D9D9"  # cinza
co2 = "#1A1D1A"  # preta
co3 = "#26413C"  # verde

current_module = None
modules = []

frame_coluna_A = None
frame_coluna_B = None

def run():

    # cria a janela
    janela = Tk()
    janela.title('')
    janela.geometry('1300x670')  # tamanho da tela, largura x altura

    # tentativa de dar numero de linhas e colunas para a tabela. Se deixo ativado, os labels ficam espalhados pela tela.
    janela.rowconfigure(0, minsize = 800, weight = 1)
    janela.columnconfigure(1, minsize = 800, weight = 1)
    janela.configure(background=co0)

    # função de criar frame
    # row e column referem-se a posição do frame
    def criar_frame(quadro, row, column):
        frame = Frame(quadro, background=co0)
        frame.grid(row = row, column = column, sticky = "nw")
        return frame

    # cria widget do tipo label
    def criar_label(quadro, text, font, r, c, w, padx, pady):
        Label(quadro, text=text, font=font, background=co0).grid(row=r, column=c, sticky=w, padx = padx, pady = pady)

    def criar_button(quadro, text, font, command, r, c, w, padx, pady):
        Button(quadro, text=text, font=font, height=0, command = command, background = co3, fg = 'white').grid(row=r, column=c, sticky=w, padx = padx, pady = pady)

    # COLUNA A --------------------------------------------------------------
    #frame widgets
    global frame_coluna_A
    frame_coluna_A = criar_frame(janela, 0,0)

    frame_logo = criar_frame(frame_coluna_A, 0, 0)

    #adiciona Logo
    img = PhotoImage(file=".\\" + Settings.RESOURCES_PATH + "\Logo_small.png")  # imagem que vai ser colocada na tela, tem que estar com formato gif
    logo = Label(frame_logo, image=img)
    logo.photo = img
    logo.grid(row = 0, column = 0, sticky = 'n')

    from Front.Modules import ModulesManager
    global modules
    modules = ModulesManager.get_modules()

    frame_tabs = criar_frame(frame_coluna_A, 1, 0)

    for tab_index, module in enumerate(modules):
        criar_button(frame_tabs, module.NAME, "Calibri, 14", lambda i=tab_index: run_module(i), tab_index, 0, 'w', 5, 5)  

    from Users.Authentication import sair
    criar_button(frame_coluna_A ,"    sair    " ,"arial" ,sair ,2 ,0 ,"w" ,5 , 5)

    print(f'modules: {modules}')

    #adiciona botões
    #criar_button(frame_coluna_A, 'Meu Perfil', "Calibri, 14", None, 1,0, 'w', 5, 5)

    # COLUNA B --------------------------------------------------------------
    #frame da segunda coluna, que muda se apertar "Cadastro" ou "Meu Perfil"
    # frame_coluna_B = criar_frame(janela, 0,1)
    # frame_coluna_B.configure(background="green")
    # frame_coluna_B.grid(row=0, column=1, sticky="nsew")


    def run_module (m_index):
        global frame_coluna_B
        frame_coluna_B = Frame(janela)
        frame_coluna_B.grid(row=0, column=1, sticky = "nsew")
        global current_module
        if current_module is not None:
            current_module.configure(background = "red")
            current_module.destroy()
        current_module = modules[m_index].run(frame_coluna_B)

    run_module(0)    
    return janela