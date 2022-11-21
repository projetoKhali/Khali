from tkinter import *
from Front.Core import *
import Settings

modules = []

current_module = None

current_module_index = None
previous_module_index = None

frame_coluna_A = None
frame_coluna_B = None

janela = None

def run():

    global janela

    from Front.WindowManager import create_window
    janela = create_window(co0, current_module)

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

    from Events import register
    register('sub_module_open', open_sub_module)
    register('sub_module_close', close_sub_module)

    # create_modules()

    if len(modules) > 0: run_module(0)

    return janela


def open_sub_module():
    global current_module_index, previous_module_index
    previous_module_index = current_module_index
    current_module_index = None
    create_modules()

def close_sub_module():
    global current_module_index, previous_module_index
    current_module_index = previous_module_index
    previous_module_index = None
    create_modules()


def create_modules():

    frame_tabs = criar_frame(frame_coluna_A, 1, 0, 'news')
    frame_tabs.columnconfigure(0, weight = 1)
    
    for index, module in enumerate(modules):
        btn = criar_button(frame_tabs, module.NAME, "Calibri, 14", index, 0, lambda i=index: run_module(i), 'ew')
        if index == current_module_index: btn.config(disabledforeground=co3, bg=co1, state='disabled')
        else: btn.config(bg=co3, fg=co0)

    from Authentication import sair
    criar_button(frame_tabs, "Sair", "Calibri, 14", len(modules), 0, sair, "ews").config(bg=co3, fg=co0)


def run_module (index):
    global janela, frame_coluna_B, frame_coluna_A

    # prepara o frame_coluna_B
    frame_coluna_B = Frame(janela)
    frame_coluna_B.rowconfigure(0, weight = 1)
    frame_coluna_B.columnconfigure(0, weight = 1)
    frame_coluna_B.grid(row=0, column=1, sticky = "nsew")

    global current_module, current_module_index
    # if current_module is not None:
    #     # current_module.configure(background = "red")
    #     current_module.destroy()
    #     current_module = None

    # roda o modulo e sobrescreve a variavel current_module
    current_module_index = index
    current_module = modules[index].run(frame_coluna_B)

    children = frame_coluna_A.winfo_children()
    if children is not None and len(children) > 1 and children[1] is not None:
        children[1].destroy()

    create_modules()

