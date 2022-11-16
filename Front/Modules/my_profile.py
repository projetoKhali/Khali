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
    
    criar_piechart(module_frame, [len(grades[0]), len(grades[1])])

    frame_usuarios = criar_frame(module_frame, 1, 0, "nes", co0, co1, 3)
    frame_usuarios.columnconfigure(0, minsize = 0, weight = 1)
    frame_usuarios.rowconfigure(0, minsize = 0, weight = 1)

    indice = 2
    frame_avaliados = criar_frame(frame_usuarios, 1, 0, "nsew", co0, co0, 1)
    frame_avaliados.columnconfigure(0, minsize = 0, weight = 1)
    for grade in grades:
        for user in grade:

            frame_rated = criar_frame(frame_avaliados, indice, 0, "ews", co0, co0, 1)
            frame_rated.columnconfigure(0, minsize = 0, weight = 1)
            criar_label(frame_rated, get_role_name(user['role_id']), 'Calibri, 12', co0, 0, 0, "w")  # linha para teste
            criar_label(frame_rated, grade['name'], 'Calibri, 12', co0, 1, 0, "w")  # linha para teste
            # criar_button(frame_rated, 'Editar Avaliação', 'Calibri, 12', 1, 1, "e")  # linha para teste
            indice = indice + 1



def criar_frame(quadro, row, column, sticky, background, highlightbackground, highlightthickness):
    from tkinter import Frame
    frame = Frame(quadro, background=background, highlightbackground=highlightbackground, highlightthickness=highlightthickness)
    frame.grid(row = row, column = column, sticky = sticky, padx = 5, pady = 5)
    return frame

# cria widget do tipo label
def criar_label(quadro, text, font, background, r, c, sticky='n'):
    from tkinter import Label
    Label(quadro, text=text, font=font, background = background , justify='LEFT').grid(row=r, column=c, sticky= sticky)

def criar_button(quadro, text, font, r, c, command, sticky='ne'):
    from tkinter import Button
    Button(quadro, text = text, font = font, background = COLS[0], justify='RIGHT', fg=COLS[2], command=command,
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
