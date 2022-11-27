from Front.Core import *

# cores utilizadas nos frames de usuário das listas pendentes / avaliados
col_to_rate = '#DBBDC1'
col_rated = '#76807D'

global module_frame
global sel_sprint
global user_is_instructor

# Informações do modulo
NAME = 'Lista'
REQUIRED_PERMISSIONS_REG  = [None]
REQUIRED_PERMISSIONS_RATE = [
    [3, 4, 5]  # pelo menos uma das 3
]
REQUIRED_PERMISSIONS_VIEW = [None]

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
    from Time import today

    # sprints = [s for s in get_group_sprints(trigger("get_group_id")) if today() >= s.rating_period_end()]
    sprints = [s for s in get_group_sprints(CURRENT_USER.group_id) if today() >= s.rating_period_end()]

    # após adquirir as sprints que serão utilizadas na tela, define a sprint selecionada como a ultima sprint da lista
    global sel_sprint
    sel_sprint = len(sprints) - 1

    # cria a seção da direita onde estarão as informações do usuário logado
    criar_section_2(sprints)    

    return module_frame


def criar_section_1():
    from Utils import lista_usuarios_back
    from Front.Scrollbar import add_scrollbar
    from Models.Sprint import current_rating_period, next_rating_period, sprint_index
    from Authentication import CURRENT_USER
    from Events import trigger

    # Define se o usuário logado é instrutor
    global user_is_instructor
    user_is_instructor = CURRENT_USER.role_id in [1, 2]

    # o ID do grupo que será referenciado é o valor de retorno do dropdown seletor de grupos caso o usuário seja instrutor
    # ou o group_id do usuário caso aluno
    group_id = trigger("get_group_id") if user_is_instructor else CURRENT_USER.group_id

    # Cria o frame principal da seção
    frame_section = criar_frame(module_frame, 0, 0, "nwes", co0, co2, 2, 0, 0)
    if current_rating_period(group_id) == None and next_rating_period(group_id) == None: frame_section = criar_frame(module_frame, 0, 0, "nwes", co0, co0, 0, 0, 0)
    frame_section.columnconfigure(0, weight = 1)
    frame_section.rowconfigure(3, weight = 1)

    # Cria o frame de cabeçalho
    frame_section_header = criar_frame(frame_section, 0, 0, "we", co3, co3, 0, 0, 0)
    frame_section_header.columnconfigure(0, weight = 1)

    # Cria um frame para a label de título dentro do cabeçalho
    frame_header_title = criar_frame(frame_section_header, 0, 0, "we", co3, co3, 0, 0, 0)
    criar_label(frame_header_title, 'Avaliações', 'Calibri, 24 bold', 0, 0, co3, 'nes').configure(fg=co0)

    # dropdown com nome dos grupos
    from Models.Group import get_groups_of_instructor, get_group_of_name
    if user_is_instructor: create_dropdown(criar_frame(frame_section, 1, 0, "ew", co3, px=0, py=0),0,0, [i.name for i in get_groups_of_instructor(CURRENT_USER.id)], "get_group_id", lambda v: get_group_of_name(v).id)

    # Frame para a timeline / datas importantes da sprint / periodo avaliativo
    frame_sprint_timeline = criar_frame(frame_section, 2, 0, "ew", co0, co0, 0, 2, 2)

    from Time import today

    # pega o periodo avaliativo atual e inicializa uma string que irá conter o valor na label sprint_timeline
    sprint = current_rating_period(group_id)
    sprint_timeline_str = ''

    # Caso possuirmos uma sprint cujo periodo avaliativo encontra-se ativo
    if sprint is not None:

        # informa sprint atual + quantidade de dias até o fim do periodo avaliativo
        cur_ratings_end = sprint.rating_period_end() - today()
        sprint_timeline_str = f'Sprint {sprint_index(group_id, sprint.id)} | Período avaliativo acaba em {cur_ratings_end.days} dias'

    # Caso contrário, a sprint com o periodo avaliativo mais proximo será considerada
    else: 
        sprint = next_rating_period(group_id)
        if sprint is not None:

            # informa sprint atual + quantidade de dias até o começo do periodo avaliativo
            next_ratings_start = sprint.rating_period_start() - today()
            sprint_timeline_str = f'Sprint {sprint_index(group_id, sprint.id)} | Período avaliativo começa em {next_ratings_start.days} dias'

        # nenhuma informação relacionada a periodo avaliativo encontrada, mensagem genérica
        else:
            sprint_timeline_str = 'Nenhum período avaliativo previsto'
            
    # cria a label com as informações do periodo avaliativo
    criar_label(frame_sprint_timeline, sprint_timeline_str, 'Calibri, 15', 1, 0, co0, 'ew')

    from Models.Role import get_role_name

    # cria uma lista com os usuários a serem avaliados pelo usuário logado
    # grades = [
    #       pendentes = indice 0
    #       avaliados = indice 1
    # ]
    grades = lista_usuarios_back.get_users(CURRENT_USER)

    # variavel com o tamanho das listas
    g = [len(grades[0]), len(grades[1])]

    # Cria o pie chart utilizando a informação de usuários
    if (sum(g) > 0) and current_rating_period(group_id) != None: criar_piechart(frame_section_header, g)
    
    # Cria o Frame parent de ambas as listas
    frame_listas_parent = criar_frame(frame_section, 3, 0, "nsew", co0 if g[1] == 0 else co0, co0, 0, 0, 0)
    frame_listas_parent.columnconfigure(0, weight = 1)
    if g[0] > 0: frame_listas_parent.rowconfigure(0, weight = 250 if g[1] == 0 else 10)
    if g[1] > 0: frame_listas_parent.rowconfigure(1, weight = 250 if g[0] == 0 else 10)
    frame_listas_parent.rowconfigure(2, weight = 1)

    # listas para facilitar o acesso a informações dentro do loop 'i'
    lista_titles = ['Integrantes ainda não Avaliados', 'Integrantes já Avaliados']
    if current_rating_period(group_id) == None:
        lista_titles = ['Integrantes a serem Avaliados', 'Integrantes a serem Avaliados']
        if next_rating_period(group_id) == None:
            lista_titles = ['Integrantes Avaliados', 'Integrantes Avaliados']
    
    # para cada lista
    for i, grade in enumerate(grades):
        glen=len(grade)

        # se a lista não possui usuários, ignore-a - não cria os frames da lista
        if len(grade) < 1: continue

        lista_col = [co0, co0][i]

        # Cria o frame da lista
        frame_lista = criar_frame(frame_listas_parent, i, 0, "news", lista_col, lista_col, 0, 0, 0)
        frame_lista.columnconfigure(0, weight = 1)
        frame_lista.rowconfigure(1, weight=1)

        # Coloca o título da lista 
        criar_label(frame_lista, lista_titles[i], 'Calibri, 14', 0, 0, [col_to_rate, col_rated][i], "we")

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
            frame_user = criar_frame(frame_parent_users, j, 0, 'nsew', lista_col, co0, 0, 0, 0)
            frame_user.columnconfigure(0, weight=1)

            # Cria um frame pro nome e role
            frame_user_data = criar_frame(frame_user, 0, 0, 'ew', lista_col, lista_col, 0, 0, 0)
            frame_user_data.columnconfigure(0, weight=1)

            # cria as labels de nome e role
            criar_label(frame_user_data, user.name, 'Calibri, 12', 0, 0, lista_col, "w")
            criar_label(frame_user_data, get_role_name(user.role_id), 'Calibri, 10', 1, 0, lista_col, "w")

            # Cria um frame pro botão
            if current_rating_period(group_id) != None:
                frame_user_button = criar_frame(frame_user, 0, 1, 'ew', co0, co0, 0, 0, 0)

            # insere o botão correspondente ao tipo da lista. Pendentes: avaliar; Avaliados: editar
            if i == 0 and current_rating_period(group_id) != None:
                criar_button(frame_user_button, 'Avaliar', 'Calibri, 12', 1, 1, lambda u=user: avaliar(u), "e"),
            # else: criar_button(frame_user_button, 'Editar Avaliação', 'Calibri, 12', 1, 1, lambda u=user: avaliar(u['id']), "w"),


# Cria a parte direita da tela, chamando a função apropriada dependendo do usuário logado e da sprint atual
def criar_section_2(sprints):
    
    # destroy o frame_section_2 anterior caso já exista 
    mf_children = module_frame.winfo_children()
    if mf_children and len(mf_children) > 2 and mf_children[1] is not None:
        from matplotlib import pyplot
        pyplot.close()
        mf_children[1].destroy()

    # Cria o frame principal da seção
    frame_section = criar_frame(module_frame, 0, 1, "nwes", co0, co0, 2, 0, 0)
    frame_section.columnconfigure(0, weight = 1)
    frame_section.rowconfigure(2, weight = 1)

    # caso o usuário logado seja instrutor
    if user_is_instructor: 
        criar_section_instructor(frame_section) # TODO: seção de instrutor
        return

    from Models.Sprint import previous_sprint, next_rating_period, current_rating_period
    from Authentication import CURRENT_USER

    # !!!!!!!!!! Nesse caso não utilizamos trigget('get_group_id') já que o usuário não é instrutor !!!!!!!!!!
    
    # pega a sprint anterior do grupo do usuário logado
    target_sprint = previous_sprint(CURRENT_USER.group_id)
    # if current_rating_period(CURRENT_USER.group_id) == None and next_rating_period(CURRENT_USER.group_id) == None:
    #     target_sprint = 'not none'

    # sem target_sprint: renderiza informações sobre a avaliação 360
    if target_sprint is None: criar_section_info(frame_section) # TODO: seção com informações da avaliação 360
    
    # caso contrario, cria a seção com informações sobre o usuário logado
    else: criar_section_profile(frame_section, sprints)


# Cria informações adicionais na seção 2 caso o usuário seja aluno
def criar_section_profile(frame_section, sprints):

    # Cria o frame de cabeçalho
    frame_section_header = criar_frame(frame_section, 0, 0, "we", co3, co3, 0, 0, 0)
    frame_section_header.columnconfigure(0, weight = 1)

    # Cria um frame para a label de título dentro do cabeçalho
    frame_header_title = criar_frame(frame_section_header, 0, 0, "ns", co0, co3, 0, 0, 0)
    criar_label(frame_header_title, 'Perfil', 'Calibri, 20', 0, 0, co3, 'nwes').configure(fg='white')

    from Authentication import CURRENT_USER
    from Models.Role import get_role_name
    from Models.Group import get_group_name
    from Models.Team import get_team_name

    # Cria o cabeçalho do perfil contendo informações do usuário: nome, função, grupo e time
    frame_header_data = criar_frame(frame_section_header, 1, 0, "ew", co0, co2, 2, 0, 0)
    frame_header_data.columnconfigure([0, 1], weight = 1)
    frame_header_data.columnconfigure([0, 1], weight = 1)
    criar_label(frame_header_data, f'Nome: {CURRENT_USER.name}', 'Calibri, 14', 0, 0, co0, 'w')
    (lambda d=get_role_name(CURRENT_USER.role_id):   criar_label(frame_header_data, f'Função: {d}', 'Calibri, 12', 1, 0, co0, 'w') if d is not None else None)()
    (lambda d=get_group_name(CURRENT_USER.group_id): criar_label(frame_header_data, f'Grupo: {d}', 'Calibri, 14', 0, 1, co0, 'e') if d is not None else None)()
    (lambda d=get_team_name(CURRENT_USER.team_id):   criar_label(frame_header_data, f'Time: {d}', 'Calibri, 12', 1, 1, co0, 'e') if d is not None else None)()

    # Cria o frame para o grafico pentagono
    frame_user_pentagon = criar_frame(frame_section, 1, 0, "ew", co0, co0, 0, 2, 2)
    frame_user_pentagon.columnconfigure(1, weight = 1)
    # frame_user_pentagon.rowconfigure(1, weight = 1)

    from graficos.Dashboards import user_pentagon
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    # Cria o gráfico pentagono
    figure = user_pentagon(CURRENT_USER.id, sprints[sel_sprint], co3, co3, 2.75, 2.25)

    # configura o canvas e adiciona a Figure do grafico
    canvas = FigureCanvasTkAgg(figure, master=frame_user_pentagon)
    canvas_tkw = canvas.get_tk_widget()
    canvas_tkw.columnconfigure(1, weight = 1)
    canvas_tkw.grid(row=0, column=0, sticky='wens')

    from Models.id_criteria import criteria, criteria_full

    # Cria um frame para a legenda do grafico pentagono
    frame_legenda = criar_frame(frame_user_pentagon, 0, 1, "nsew", co0, co2, 2, 8, 32)
    frame_legenda.columnconfigure(0, weight = 1)
    frame_legenda.rowconfigure([i for i in range(len(criteria))], weight = 1)

    from Models.Rating import get_ratings
    from graficos.Integrador import classify_criteria, medias

    # adquire as notas usuário 
    target_sprint = sprints[sel_sprint]
    ratings = get_ratings(to_user_id=CURRENT_USER.id, sprint_id=target_sprint.id)
    u_medias = medias(criteria, [classify_criteria(criteria, ratings)])[0]

    # cria um título no frame legenda
    frame_legenda_title = criar_frame(frame_legenda, 0, 0, "ew", co0, co2, 0, 4, 4)
    criar_label(frame_legenda_title, f'Médias durante a Sprint {sel_sprint+1}', 'Calibri, 10 bold', 0, 0, co0, 'we', 'center')

    # cria um frame pra cada critério contendo criteria, criteria_full e média do criterio
    for c_index, c in enumerate(criteria):
        frame_criterio = criar_frame(frame_legenda, c_index+1, 0, "nsew", co0, co2, 0, 4, 4)
        frame_criterio.columnconfigure(1, weight=1)
        criar_label(frame_criterio, f'{c}: ', 'Calibri, 10 bold', 0, 0, co0, 'we', 'center')
        criar_label(frame_criterio, f'{criteria_full[c_index]}: ', 'Calibri, 10', 0, 1, co0, 'we', 'center')
        criar_label(frame_criterio, f'{u_medias[c_index]:.1f}', 'Calibri, 10 bold', 0, 2, co0, 'e', 'center').configure(fg=co3)

    # cria um frame para renderizar o retorno dos feedbacks do usuario
    frame_section_feedbacks = criar_frame(frame_section, 2, 0, "nsew", co0, co0, 0, 0, 0)
    frame_section_feedbacks.columnconfigure(0, weight=1)
    frame_section_feedbacks.rowconfigure(2, weight=1)
    criar_retorno_feedbacks(frame_section_feedbacks, sprints)


# Cria a seção com o retorno de feedbacks recebidos e botões de selecionar sprint
def criar_retorno_feedbacks(frame_section_feedbacks, sprints):
    from Authentication import CURRENT_USER

    # cria um frame parent para o seletor de sprints e retorno de feedbacks
    frame_feedbacks = criar_frame(frame_section_feedbacks, 2, 0, "nsew", co0, co0, 0, 0, 0)
    frame_feedbacks.columnconfigure(0, weight=1)
    frame_feedbacks.rowconfigure(2, weight=1)

    # frame dos botões de selecionar sprint
    frame_sprint_selector = criar_frame(frame_feedbacks, 0, 0, "ew", co3, co3, 2, 0, 0)
    frame_sprint_selector.columnconfigure([i for i in range(len(sprints))], weight=1)

    # define a função que seleciona uma sprint ao clicar no botão
    def select_sprint(_, sprints, sprint_index):
        global sel_sprint
        sel_sprint = sprint_index
        criar_section_2(sprints)

    # Cria os botões que selecionam a sprint
    for index, _ in enumerate(sprints):
        sprint_btn = criar_button(frame_sprint_selector, f'Sprint {index+1}', 'Calibri, 12 bold', 0, index, lambda e=None, s=sprints, i=index: select_sprint(e, s, i), 'ew', 0)
        print(f'index: {index} | sel_sprint: {sel_sprint}')
        sprint_btn.configure(fg=co3 if index == sel_sprint else co1, bg=co1 if index == sel_sprint else co3)


    # oi Tânia
    from Utils.lista_usuarios_back import get_feedbacks
    feedbacks = get_feedbacks(CURRENT_USER.id, sprints[sel_sprint].id)
    # Cria um pseudo título para o retorno de feedbacks 
    frame_fb_title = criar_frame(frame_feedbacks, 1, 0, "ew", co0, co0, 4, 0, 0)
    criar_label(frame_fb_title, f'Feedbacks recebidos durante a Sprint {sel_sprint + 1}:', 'Calibri, 12 bold', 0, 0, co2, 'w', 'center').configure(fg='white')

    # Cria um frame parent pros feedbacks
    frame_feedback_list = criar_frame(frame_feedbacks, 2, 0, "nsew", co0, co0, 2, 2, 2)
    frame_feedback_list.columnconfigure(0, minsize=0, weight=1)
    frame_feedback_list.rowconfigure(0, minsize=0, weight=1)
    
    # substitui o frame pelo resultado retornado do add_scrollbar 
    from Front.Scrollbar import add_scrollbar
    frame_feedback_list = add_scrollbar(frame_feedback_list, co0, 0)

    from Models.id_criteria import criteria_full
    for index, criteria in enumerate(criteria_full):
        frame_criteria = criar_frame(frame_feedback_list, index, 0, "news", co0, co2, 2, 5, 5)
        frame_criteria.columnconfigure(0, weight=1)
        criar_label(frame_criteria, criteria, 'Calibri, 12 bold', 0, 0, co0, 'we', 'left')
        linha = 1
        for feedback in feedbacks:
            if feedback[0] == index:
                frame_fb = criar_frame(frame_criteria, linha, 0, "ns", co0, co0, 2, 4, 4)
                criar_label(frame_fb, f"\"{feedback[1]}\"", 'Calibri, 10', 0, 0, co0, 'we', 'left' )
                linha += 1




    # # cria cada feedback
    # for index, feedback in enumerate(feedbacks):
    #     frame_fb = criar_frame(frame_feedback_list, index, 0, "ns", co0, co0, 2, 4, 4)
    #     frame_fb.columnconfigure(0, weight=1)
    #     from Models.id_criteria import criteria_full
    #     criar_label(frame_fb, f'{criteria_full[feedback[0]]}: ', 'Calibri, 10 bold', 0, 0, co0, 'we', 'left')
    #     criar_label(frame_fb, feedback[1], 'Calibri, 10', 1, 0, co0, 'we', 'left').configure(wraplength=400, anchor='n')


# TODO: seção com as informações de instrutor
def criar_section_instructor(frame_section):
    pass # TODO




# TODO: seção com informações sobre a avaliação 360
def criar_section_info(frame_section):
    
    frame_ratings_info = criar_frame(frame_section, 1, 0, "ew", co0, co0, 0, 2, 2)
    criar_label(frame_ratings_info, ''' ''', 'Calibri, 10', 0, 0, co0, 'nw')
    criar_label(frame_ratings_info, 'Informações sobre a Avaliação 360°', 'Calibri, 15 bold', 1, 0, co0 , 'nwes')
    criar_label(frame_ratings_info, ''' ''', 'Calibri, 10', 2, 0, co0, 'nw')
    criar_label(frame_ratings_info, '       O que é?', 'Calibri, 13 bold', 3, 0, co0, 'nw')
    criar_label(frame_ratings_info, ''' ''', 'Calibri, 10', 4, 0, co0, 'nw')
    criar_label(frame_ratings_info, '''     Avaliação 360° é uma ferramenta onde um integrante de um time é analisado com base em suas competências por todos que compõem
    seu entorno educacional, como outros integrantes de mesma ou outra função, instrutores e ele mesmo (autoavaliação). 
    Utilizada principalmente para avaliar funções desempenhadas e para auxiliar no alinhamento de um membro específico do time ou do
    coletivo ao longo de um período específico. ''', 'Calibri, 10', 5, 0, co0, 'nw')
    criar_label(frame_ratings_info, ''' ''', 'Calibri, 10', 6, 0, co0, 'nw')
    criar_label(frame_ratings_info, '       Como é aplicada? ', 'Calibri, 13 bold', 7, 0, co0, 'nw')
    criar_label(frame_ratings_info, ''' ''', 'Calibri, 10', 8, 0, co0, 'nw')
    criar_label(frame_ratings_info, '''     A avaliação acontece por meio de um formulário composto por critérios relacionados às habilidades necessárias e comportamentos
    esperados para a execução das funções, onde todas as partes irão receber e dar uma nota para cada critério. As notas são de
    1 a 5, utilizando valores ordenados entre “Péssimo” e “Ótimo”.
    Para um resultado mais preciso, todas as avaliações são feitas possuindo os mesmos critérios para todos os integrantes. 
    Quando a nota atribuída for igual ou menor que 3, uma resposta descritiva precisará ser enviada obrigatoriamente pelo avaliador como
    um feedback qualitativo, para o aprimoramento do desempenho.''', 'Calibri, 10', 9, 0, co0, 'nw')
    criar_label(frame_ratings_info, ''' 
    
    ''', 'Calibri, 15', 10, 0, co0, 'nw')
    


# função que cria e coloca o grafico pentagono em um canvas dentro do frame parametro
def criar_piechart (module_frame, data):
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    frame_dashboards = criar_frame(module_frame,0, 1, "ne", co3, co3, 0, 0, 0)
    figure = graphic_pie(data)
    canvas = FigureCanvasTkAgg(figure, master = frame_dashboards)
    canvas.get_tk_widget().grid(row=0, column=0, sticky='e')

# função que cria o grafico pentagono com as informações parametro
def graphic_pie(data=list):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize = (1, 1), subplot_kw=dict(aspect="equal"))
    ax.set_anchor('E')
    def func (pct, allvals):
        absolute = int(pct/100.*sum(allvals))
        return "{:.0f}%\n({:d})".format(pct, absolute)
    _, _, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), textprops=dict(color="white"), colors=[col_to_rate, col_rated])
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    plt.setp(autotexts, size=7, weight='bold')
    fig.set_facecolor(co3)
    return fig

# função que muda para a tela de avaliação para o usuário parametro
def avaliar (user):

    from matplotlib import pyplot
    pyplot.close()

    from Front.Modules import avaliacao
    target_frame = module_frame.master
    module_frame.destroy()

    from Events import trigger
    trigger('sub_module_open')

    avaliacao.run(target_frame, user)
