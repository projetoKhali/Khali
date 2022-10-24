from tkinter import *
from Settings import co0

def add_scrollbar (target_frame, bg=co0):

    # cria um frame dentro do target_frame, que é a frame "root"
    frm_main = Frame(target_frame, bg=bg)
    frm_main.columnconfigure(0, minsize=0, weight=1)
    frm_main.rowconfigure(0, minsize=0, weight=1)
    frm_main.grid(row=0, column=0, sticky='news')

    # cria um canvas dentro do frame
    canvas = Canvas(frm_main, bg=bg)
    canvas.columnconfigure(0, minsize=0, weight=1)
    canvas.rowconfigure(0, minsize=0, weight=1)
    canvas.grid(row=0, column=0, sticky='news')

    # inicializa a scrollbar
    scrollbar_ver=Scrollbar(frm_main, orient=VERTICAL, command=canvas.yview)
    scrollbar_ver.grid(row=0, column=0, sticky='nse')

    # configura o canvas com o comando da scrollbar
    canvas.configure(yscrollcommand=scrollbar_ver.set)

    # cria outro Frame dentro do Canvas
    module_frame=Frame(canvas, bg=bg, relief = FLAT, bd = 3)
    # module_frame.columnconfigure(0, minsize = 0, weight = 1)
    # module_frame.rowconfigure(0, minsize = 0, weight = 1)
    # module_frame.grid(row=0, column=0, sticky="nsew")
    module_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    
    # adicionar a nova frame a uma janela no canvas
    canvas.create_window((0,0), window=module_frame, anchor='nw')
    
 


    # retorna o novo frame onde estará o conteudo da tela
    return module_frame
