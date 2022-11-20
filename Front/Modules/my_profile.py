
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
global sel_sprint

def run(frame_parent):
    global module_frame

    # configura o frame_parent para que o module_frame preencha todo o espaço
    frame_parent.columnconfigure(0, weight = 1)
    frame_parent.rowconfigure(0, weight = 1)

    # cria o frame principal do modulo
    module_frame = criar_frame(frame_parent, 0, 0, "news", co0, co0, 0, 0, 0)
    module_frame.columnconfigure(0, weight = 2)
    module_frame.columnconfigure(1, weight = 6)
    module_frame.rowconfigure(0, weight = 1)
    module_frame.rowconfigure(1, weight = 3)

    # cria a seção da esquerda onde estará a lista de usuários avaliados e pendentes
    criar_section_1()    

    from Authentication import CURRENT_USER
    from Models.Sprint import get_group_sprints
    sprints = get_group_sprints(CURRENT_USER.group_id)

    global sel_sprint
    sel_sprint = len(sprints) - 1

    # cria a seção da direita onde estarão as informações do usuário logado
    criar_section_2(sprints)    

    return module_frame


def criar_section_1():
    from Utils import lista_usuarios_back
    from Front.Scrollbar import add_scrollbar

    # Cria o frame principal da seção
    frame_section = criar_frame(module_frame, 0, 0, "nwes", co0, co1, 2, 0, 0)
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

    from Authentication import CURRENT_USER
    from Models.Sprint import current_rating_period, next_rating_period, get_group_sprints
    from datetime import date

    today = date.today()
    sprint = current_rating_period(CURRENT_USER.group_id)
    sprint_timeline_str = ''

    # Retorna o indice da sprint dentro da lista com as sprints do grupo
    def sprint_n(s):
        for i, s in enumerate(get_group_sprints(CURRENT_USER.group_id)): 
            if s.id == sprint.id: return i + 1

    # Caso possuirmos uma sprint cujo periodo avaliativo encontra-se ativo
    if sprint is not None:

        # informa sprint atual + quantidade de dias até o fim do periodo avaliativo
        cur_ratings_end = sprint.rating_period_end() - today
        sprint_timeline_str = f'Sprint {sprint_n(sprint)} | periodo avaliativo acaba em {cur_ratings_end.days} dias'

    # Caso contrário, a sprint com o periodo avaliativo mais proximo será considerada
    else: 
        sprint = next_rating_period(CURRENT_USER.group_id)
        if sprint is not None:

            # informa sprint atual + quantidade de dias até o começo do periodo avaliativo
            next_ratings_start = sprint.rating_period_start() - today
            sprint_timeline_str = f'Sprint {sprint_n(sprint)} | periodo avaliativo começa em {next_ratings_start.days} dias'

        # nenhuma informação relacionada a periodo avaliativo encontrada, mensagem genérica
        else:
            sprint_timeline_str = 'Nenhum período avaliativo previsto'

    # cria a label com as informações do periodo avaliativo
    criar_label(frame_sprint_timeline, sprint_timeline_str, 'Calibri, 10', co0, 1, 0, 'ew')

    from Models.Role import get_role_name

    # cria uma lista com os usuários a serem avaliados pelo usuário logado
    # grades = [
    #       pendentes   = indice 0
    #       avaliados   = indice 1
    # ]
    grades = lista_usuarios_back.get_users(CURRENT_USER.email)

    # grades = [grades[0], grades[0]] # -----------------------------------------------------------------------------------------

    # variavel com o tamanho das listas
    g = [len(grades[0]), len(grades[1])]

    # Cria o pie chart utilizando a informação de usuários
    criar_piechart(frame_section_header, [len(grades[0]), len(grades[1])])

    # Cria o Frame parent de ambas as listas
    frame_listas_parent = criar_frame(frame_section, 2, 0, "nsew", co0 if g[1] == 0 else co1, co1, 0, 0, 0)
    frame_listas_parent.columnconfigure(0, weight = 1)
    if g[0] > 0: frame_listas_parent.rowconfigure(0, weight = 250 if g[1] == 0 else 10)
    if g[1] > 0: frame_listas_parent.rowconfigure(1, weight = 250 if g[0] == 0 else 10)
    frame_listas_parent.rowconfigure(2, weight = 1)

    # listas para facilitar o acesso a informações dentro do loop 'i'
    lista_titles = ['Integrantes ainda não Avaliados', 'Integrantes já Avaliados']
    lista_colors = [col_to_rate, col_rated]

    # para cada lista
    for i, grade in enumerate(grades):
        glen=len(grade)

        # se a lista não possui usuários, ignore-a - não cria os frames da lista
        if len(grade) < 1: continue

        lista_col = [co0, co1][i]

        # Cria o frame da lista
        frame_lista = criar_frame(frame_listas_parent, i, 0, "news", lista_col, lista_col, 0, 0, 0)
        frame_lista.columnconfigure(0, weight = 1)
        frame_lista.rowconfigure(1, weight=1)

        # Coloca o título da lista 
        criar_label(frame_lista, lista_titles[i], 'Calibri, 14', lista_colors[i], 0, 0, "we")

        # Cria um frame parent para os usuários dessa lista
        frame_parent_users = criar_frame(frame_lista, 1, 0, "news", lista_col, lista_col, 0, 0, 0)
        frame_parent_users.columnconfigure(0, weight=1)
        frame_parent_users.rowconfigure(0, weight=1)

        # Scrollbar condicional: Apenas utilize Scrollbar nas listas caso o numero total de usuários em ambas seja maior que (...)
        # se não fica mt feio seloko xD
        if lambda g=glen, g0=g[0], g1=g[1]: True if g0 > 0 and g1 > 0 and g0+g1 >= 12 else True if g >= 12 else False:
            frame_parent_users = criar_frame(frame_parent_users, 0, 0, 'nsew', lista_col, lista_col, 0, 0, 0)
            frame_parent_users.columnconfigure(0, minsize=0, weight=1)
            frame_parent_users.rowconfigure(0, minsize=0, weight=1)
            frame_parent_users = add_scrollbar(frame_parent_users, lista_col, 0)

        # para cada usuário nessa lista
        for j, user in enumerate(grade):

            # Cria um frame para o usuário
            frame_user = criar_frame(frame_parent_users, j, 0, 'nsew', lista_col, co1, 0, 0, 0)
            frame_user.columnconfigure(0, weight=1)

            # Cria um frame pro nome e role
            frame_user_data = criar_frame(frame_user, 0, 0, 'ew', lista_col, lista_col, 0, 0, 0)
            frame_user_data.columnconfigure(0, weight=1)

            # cria as labels de nome e role
            criar_label(frame_user_data, user['name'], 'Calibri, 12', lista_col, 0, 0, "w")
            criar_label(frame_user_data, get_role_name(user['role_id']), 'Calibri, 10', lista_col, 1, 0, "w")

            # Cria um frame pro botão
            frame_user_button = criar_frame(frame_user, 0, 1, 'ew', co0, co0, 0, 0, 0)

            # insere o botão correspondente ao tipo da lista. Pendentes: avaliar; Avaliados: editar
            if i == 0: criar_button(frame_user_button, 'Avaliar', 'Calibri, 12', 1, 1, lambda u=user: avaliar(u['id']), "e"),
            # else: criar_button(frame_user_button, 'Editar Avaliação', 'Calibri, 12', 1, 1, lambda u=user: avaliar(u['id']), "w"),


def criar_section_2(sprints):
    
    # destroy o frame_section_2 anterior caso já exista 
    mf_children = module_frame.winfo_children()
    if mf_children and len(mf_children) > 2 and mf_children[1] is not None:
        from matplotlib import pyplot
        pyplot.close()
        mf_children[1].destroy()

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

    # Cria o cabeçalho do perfil contendo informações do usuário: nome, função, grupo e time
    frame_header_data = criar_frame(frame_section_header, 1, 0, "ew", co0, co2, 2, 0, 0)
    frame_header_data.columnconfigure([0, 1], weight = 1)
    frame_header_data.columnconfigure([0, 1], weight = 1)
    criar_label(frame_header_data, f'Nome: {CURRENT_USER.name}', 'Calibri, 14', co0, 0, 0, 'w')
    criar_label(frame_header_data, f'Função: {get_role_name(CURRENT_USER.role_id)}', 'Calibri, 12', co0, 1, 0, 'w')
    criar_label(frame_header_data, f'Grupo: {get_group_name(CURRENT_USER.group_id)}', 'Calibri, 14', co0, 0, 1, 'e')
    criar_label(frame_header_data, f'Time: {get_team(CURRENT_USER.team_id).name}', 'Calibri, 12', co0, 1, 1, 'e')

    from Models.Sprint import previous_sprint

    # pega a sprint anterior do grupo do usuário logado
    target_sprint = previous_sprint(CURRENT_USER.group_id)

    # sem target_sprint: renderiza informações sobre a avaliação 360
    if target_sprint is None:
        # TODO
        frame_ratings_info = criar_frame(frame_section, 1, 0, "ew", co1, co1, 0, 2, 2)
        criar_label(frame_ratings_info, 'informações sobre a avaliação 360', 'Calibri, 12', co1, 0, 0, 'nwes')

    # Renderiza a seção2 com as informações referentes as avaliações feitas ao usuário
    else:

        # caso o usuário logado seja instrutor
        if CURRENT_USER.role_id not in [3, 4, 5]:
            pass # TODO: seção com as informações de instrutor

        # caso contrario, usuário padrão
        else:
            criar_section_profile(frame_section, sprints)


def criar_section_profile(frame_section, sprints):
    from Authentication import CURRENT_USER

    frame_user_pentagon = criar_frame(frame_section, 1, 0, "ew", co1, co1, 0, 2, 2)
    frame_user_pentagon.columnconfigure(1, weight = 1)
    # frame_user_pentagon.rowconfigure(1, weight = 1)

    from graficos.Dashboards import user_pentagon
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    figure = user_pentagon(CURRENT_USER.id, sprints[sel_sprint], co3, co1, 2.75, 2.25)

    canvas = FigureCanvasTkAgg(figure, master=frame_user_pentagon)

    canvas_tkw = canvas.get_tk_widget()
    canvas_tkw.columnconfigure(1, weight = 1)
    canvas_tkw.grid(row=0, column=0, sticky='wens')

    from Models.id_criteria import criteria

    frame_legenda = criar_frame(frame_user_pentagon, 0, 1, "nsew", co0, co2, 2, 8, 32)

    frame_legenda.columnconfigure(0, weight = 1)
    frame_legenda.rowconfigure([i for i in range(len(criteria))], weight = 1)

    from Models.Rating import get_ratings
    from Models.id_criteria import criteria, criteria_full
    from graficos.Integrador import classify_criteria, medias
    target_sprint = sprints[sel_sprint]
    ratings = get_ratings(to_user_id=CURRENT_USER.id, sprint_id=target_sprint.id)
    u_medias = medias(criteria, [classify_criteria(criteria, ratings)])[0]

    frame_legenda_title = criar_frame(frame_legenda, 0, 0, "ew", co0, co2, 0, 4, 4)
    criar_label(frame_legenda_title, f'Medias durante a sprint {sel_sprint+1}', 'Calibri, 10 bold', co0, 0, 0, 'we', 'center')

    for c_index, c in enumerate(criteria):
        frame_criterio = criar_frame(frame_legenda, c_index+1, 0, "nsew", co0, co2, 0, 4, 4)
        frame_criterio.columnconfigure(1, weight=1)
        criar_label(frame_criterio, f'{c}: ', 'Calibri, 10 bold', co0, 0, 0, 'we', 'center')
        criar_label(frame_criterio, f'{criteria_full[c_index]}: ', 'Calibri, 10', co0, 0, 1, 'we', 'center')
        criar_label(frame_criterio, f'{u_medias[c_index]:.1f}', 'Calibri, 10 bold', co0, 0, 2, 'e', 'center').configure(fg=co3)

    frame_section_feedbacks = criar_frame(frame_section, 2, 0, "nsew", co0, co2, 0, 0, 0)
    frame_section_feedbacks.columnconfigure(0, weight=1)
    frame_section_feedbacks.rowconfigure(2, weight=1)
    create_sprint_selectors(frame_section_feedbacks, sprints)


def create_sprint_selectors(frame_section_feedbacks, sprints):
    from Authentication import CURRENT_USER

    frame_feedbacks = criar_frame(frame_section_feedbacks, 2, 0, "nsew", co0, co2, 0, 0, 0)
    frame_feedbacks.columnconfigure(0, weight=1)
    frame_feedbacks.rowconfigure(2, weight=1)

    frame_sprint_selector = criar_frame(frame_feedbacks, 0, 0, "ew", co3, co3, 2, 0, 0)
    frame_sprint_selector.columnconfigure([i for i in range(len(sprints))], weight=1)

    def select_sprint(_, sprints, sprint_index):
        global sel_sprint
        sel_sprint = sprint_index
        criar_section_2(sprints)

    for index, _ in enumerate(sprints):
        sprint_btn = criar_button(frame_sprint_selector, f'Sprint {index+1}', 'Calibri, 12 bold', 0, index, 
            lambda e=None, s=sprints, i=index: select_sprint(e, s, i), 'ew', 0)
        sprint_btn.configure(fg=co3 if index == sel_sprint else co1, bg=co1 if index == sel_sprint else co3)

    from Front.Scrollbar import add_scrollbar

    from Utils.lista_usuarios_back import get_feedbacks
    feedbacks = get_feedbacks(CURRENT_USER.id, sprints[sel_sprint].id)

    frame_fb_title = criar_frame(frame_feedbacks, 1, 0, "ew", co2, co1, 4, 0, 0)
    criar_label(frame_fb_title, f'Feedbacks recebidos durante a sprint {sel_sprint + 1}:', 'Calibri, 12 bold', co2, 0, 0, 'w', 'center').configure(fg='white')

    frame_feedback_list = criar_frame(frame_feedbacks, 2, 0, "nsew", co1, co1, 2, 2, 2)
    frame_feedback_list.columnconfigure(0, minsize=0, weight=1)
    frame_feedback_list.rowconfigure(0, minsize=0, weight=1)
    frame_feedback_list = add_scrollbar(frame_feedback_list, co0, 0)

    for index, fb in enumerate(feedbacks):
        frame_fb = criar_frame(frame_feedback_list, index, 0, "ns", co0, co2, 2, 4, 4)
        frame_fb.columnconfigure(0, weight=1)
        criar_label(frame_fb, fb, 'Calibri, 10', co1, 0, 0, 'we', 'left').configure(wraplength=400, anchor='n')


# funções genéricas de widgets do tkinter
def criar_frame(quadro, row, column, sticky, background, highlightbackground, highlightthickness, px = 5, py = 5):
    from tkinter import Frame
    frame = Frame(quadro, background=background, highlightbackground=highlightbackground, highlightthickness=highlightthickness)
    frame.grid(row = row, column = column, sticky = sticky, padx = px, pady = py)
    return frame

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


# função que cria e coloca o grafico pentagono em um canvas dentro do frame parametro
def criar_piechart (module_frame, data):
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    frame_dashboards = criar_frame(module_frame, 0, 1, "ne", co3, co3, 0, 0, 0)
    figure = graphic_pie(data)
    canvas = FigureCanvasTkAgg(figure, master = frame_dashboards)
    canvas.get_tk_widget().grid(row=0, column=0, sticky='e')

# função que cria o grafico pentagono com as informações parametro
def graphic_pie(data=list):
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

# função que muda para a tela de avaliação para o usuário de id parametro
def avaliar (id):
    from Front.Modules import avaliacao
    target_frame = module_frame.master.master
    module_frame.master.destroy()
    avaliacao.run(target_frame, id)


