
co0 = "#fae8e8"  # rosa
co1 = "#d9d9d9"  # cinzinha
co2 = "#1a1d1a"  # preta
co3 = "#26413C"  # verde

col_rated = 'brown'
col_to_rate = 'orange'

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

    # configura o frame_parent para que o module_frame preencha todo o espaço
    frame_parent.columnconfigure(0, weight = 1)
    frame_parent.rowconfigure(0, weight = 1)

    # cria o frame principal do modulo
    module_frame = criar_frame(frame_parent, 0, 0, "news", co0, co0, 0, 0, 0)
    module_frame.columnconfigure(1, weight = 1)
    module_frame.rowconfigure(0, weight = 1)

    # cria a seção da esquerda onde estará a lista de usuários avaliados e pendentes
    criar_section_ratings()    

    # cria a seção da direita onde estarão as informações do usuário logado
    criar_section_profile()    

    return module_frame

def criar_section_ratings():
    from Utils import lista_usuarios_back
    from Front.Scrollbar import add_scrollbar

    # Cria o frame principal da seção
    frame_section = criar_frame(module_frame, 0, 0, "nws", co0, co1, 2, 0, 0)
    frame_section.columnconfigure(0, weight = 1)
    frame_section.rowconfigure(2, weight = 1)

    # Cria o frame de cabeçalho
    frame_section_header = criar_frame(frame_section, 0, 0, "we", co3, co3, 0, 0, 0)
    frame_section_header.columnconfigure(0, weight = 1)

    # Cria um frame para a label de título dentro do cabeçalho
    frame_header_title = criar_frame(frame_section_header, 0, 0, "we", co3, co3, 0, 0, 0)
    criar_label(frame_header_title, 'Avaliações', 'Calibri, 20', co3, 0, 0, 'nes').configure(fg='white')

    # Frame para a timeline / datas importantes da sprint / periodo avaliativo
    frame_sprint_timeline = criar_frame(frame_section, 1, 0, "ew", co0, co1, 0, 2, 2)
    sprint_timeline_str = 'Sprint x | periodo avaliativo acaba em y dias'
    criar_label(frame_sprint_timeline, sprint_timeline_str, 'Calibri, 10', co0, 1, 0, 'ew')

    from Authentication import CURRENT_USER
    from Models.Role import get_role_name

    # cria uma lista com os usuários a serem avaliados pelo usuário logado
    # grades = [
    #       pendentes   = indice 0
    #       avaliados   = indice 1
    # ]
    grades = lista_usuarios_back.get_users(CURRENT_USER.email)
    grades = [grades[0], grades[0]]

    # Cria o pie chart utilizando a informação de usuários
    criar_piechart(frame_section_header, [len(grades[0]), len(grades[1])])

    # Cria o Frame parent de ambas as listas
    frame_listas = criar_frame(frame_section, 2, 0, "nsew", co3, co3, 0, 0, 0)
    frame_listas.columnconfigure(0, weight = 1)
    # frame_listas.rowconfigure([0,1], weight = 1)
    lista_titles = ['Integrantes ainda não Avaliados', 'Integrantes já Avaliados']
    lista_colors = [col_to_rate, col_rated]

    # para cada lista
    for i, grade in enumerate(grades):

        # se a lista não possui usuários, ignore-a - não cria os frames da lista
        if len(grade) < 1: continue

        lista_col = [co0, co1][i]

        # Cria o frame da lista
        frame_lista = criar_frame(frame_listas, i, 0, "news", lista_col, lista_col, 0, 0, 0)
        frame_lista.columnconfigure(0, weight = 1)
        frame_lista.rowconfigure(1, weight = 1)

        # Coloca o título da lista 
        criar_label(frame_lista, lista_titles[i], 'Calibri, 14', lista_colors[i], 0, 0, "we")

        # Cria um frame parent para os usuários dessa lista
        frame_parent_users = criar_frame(frame_lista, 1, 0, "news", lista_col, lista_col, 0, 0, 0)
        frame_parent_users.columnconfigure(0, weight=1)

        # Scrollbar condicional: Apenas utilize Scrollbar nas listas caso o numero total de usuários em ambas seja maior que 10
        # se não fica mt feio seloko xD
        # if len(grades[0] + grades[1]) > 10:
        frame_parent_users = add_scrollbar(criar_frame(frame_parent_users, 0, 0, 'nsew', lista_col, lista_col, 0, 0, 0), lista_col, 0)

        # para cada usuário nessa lista
        for j, user in enumerate(grade + grade):

            # Cria um frame para o usuário
            frame_user = criar_frame(frame_parent_users, j, 0, 'nsew', lista_col, co1, 0, 0, 0)
            frame_user.columnconfigure(0, weight=1)

            # Cria um frame pro nome e role
            frame_user_data = criar_frame(frame_user, 0, 0, 'ew', lista_col, lista_col, 0, 0, 0)
            frame_user_data.columnconfigure(0, weight=1)

            # cria as labels de nome e role
            criar_label(frame_user_data, user['name'], 'Calibri, 12', lista_col, 0, 0, "w")  # linha para teste
            criar_label(frame_user_data, get_role_name(user['role_id']), 'Calibri, 10', lista_col, 1, 0, "w")  # linha para teste

            # Cria um frame pro botão
            frame_user_button = criar_frame(frame_user, 0, 1, 'ew', co0, co0, 0, 0, 0)

            # insere o botão correspondente ao tipo da lista. Pendentes: avaliar; Avaliados: editar
            if i == 0: criar_button(frame_user_button, 'Avaliar', 'Calibri, 12', 1, 1, lambda u=user: avaliar(u['id']), "w"),  # linha para teste
            # else: criar_button(frame_user_button, 'Editar Avaliação', 'Calibri, 12', 1, 1, lambda u=user: avaliar(u['id']), "w"),  # linha para teste


def criar_section_profile():

    # Cria o frame principal da seção
    frame_section = criar_frame(module_frame, 0, 1, "nwes", co0, co1, 2, 0, 0)
    frame_section.columnconfigure(0, weight = 1)
    frame_section.rowconfigure(2, weight = 1)

    # Cria o frame de cabeçalho
    frame_section_header = criar_frame(frame_section, 0, 0, "we", co3, co3, 0, 0, 0)
    frame_section_header.columnconfigure(0, weight = 1)

    # Cria um frame para a label de título dentro do cabeçalho
    frame_header_title = criar_frame(frame_section_header, 0, 0, "ns", co0, co3, 0, 0, 0)
    criar_label(frame_header_title, 'Perfil', 'Calibri, 20', co3, 0, 0, 'nwes').configure(fg='white')

    from Authentication import CURRENT_USER
    from Models.Role import get_role_name
    from Models.Group import get_group_name
    from Models.Team import get_team

    frame_header_data = criar_frame(frame_section_header, 1, 0, "ew", co0, co2, 2, 0, 0)
    frame_header_data.columnconfigure([0, 1], weight = 1)
    frame_header_data.columnconfigure([0, 1], weight = 1)
    criar_label(frame_header_data, f'Nome: {CURRENT_USER.name}', 'Calibri, 14', co0, 0, 0, 'w')
    criar_label(frame_header_data, f'Função: {get_role_name(CURRENT_USER.role_id)}', 'Calibri, 12', co0, 1, 0, 'w')
    criar_label(frame_header_data, f'Grupo: {get_group_name(CURRENT_USER.group_id)}', 'Calibri, 14', co0, 0, 1, 'e')
    criar_label(frame_header_data, f'Time: {get_team(CURRENT_USER.team_id).name}', 'Calibri, 12', co0, 1, 1, 'e')

    from Models.Sprint import previous_sprint
    target_sprint = previous_sprint(CURRENT_USER.group_id)

    # sem target_sprint: renderiza informações sobre a avaliação 360
    if target_sprint is None:
        # TODO
        frame_ratings_info = criar_frame(frame_section, 1, 0, "ew", co1, co1, 0, 2, 2)
        criar_label(frame_ratings_info, 'informações sobre a avaliação 360', 'Calibri, 12', co1, 0, 0, 'nwes')

    # Renderiza a seção2 com as informações releantes ao usuário
    else:

        # caso o usuário logado seja instrutor
        if CURRENT_USER.role_id not in [3, 4, 5]:
            pass # TODO: seção com as informações de instrutor

        # caso contrario, usuário padrão
        else:
            criar_seção_perfil(frame_section)


def criar_frame(quadro, row, column, sticky, background, highlightbackground, highlightthickness, px = 5, py = 5):
    from tkinter import Frame
    frame = Frame(quadro, background=background, highlightbackground=highlightbackground, highlightthickness=highlightthickness)
    frame.grid(row = row, column = column, sticky = sticky, padx = px, pady = py)
    return frame


# cria widget do tipo label
def criar_label(quadro, text, font, background, r, c, sticky='n', justify='left'):
    from tkinter import Label
    widget = Label(quadro, text=text, font=font, background = background , justify=justify)
    widget.grid(row=r, column=c, sticky= sticky)
    return widget


def criar_button(quadro, text, font, r, c, command, sticky='ne', width=12):
    from tkinter import Button
    widget = Button(quadro, text = text, font = font, background = co0, justify='right', fg=co2, command=command,
        width=width, height=0, activebackground='#c5a8b0')
    widget.grid(row=r, column=c, sticky= sticky)
    return widget


def criar_piechart (module_frame, data):
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    frame_dashboards = criar_frame(module_frame, 0, 1, "ne", co3, co3, 0, 0, 0)
    figure = graphic_pie(data)
    canvas = FigureCanvasTkAgg(figure, master = frame_dashboards)
    canvas.get_tk_widget().grid(row=0, column=0, sticky='e')


def graphic_pie(data=list,):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize = (.65,.65), subplot_kw=dict(aspect="equal"))
    ax.set_anchor('E')
    def func (pct, allvals):
        absolute = int(pct/100.*sum(allvals))
        return "{:.0f}%\n({:d})".format(pct, absolute)
    _, _, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), textprops=dict(color="white"), colors=[col_to_rate, col_rated])
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    plt.setp(autotexts, size=7, weight='bold')
    fig.set_facecolor(co3)
    return fig


def avaliar (id):
    from Front.Modules import avaliacao
    global module_frame
    avaliacao.run(module_frame, id)


def criar_seção_perfil(frame_section):
    from Authentication import CURRENT_USER

    frame_user_pentagon = criar_frame(frame_section, 1, 0, "ew", co1, co1, 0, 2, 2)
    frame_user_pentagon.columnconfigure(1, weight = 1)
    # frame_user_pentagon.rowconfigure(1, weight = 1)

    from graficos.Dashboards import user_pentagon
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    figure = user_pentagon(CURRENT_USER.id, co3, co1, 2.75, 2.25)

    canvas = FigureCanvasTkAgg(figure, master=frame_user_pentagon)

    canvas_tkw = canvas.get_tk_widget()
    canvas_tkw.columnconfigure(1, weight = 1)
    canvas_tkw.grid(row=0, column=0, sticky='wens')

    from Models.id_criteria import criteria

    frame_legenda = criar_frame(frame_user_pentagon, 0, 1, "nsew", co0, co2, 2, 8, 32)

    frame_legenda.columnconfigure(0, weight = 1)
    frame_legenda.rowconfigure([i for i in range(len(criteria))], weight = 1)

    from Models.Rating import get_ratings
    from Models.id_criteria import criteria
    from Models.Sprint import previous_sprint
    from graficos.Integrador import classify_criteria, medias
    target_sprint = previous_sprint(CURRENT_USER.group_id)
    ratings = get_ratings(to_user_id=CURRENT_USER.id, sprint_id=target_sprint.id)
    u_medias = medias(criteria, [classify_criteria(criteria, ratings)])[0]

    for c_index, c in enumerate(criteria):
        frame_criterio = criar_frame(frame_legenda, c_index, 0, "nsew", co0, co2, 0, 4, 4)
        frame_criterio.columnconfigure(1, weight=1)
        criar_label(frame_criterio, f'{c}: ', 'Calibri, 10 bold', co0, 0, 0, 'we', 'center')
        criar_label(frame_criterio, f'Nome do Critério: ', 'Calibri, 10', co0, 0, 1, 'we', 'center')
        criar_label(frame_criterio, f'{u_medias[c_index]:.1f}', 'Calibri, 10 bold', co0, 0, 2, 'e', 'center').configure(fg=co3)

    frame_feedbacks = criar_frame(frame_section, 2, 0, "nsew", co0, co2, 0, 0, 0)
    frame_feedbacks.columnconfigure(0, weight=1)
    frame_feedbacks.rowconfigure(2, weight=1)

    from Models.Sprint import get_group_sprints
    sprints = get_group_sprints(CURRENT_USER.group_id)

    frame_sprint_selector = criar_frame(frame_feedbacks, 0, 0, "ew", co3, co3, 2, 0, 0)
    frame_sprint_selector.columnconfigure([i for i in range(len(sprints))], weight=1)

    for i, sprint in enumerate(sprints):
        criar_button(frame_sprint_selector, f'Sprint {i+1}', 'Calibri, 12 bold', 0, i, lambda e, i=i, s=sprint:print(f'{i}: {s}'), 'ns', 0)

    from Front.Scrollbar import add_scrollbar

    from Utils.lista_usuarios_back import get_feedbacks
    feedbacks = get_feedbacks(CURRENT_USER.id)

    frame_fb_title = criar_frame(frame_feedbacks, 1, 0, "ew", co2, co1, 4, 0, 0)
    criar_label(frame_fb_title, 'Feedbacks recebidos durante a sprint x:', 'Calibri, 12 bold', co2, 0, 0, 'w', 'center').configure(fg='white')

    frame_feedback_list = add_scrollbar(criar_frame(frame_feedbacks, 2, 0, "nsew", co1, co1, 2, 2, 2), co0, 0)

    for i, fb in enumerate(feedbacks):
        frame_fb = criar_frame(frame_feedback_list, i, 0, "nsew", co0, co2, 2, 4, 4)
        criar_label(frame_fb, fb, 'Calibri, 10', co1, 0, 0, 'we', 'center').configure(wraplength=400)


