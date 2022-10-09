from tkinter import *
from Settings import co0

def add_scrollbar (target_frame, bg=co0):

    # cria um frame dentro do target_frame
    frm_main = Frame(target_frame, bg=bg)
    # frm_main.columnconfigure(0, minsize=0, weight=1)
    frm_main.grid(row=0, column=0, sticky='news')

    # cria um canvas dentro do frame
    canvas = Canvas(frm_main, bg=bg)
    # canvas.rowconfigure(0, minsize=0, weight=1)
    canvas.grid(row=0, column=0, sticky='news')

    # inicializa a scrollbar
    scrollbar_ver=Scrollbar(frm_main, orient=VERTICAL, command=canvas.yview)
    scrollbar_ver.grid(row=0, column=0, sticky='nsw')

    # configura o canvas com o comando da scrollbar
    canvas.configure(yscrollcommand=scrollbar_ver.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    
    module_frame=Frame(canvas, bg=co0)
    module_frame.columnconfigure(0, minsize = 0, weight = 1)
    module_frame.grid(row=0, column=0, sticky="nsew")


    # retorna o novo frame onde estará o conteudo da tela
    return module_frame
