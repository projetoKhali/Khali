from Utils import lista_usuarios_back
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# cores
co0 = "#fae8e8"  # rosa
co1 = "#d9d9d9"  # cinza
co2 = "#1a1d1a"  # preta

# Informações do modulo
NAME = 'Lista'
REQUIRED_PERMISSIONS_REG  = [None]
REQUIRED_PERMISSIONS_RATE = [
    [3, 4, 5]  # pelo menos uma das 3
]
REQUIRED_PERMISSIONS_VIEW = [None]

module_frame = None

# executa o modulo e retorna
def run(frame_parent):

    # global module_frame
    # module_frame=Frame(frame_parent, bg=co0)
    # module_frame.columnconfigure(0, minsize = 0, weight = 1)
    # module_frame.grid(row=0, column=0, sticky="nsew")

    from Front.Scrollbar import add_scrollbar
    module_frame = add_scrollbar(frame_parent)
    module_frame.columnconfigure([0,1], minsize = 0, weight = 1)
    module_frame.rowconfigure([0,1], minsize = 0, weight = 1)
    # module_frame.grid(row=0, column=0, sticky="nsew")

    # ## ScrollBar da Tela Principal
    # # Criar um frame para comportar o canvas 
    # frm_main=Frame(frame_parent, bg=co0)
    # frm_main.pack(fill=BOTH, expand=1) 

    # # O canvas aceita o scrollbar, mas ela só faz o papel da responsividade
    # canvas=Canvas(frm_main, bg=co0)
    # canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # # Configurações do scrollbar
    # scrollbar_ver = Scrollbar(frm_main, orient=VERTICAL, command=canvas.yview) # Comando xview para orientação HORIZONTAL
    # scrollbar_ver.pack(side=RIGHT, fill=Y)

    # # Configurações do canvas
    # canvas.configure(yscrollcommand=scrollbar_ver.set) # xscrollcomand para barra horizontal
    # module_frame=Frame(canvas, bg=co0, relief=FLAT, bd=3) # Não colocamos o frame com o .pack nesse caso
    # module_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar

    
   
    # Integração do frame geral a uma janela do canvas
    # canvas.create_window((0,0), window=module_frame, anchor='nw')

    # importa o usuário logado
    from Users.Authentication import CURRENT_USER

    # cria uma lista com os usuários a serem avaliados pelo usuário logado
    grade_submitted = lista_usuarios_back.get_users(CURRENT_USER.email)[0]
    grade_to_submit = lista_usuarios_back.get_users(CURRENT_USER.email)[1]

    # função de criar frame
    # row e column referem-se a posição do frame
    def criar_frame(quadro, row, column, sticky, background, highlightbackground, highlightthickness):
        frame = Frame(quadro, background=background, highlightbackground=highlightbackground, highlightthickness=highlightthickness)
        frame.grid(row = row, column = column, sticky = sticky, padx = 5, pady = 5)
        return frame

    # cria widget do tipo label
    def criar_label(quadro, text, font, r, c, sticky='n'):
        Label(quadro, text=text, font=font, background = co0, justify=LEFT).grid(row=r, column=c, sticky= sticky)

    def criar_button(quadro, text, font, r, c, command, sticky='ne'):
        Button(quadro, text = text, font = font, background = co0, justify=RIGHT, fg=co2, command=command,
               width=13, height=0, activebackground='#c5a8b0').grid(row=r, column=c, sticky= sticky)

    

    


   # importa a função que transforma role_id em nome da role
    from Models.Role import get_role_name
   
    # frame com os dados do usuário que está logado
    frame_user_logado = criar_frame(module_frame, 0, 0, "nsew", co0, co0, 1)
    criar_label(frame_user_logado, 'Meu Perfil', 'Calibri, 30', 0, 0)
    criar_label(frame_user_logado, get_role_name(CURRENT_USER.role_id), 'Calibri, 12',1, 0, "w")
    criar_label(frame_user_logado, CURRENT_USER.name, 'Calibri, 12',2, 0, "w")

    # frame com todas a lista de usuários, que ocupará apenas o canto superior direito da tela
    # para deixar essa tela menor, coloco nw apenas
    frame_usuarios = criar_frame(module_frame, 1, 0, "nsw", co1, co1, 2)
    frame_usuarios.columnconfigure(0, minsize = 0, weight = 1)
    frame_usuarios.rowconfigure(0, minsize = 0, weight = 1)
    # frame_usuarios = add_scrollbar(frame_usuarios)
    

    frame_dashboards = criar_frame(module_frame, 1, 1, "nsw", co0, co0, 1)
    ## grafico pizza
    # data = [len(grade_submitted), len(grade_to_submit)]
    # figure = graphic_pie(data)
    # canvas = FigureCanvasTkAgg(figure, master = frame_dashboards)
    # canvas.get_tk_widget().grid(row=0, column=0, sticky='wens')
    
   # frame com os usuários que devem ser analisados por quem está logado
    frame_avaliados = criar_frame(frame_usuarios, 1, 0, "nsew", co0, co0, 1)
    frame_avaliados.columnconfigure(0, minsize = 0, weight = 1)
    criar_label(frame_avaliados, 'Integrantes ainda não Avaliados', 'Calibri, 14', 0, 0, "w")

    indice = 2

    for user_to_submit in grade_to_submit:

        frame_to_rate = criar_frame(frame_avaliados, indice, 0, "ew", co0, co0, 1)
        frame_to_rate.columnconfigure(0, minsize = 0, weight = 1)
        criar_label(frame_to_rate, get_role_name(user_to_submit['role_id']), 'Calibri, 12', 0, 0, "w")  # linha para teste
        criar_label(frame_to_rate, user_to_submit['name'], 'Calibri, 12', 1, 0, "w")  # linha para teste
        criar_button(frame_to_rate, 'Avaliar', 'Calibri, 12', 1, 1, lambda u=user_to_submit: avaliar(u['id']), "e")  # linha para teste
        indice = indice + 1


        criar_label(frame_avaliados, 'Integrantes já Avaliados', 'Calibri, 14', indice, 0, "w")

    indice = indice + 1

    for user_submited in grade_submitted:

        frame_rated = criar_frame(frame_avaliados, indice, 0, "ew", co0, co0, 1)
        frame_rated.columnconfigure(0, minsize = 0, weight = 1)
        criar_label(frame_rated, get_role_name(user_submited['role_id']), 'Calibri, 12', 0, 0, "w")  # linha para teste
        criar_label(frame_rated, user_submited['name'], 'Calibri, 12', 1, 0, "w")  # linha para teste
        # criar_button(frame_rated, 'Editar Avaliação', 'Calibri, 12', 1, 1, "e")  # linha para teste
        indice = indice + 1

    f = Frame(frame_usuarios, pady=100, bg=co0)
    Label(f, text='', bg=co0).grid(row=0, column=0, sticky="s")
    f.grid(row=100, column=0, sticky="s")


    return module_frame

def avaliar (id):
    from Front.Modules import avaliacao_teste
    global module_frame
    avaliacao_teste.run(module_frame, id)

def graphic_pie(data = list):
    global grade_submitted
    global grade_to_submit

    plt.style.use('_mpl-gallery-nogrid')

    # make data
    # n_submitted = len(grade_submitted)
    # n_to_submit = len(grade_to_submit)
    # data = [n_submitted, n_to_submit]
    colors = plt.get_cmap('Pastel2')(np.linspace(0.2, 0.7, len(data)))

    # plot
    fig, ax = plt.subplots()
    ax.pie(data, colors = colors, radius = 3, center = (4,4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    ax.set(xlim = (0,8), xticks = np.arange(1,8), ylim=(0,8), yticks=np.arange(1,8))
    return fig
