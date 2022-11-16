from tkinter import *
import Settings

# cores
co0 = "#fae8e8"  # rosa
co1 = "#d9d9d9"  # cinza
co2 = "#1a1d1a"  # preta
co3 = "#26413c"  # verde

current_module = None
modules = []

frame_coluna_A = None
frame_coluna_B = None

janela = None

def run():

    global janela

    from Front.WindowManager import create_window
    janela = create_window(co0)

    # função de criar frame
    # row e column referem-se a posição do frame
    def criar_frame(quadro, row, column, sticky="nw"):
        frame = Frame(quadro, background=co0)
        frame.grid(row = row, column = column, sticky = sticky)
        return frame

    # cria widget do tipo label
    def criar_label(quadro, text, font, r, c, w, padx, pady):
        Label(quadro, text=text, font=font, background=co0).grid(row=r, column=c, sticky=w, padx=padx, pady=pady)

    def criar_button(quadro, text, font, command, r, c, w, padx, pady):
        Button(quadro, text=text, font=font, width=10, height=1, command=command, background=co3, fg='white').grid(row=r, column=c, sticky=w, padx=padx, pady=pady)

    # COLUNA A --------------------------------------------------------------
    #frame widgets
    global frame_coluna_A
    frame_coluna_A = criar_frame(janela, 0,0)

    frame_logo = criar_frame(frame_coluna_A, 0, 0, 'news')

    #adiciona Logo
    img = PhotoImage(file=Settings.RESOURCES_PATH + "\Logo_small.png")  # imagem que vai ser colocada na tela, tem que estar com formato gif
    logo = Label(frame_logo, image=img)
    logo.photo = img
    logo.grid(row = 0, column = 0, sticky = 'n')

    from Front.Modules import ModulesManager
    global modules
    modules = ModulesManager.get_modules()

    frame_tabs = criar_frame(frame_coluna_A, 1, 0, 'news')
    frame_tabs.rowconfigure(0, weight = 1)
    frame_tabs.columnconfigure(0, weight = 1)
    
    for tab_index, module in enumerate(modules):
        criar_button(frame_tabs, module.NAME, "Calibri, 14", lambda i=tab_index: run_module(i), tab_index, 0, 'ew', 5, 5)  

    from Authentication import sair
    criar_button(frame_tabs, "Sair", "Calibri, 14", sair, len(modules), 0, "ew", 5, 5)

    if len(modules) > 0: run_module(0)

    return janela

def run_module (m_index):
    global janela
    global frame_coluna_B
    frame_coluna_B = Frame(janela)
    frame_coluna_B.rowconfigure(0, minsize = 800, weight = 1)
    frame_coluna_B.columnconfigure(0, minsize = 800, weight = 1)
    frame_coluna_B.grid(row=0, column=1, sticky = "nsew")
    global current_module
    if current_module is not None:
        current_module.configure(background = "red")
        current_module.destroy()
    current_module = modules[m_index].run(frame_coluna_B)

    return janela

