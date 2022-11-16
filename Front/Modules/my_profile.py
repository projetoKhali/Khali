from Settings import COLS

co0 = "#fae8e8"  # rosa
co1 = "#d9d9d9"
co2 = "#1a1d1a"  # preta

# Informações do modulo
NAME = 'Lista'
REQUIRED_PERMISSIONS_REG  = [None]
REQUIRED_PERMISSIONS_RATE = [
    [3, 4, 5]  # pelo menos uma das 3
]
REQUIRED_PERMISSIONS_VIEW = [None]

def run(frame_parent):
    from Utils import lista_usuarios_back

    from Front.Scrollbar import add_scrollbar
    module_frame = add_scrollbar(frame_parent)
    module_frame.columnconfigure([0,1], minsize = 0, weight = 1)
    module_frame.rowconfigure([0,1], minsize = 0, weight = 1)

    from Authentication import CURRENT_USER
    from Models.Role import get_role_name
    # cria uma lista com os usuários a serem avaliados pelo usuário logado
    grades = lista_usuarios_back.get_users(CURRENT_USER.email)
    
    criar_piechart(module_frame, [len(grades[1]), len(grades[0])])

    frame_section_lista = criar_frame(module_frame, 0, 0, "nes", co0, co1, 3)
    frame_section_lista.columnconfigure(0, minsize = 0, weight = 1)
    frame_section_lista.rowconfigure(0, minsize = 0, weight = 1)

    frame_listas = criar_frame(frame_section_lista, 0, 0, "nsew", co0, co0, 1)
    frame_listas.columnconfigure(0, minsize = 0, weight = 1)
    lista_titles = ['Integrantes ainda não Avaliados', 'Integrantes já Avaliados']

    # grades = grades[:1]

    for i, grade in enumerate(grades):

        if len(grade) < 1: continue
            
        frame_lista = criar_frame(frame_listas, i, 0, "ews", co0, co0, 1)
        frame_lista.columnconfigure(0, minsize = 0, weight = 1)
        criar_label(frame_lista, lista_titles[i], 'Calibri, 14', co0, 0, 0, "w")
        frame_parent_users = criar_frame(frame_lista, 1, 0, "ews", co0, co0, 1)

        for j, user in enumerate(grade):

            frame_user = criar_frame(frame_parent_users, j, 0, 'ew', co0, co0, 0)

            criar_label(frame_user, get_role_name(user['role_id']), 'Calibri, 12', co0, 0, 0, "w")  # linha para teste
            criar_label(frame_user, user['name'], 'Calibri, 12', co0, 1, 0, "w")  # linha para teste
            # criar_button(frame_rated, 'Editar Avaliação', 'Calibri, 12', 1, 1, "e")  # linha para teste



def criar_frame(quadro, row, column, sticky, background, highlightbackground, highlightthickness):
    from tkinter import Frame
    frame = Frame(quadro, background=background, highlightbackground=highlightbackground, highlightthickness=highlightthickness)
    frame.grid(row = row, column = column, sticky = sticky, padx = 5, pady = 5)
    return frame

# cria widget do tipo label
def criar_label(quadro, text, font, background, r, c, sticky='n'):
    from tkinter import Label
    Label(quadro, text=text, font=font, background = background , justify='left').grid(row=r, column=c, sticky= sticky)

def criar_button(quadro, text, font, r, c, command, sticky='ne'):
    from tkinter import Button
    Button(quadro, text = text, font = font, background = COLS[0], justify='right', fg=COLS[2], command=command,
        width=13, height=0, activebackground='#c5a8b0').grid(row=r, column=c, sticky= sticky)

def criar_piechart (module_frame, data):
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    frame_dashboards = criar_frame(module_frame, 1, 1, "new", co0, co0, 0)
    ## grafico pizza
    labels_pie_graphic = ['Concluídas', 'Pendentes']
    figure = graphic_pie(data, labels_pie_graphic)
    canvas = FigureCanvasTkAgg(figure, master = frame_dashboards)
    canvas.get_tk_widget().grid(row=0, column=0, sticky='n')

def graphic_pie(data=list, labels = list):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize = (7,4), subplot_kw=dict(aspect="equal"))
    def func (pct, allvals):
        valsum = 0
        for i in allvals:
            valsum += i
        absolute = int(pct/100.*valsum)
        return "{:.1f}%\n({:d})".format(pct, absolute)
    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), textprops=dict(color="black"))
    ax.legend(wedges, labels, title="Avaliações", loc="center left", bbox_to_anchor=(1,0,0.5,1))
    plt.setp(autotexts, size=8, weight='bold')
    ax.set_title("Relação de avaliações concluídas e pendentes")
    fig.set_facecolor(co0)
    return fig
