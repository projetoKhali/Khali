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

global module_frame

def run(frame_parent):
    global module_frame
    from Utils import lista_usuarios_back

    frame_parent.columnconfigure(0, minsize = 0, weight = 1)
    frame_parent.rowconfigure(0, minsize = 0, weight = 1)
    frame_parent.configure(background='yellow')

    from Front.Scrollbar import add_scrollbar
    # module_frame = add_scrollbar(frame_parent)
    module_frame = criar_frame(frame_parent, 0, 0, "news", co0, co1, 3)
    module_frame.columnconfigure(0, minsize = 0, weight = 1)
    module_frame.rowconfigure(0, minsize = 0, weight = 1)
    module_frame.configure(background='cyan')

    
    frame_section_ratings = criar_frame(module_frame, 0, 0, "nws", co0, co1, 3)
    frame_section_ratings.columnconfigure(0, minsize = 0, weight = 1)
    frame_section_ratings.rowconfigure(1, minsize = 0, weight = 1)

    frame_ratings_header = criar_frame(frame_section_ratings, 0, 0, "we", 'red', 'red', 0)
    frame_ratings_header.columnconfigure(0, minsize = 0, weight = 1)
    # frame_ratings_header.rowconfigure(0, minsize = 0, weight = 1)

    frame_ratings_title = criar_frame(frame_ratings_header, 0, 0, "we", co0, co1, 0)
    # frame_ratings_title.columnconfigure(0, minsize = 0, weight = 1)
    # frame_ratings_title.rowconfigure(0, minsize = 0, weight = 1)
    criar_label(frame_ratings_title, 'Avaliações', 'Calibri, 20', 'magenta', 0, 0, 'nes')

    from Authentication import CURRENT_USER
    from Models.Role import get_role_name
    # cria uma lista com os usuários a serem avaliados pelo usuário logado
    grades = lista_usuarios_back.get_users(CURRENT_USER.email)
    criar_piechart(frame_ratings_header, [len(grades[0]), len(grades[1])])

    frame_listas = criar_frame(frame_section_ratings, 1, 0, "nsew", 'green', 'green', 1)
    frame_listas.columnconfigure(0, minsize = 0, weight = 1)
    frame_listas.rowconfigure([0,1], minsize = 0, weight = 0)
    lista_titles = ['Integrantes ainda não Avaliados', 'Integrantes já Avaliados']

    for i, grade in enumerate([grades[0], grades[0]]):

        if len(grade) < 1: continue
            
        frame_lista = criar_frame(frame_listas, i, 0, "news", co0, co0, 1, 0, 0)
        frame_lista.columnconfigure(0, minsize = 0, weight = 1)
        frame_lista.rowconfigure(1, minsize = 0, weight = 1)

        criar_label(frame_lista, lista_titles[i], 'Calibri, 14', co0, 0, 0, "w")

        frame_parent_users = criar_frame(frame_lista, 1, 0, "news", co0, co0, 1, 0, 0)
        # frame_parent_users.configure(bg='yellow')
        frame_parent_users.columnconfigure(0, weight=1)

        # frame_parent_users = add_scrollbar(criar_frame(frame_parent_users, 0, 0, 'nsew', co2, co2, 0))

        for j, user in enumerate(grade):

            frame_user = criar_frame(frame_parent_users, j, 0, 'nsew', co0, co0, 0)
            # frame_user.configure(background='red')
            frame_user.columnconfigure(0, weight=1)

            frame_user_data = criar_frame(frame_user, 0, 0, 'ew', co0, co0, 0, 0, 0)
            frame_user_data.columnconfigure(0, weight=1)

            criar_label(frame_user_data, user['name'], 'Calibri, 12', co0, 0, 0, "w")  # linha para teste
            criar_label(frame_user_data, get_role_name(user['role_id']), 'Calibri, 10', co0, 1, 0, "w")  # linha para teste
            # criar_button(frame_rated, 'Editar Avaliação', 'Calibri, 12', 1, 1, "e")  # linha para teste

            frame_user_button = criar_frame(frame_user, 0, 1, 'ew', co0, co0, 0, 0, 0)

            if i == 0: criar_button(frame_user_button, 'Avaliar', 'Calibri, 12', 1, 1, lambda u=user: avaliar(u['id']), "w"),  # linha para teste
            else: criar_button(frame_user_button, 'Editar Avaliação', 'Calibri, 12', 1, 1, lambda u=user: avaliar(u['id']), "w"),  # linha para teste

    return module_frame


def criar_frame(quadro, row, column, sticky, background, highlightbackground, highlightthickness, px = 5, py = 5):
    from tkinter import Frame
    frame = Frame(quadro, background=background, highlightbackground=highlightbackground, highlightthickness=highlightthickness)
    frame.grid(row = row, column = column, sticky = sticky, padx = px, pady = py)
    return frame

# cria widget do tipo label
def criar_label(quadro, text, font, background, r, c, sticky='n'):
    from tkinter import Label
    Label(quadro, text=text, font=font, background = background , justify='left').grid(row=r, column=c, sticky= sticky)

def criar_button(quadro, text, font, r, c, command, sticky='ne'):
    from tkinter import Button
    Button(quadro, text = text, font = font, background = co0, justify='right', fg=co2, command=command,
        width=13, height=0, activebackground='#c5a8b0').grid(row=r, column=c, sticky= sticky)

def criar_piechart (module_frame, data):
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    frame_dashboards = criar_frame(module_frame, 0, 1, "ne", 'magenta', 'magenta', 0, 0, 0)
    ## grafico pizza
    labels_pie_graphic = ['Concluídas', 'Pendentes']
    figure = graphic_pie(data, labels_pie_graphic)
    canvas = FigureCanvasTkAgg(figure, master = frame_dashboards)
    canvas.get_tk_widget().grid(row=0, column=0, sticky='e')

def graphic_pie(data=list, labels = list):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize = (.65,.65), subplot_kw=dict(aspect="equal"))
    ax.set_anchor('E')
    def func (pct, allvals):
        absolute = int(pct/100.*sum(allvals))
        return "{:.0f}%\n({:d})".format(pct, absolute)
    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), textprops=dict(color="black"))
    # ax.legend(wedges, labels, loc="center right", bbox_to_anchor=(0, .25, 0, 0), prop={'size':8}, frameon=True)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    plt.setp(autotexts, size=7, weight='bold')
    fig.set_facecolor(co0)
    return fig

def avaliar (id):
    from Front.Modules import avaliacao
    global module_frame
    avaliacao.run(module_frame, id)
