from tkinter import *

def grid (obj, r, c, s):
    obj.grid(row=r, column=c)
    return obj

def create_window(a):
    co0 = "#FAE8E8"  # rosa

    window = Tk()
    window.title(a['title'])
    window.geometry(a['res'])  # tamanho da tela, largura x altura

    # tentativa de dar numero de linhas e colunas para a tabela. Se deixo ativado, os labels ficam espalhados pela tela.
    # window.rowconfigure(0, minsize = 800, weight = 1)
    # window.columnconfigure(1, minsize = 800, weight = 1)
    window.configure(background=co0)
    return window

def create_frame(parent, a):
    return grid(Frame(parent, bg=a['bg'], padx=a['padx'], pady=a['pady']), a['r'], a['c'], a['sticky'])

def create_label(parent, a):
    return grid(Label(parent, bg=a['bg'], text=a['text'], font=f"{a['font']}, {a['font-size']}"), a['r'], a['c'], a['sticky'])
