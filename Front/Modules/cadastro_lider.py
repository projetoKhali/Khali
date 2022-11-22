from Front.Core import *
from tkinter import *


# Informações do modulo
NAME = 'Cadastrar'
REQUIRED_PERMISSIONS_REG = [3, 4, 5, 6, 7]
REQUIRED_PERMISSIONS_RATE = [None]
REQUIRED_PERMISSIONS_VIEW = [None]

# executa o modulo e retorna
def run (frame_parent):

    # Cria o frame principal do modulo
    module_frame=criar_frame(frame_parent, 0, 0, 'news', '#fae8e8', None, 0, 0, 0)
    module_frame.columnconfigure(0, weight=1) 
    module_frame.rowconfigure(1, weight=1) 

    # Cria um frame de cabeçalho
    frame_header = criar_frame(module_frame, 0, 0, 'new', co0)
    frame_header.columnconfigure(0, weight=4)
    frame_header.columnconfigure(1, weight=1) 

    # insere o titulo da tela no cabeçalho
    titulo=Label(frame_header, text='Cadastro de Sprints e Times', bg='#fae8e8', font='Calibre, 24')
    titulo.grid(row=0, column=0, padx=4, pady=10, sticky='w')

    # cria o frame body que contém o conteúdo da tela
    frame_body = criar_frame(module_frame, 1, 0, 'news', co0, None, 0, 0, 0)
    frame_body.rowconfigure(0, weight=1)
    frame_body.columnconfigure(0, weight=1)

    # adiciona scrollbar no frame_bogy
    from Front.Scrollbar import add_scrollbar
    frame_body = add_scrollbar(frame_body, co0, 0)

    # dados utilizados com o create_register_container para criar ambas as seções sprints / times
    titles = ['Sprints', 'Times']
    commands = [entry_sprint, entry_times]

    # cria os container de registro sprints / times
    for i in range(2):
        create_register_container(frame_body, i, titles[i], commands[i])

    # Cria o botão responsável por confirmar os cadastros 
    frame_confirm_btn = criar_frame(frame_header, 0, 1, 'ew', co0, px=8)
    frame_confirm_btn.grid_columnconfigure(0, weight=1)
    Button(frame_confirm_btn, text="Confirmar Cadastros", font="Calibri, 12", command=confirmar_cadastros, 
        activebackground='#c5a8b0', bg='#d9d9d9', fg='#1a1d1a', height=0).grid(row=0, column=0, sticky='news')

    # retorna o modulo
    return module_frame


# Função genérica que cria um container, base para os formulários de Sprint / Time
def create_register_container(frame_parent, row, title, command):

    # cria um frame container
    frame_container = criar_frame(frame_parent, row, 0, 'news', co0)
    frame_container.columnconfigure(0, weight=1)

    # cria um frame cabeçalho do container
    frame_header = criar_frame(frame_container, 0, 0, 'new', co3)
    frame_header.columnconfigure(0, weight=1)

    # cria um frame para conter o título
    frame_title = criar_frame(frame_header, 0, 0, 'w', co3)
    frame_title.columnconfigure(0, weight=1)

    # título, input
    criar_label(frame_title, f"Número de {title}:", "Calibri 12 bold", 0, 0, None, 'w').configure(width=20)

    # cria o frame que contém os items da lista desse container
    frame_list_wrapper = criar_frame(frame_container, 1, 0, 'news', co0, co0, 0, 4, 4)
    frame_list_wrapper.columnconfigure(0, weight=1)

    # inicializa uma IntVar para atualizar os items listados nesse container quando modificada
    var = IntVar()
    var.trace('w', lambda n, i, m, v=var, lw=frame_list_wrapper: command(v, lw))
    criar_entry(frame_title, "Calibri, 10", 0, 1, 'w', 8, 2).config(textvariable=var)


# função que pegar o valor da caixa de entrada do "n° de sprints, ao apertar o button.
# essa função também "abre um frame" para que as linhas referentes ao cadastro da sprint sejam encaixadas
def entry_sprint(en_numsprints:IntVar, frame_parent):

    # deleta o frame_list caso já exista
    children = frame_parent.winfo_children()
    if children is not None and len(children) > 0 and children[0] is not None:
        children[0].destroy()

    from Events import register, trigger, unregister_all

    # Chama o evento reset_sprints que deleta algumas reações de evento cadastradas
    # evita que reações inválidas sejam ativadas
    trigger('reset_sprints')

    # deleta as reações associadas ao reset_sprint e get_sprints que se tornaram obsoletas
    unregister_all('reset_sprints')
    unregister_all('get_sprints')

    # tenta pegar o valor da entry correspondente ao numero de sprints
    try: valor = int(en_numsprints.get())
    except: return

    # caso o valor seja 0, não cria o frame_list
    if valor < 1: return

    # Notifica o usuário caso o valor de entrada seja muito alto
    if valor > 12:    
        import tkinter.messagebox
        print("número muito grande de sprints!!, por favor, insira um valor menor")
        tkinter.messagebox.showinfo("Khali Group",  "número muito grande de sprints!!, por favor, insira um valor menor")

    # Cria o frame responsável por conter os formulários de Time
    frame_list = criar_frame(frame_parent, 0, 0, 'new', co0, co0, 0, 0, 0)
    frame_list.columnconfigure(0, weight=1)

    # define o numero de sprints utilizando o valor da entry, no máximo 12
    n_sprints = min(valor, 12)

    # Cadastra as reações de evento que retornam os valores de cada sprint
    register('reset_sprints', lambda n=n_sprints: [unregister_all(f'get_sprint_{i}') for i in range(n)])
    register('get_sprints', lambda n=n_sprints: [trigger(f'get_sprint_{i}') for i in range(n)])

    # pra cada sprint
    for i in range(n_sprints):

        # cria o frame da sprint
        frame_sprint = criar_frame(frame_list, i, 0, bg=co0)

        # cria a label com o nome da sprint
        criar_label(frame_sprint, f"Sprint {i+1}", "Calibri, 10 bold", 0, 0).config(padx=8)

        # inicializa uma lista de DateEntry 
        calendars = []

        # cria as DateEntry de inicio e fim da sprint
        for j, label_text in enumerate(['Início: ', 'Fim: ']):
            criar_label(frame_sprint, label_text, "Calibri, 10", 0, j*2 + 1)
            calendars.append(create_calendar(frame_sprint, 0, j*2 + 2))

        # cria a Entry de periodo avaliativo
        criar_label(frame_sprint, "Dias para avaliação:", "Calibri, 10", 0, 5)
        entry_rating_period = criar_entry(frame_sprint, "Calibri, 10", 0, 6)
        entry_rating_period.insert(0, '5')
        entry_rating_period.config(width=4)

        # cadastra o evento que retorna os dados da sprint
        register(f'get_sprint_{i}', lambda s=calendars[0], e=calendars[1], r=entry_rating_period: [s.get_date(), e.get_date(), r.get()])


# Cria a seção de cadastro de Times 
def entry_times(en_numtimes:IntVar, frame_parent):

    # deleta o frame_list caso já exista
    children = frame_parent.winfo_children()
    if children is not None and len(children) > 0 and children[0] is not None:
        children[0].destroy()

    from Events import register, trigger, unregister_all
    
    # Chama o evento reset_teams que deleta algumas reações de evento cadastradas
    # evita que reações inválidas sejam ativadas
    trigger('reset_teams')

    # deleta as reações associadas ao reset_team e get_teams que se tornaram obsoletas
    unregister_all('reset_teams')
    unregister_all('get_teams')

    # tenta pegar o valor da entry correspondente ao numero de times
    try: valor = get_entry_int(en_numtimes)
    except: return

    # caso o valor seja 0, não cria o frame_list
    if valor < 1: return

    # Notifica o usuário caso o valor de entrada seja muito alto
    if valor > 12:    
        import tkinter.messagebox
        tkinter.messagebox.showinfo("Khali Group",  "São muitos times! Insira um valor menor.")

    # Cria o frame responsável por conter os formulários de Time
    frame_list = criar_frame(frame_parent, 0, 0, 'new', co0, co0, 0, 0, 0)
    frame_list.columnconfigure(0, weight=1)

    # define o numero de times utilizando o valor da entry, no máximo 12
    n_times = min(valor, 12)

    # Cadastra as reações de evento que retornam os valores de cada time
    register('reset_teams', lambda n=n_times: [unregister_all(f'get_team_{i}') for i in range(n)])
    register('reset_teams', lambda n=n_times: [unregister_all(f'get_team_members_{i}') for i in range(n)])
    register('get_teams', lambda n=n_times: [trigger(f'get_team_{i}') for i in range(n)])

    # pra cada time
    for i in range(n_times):

        # cria o frame do time
        frame_time = criar_frame(frame_list, i, 0, 'ew', co0, co1, 0, 0, 0)
        frame_time.columnconfigure(0, weight=1)

        # cria um frame para as informações do time (nome, n de membros)
        frame_time_data = criar_frame(frame_time, 0, 0)

        # indice, nome, n membros
        criar_label(frame_time_data, f"Time {i+1}", "Calibri, 10", 0, 0)
        entry_name = criar_entry(frame_time_data,                          "Calibri, 10", 0, 2)
        criar_label(frame_time_data, "Quantidade de membros:", "Calibri, 10", 0, 3)

        # cria o frame responsável por armazenar a lista de membros
        frame_members_wrapper = criar_frame(frame_time, 1, 0, 'ew', co0, co0, 0, 2, 2)
        frame_members_wrapper.columnconfigure(0, weight=1)

        # inicializa uma IntVar que armazena o valor da Entry de numero de membros e atualiza os formularios quando modificada
        var = IntVar(value=3)
        var.trace('w', lambda n, i, m, v=var, lw=frame_members_wrapper, ti=i: update_member_forms(v, lw, ti))

        # cria a entry de numero de membros
        criar_entry(frame_time_data, "Calibri, 10", 0, 4).config(textvariable=var)

        # atualização inicial de formulários de membros
        update_member_forms(var, frame_members_wrapper, i)
        
        # cadastra a reação de evento que retorna os dados desse time
        register(f'get_team_{i}', lambda n=entry_name, ti=i: [n.get(), trigger(f'get_team_members_{ti}')])


# Atualiza a tela para criar os formularios para cada membro de acordo com o numero de membros especificado em cada time
def update_member_forms(en_num_members, frame_time, team_index):

    # deleta o frame_list caso já exista
    children = frame_time.winfo_children()
    if children is not None and len(children) > 0 and children[0] is not None:
        children[0].destroy()

    # tenta pegar o valor da entry correspondente ao numero de membros
    try: valor = get_entry_int(en_num_members)
    except: return

    # caso o valor seja 0, não cria o frame_lista
    if valor < 1: return

    # Cria o frame responsável por conter todos os formulários de membro desse time
    frame_list = criar_frame(frame_time, 0, 0, 'new', co1, co1, 0, 0, 0)
    frame_list.columnconfigure(0, weight=1)

    # para cada membro, cria um formulário de cadastro
    for i in range(min(max(valor, 3), 9)):
        create_member_form(frame_list, i, team_index)


# Cria os campos para o cadastro de UM membro
def create_member_form (parent, row, team_index):

    # Cria o frame do membro
    frame_member = criar_frame(parent, row, 0, 'ew', co1, None, 0, 4, 4)

    # Nome - Label e Entry
    criar_label(frame_member, "Nome:",  "Calibri, 10", 0, 0, co1)
    entry_name = criar_entry(frame_member, "Calibri, 10", 0, 1)

    # Email - Label e Entry
    criar_label(frame_member, "E-mail:","Calibri, 10", 0, 2, co1)
    entry_email = criar_entry(frame_member, "Calibri, 10", 0, 3)

    from Models.Role import get_role_name, get_role_id

    # inicializa uma StringVar para armazenar o valor do dropdown de Role
    entry_role = StringVar()

    # lista o nome das possiveis funções 
    role_names = [get_role_name(i) for i in [3, 4, 5]]

    # inicializa a StringVar como LT para o primeiro membro do time, PO para o segundo e Dev para os demais
    entry_role.set(role_names[min(row, 2)])

    # Role - Label e Dropdown
    criar_label(frame_member, "Função:","Calibri, 10", 0, 4, co1)
    OptionMenu(frame_member, entry_role, *role_names).grid(row=0, column=5)

    # Registra o retorno dos valores de entrada desse formulário de membro caso o time de indice team_index seja solicitado
    from Events import register
    register(f'get_team_members_{team_index}', lambda n=entry_name, e=entry_email, r=entry_role: [n.get(), e.get(), get_role_id(r.get())])


# Retorna o valor na entry especificada considerando erros
def get_entry_int (entry):

    # tenta acessar o valor na entry especificada e retorná-lo como int
    try: return int(entry.get())

    # em caso de erro, retorne 0
    except: print("cadastro_lider.get_entry_int -- erro")
    return 0


# Cria um calendario DateEntry para input de datas
def create_calendar(parent, r, c):
    from tkcalendar import DateEntry
    calendar = DateEntry(
        parent, date_pattern='dd/mm/yyyy', firstweekday='sunday', showweeknumbers=False, locale='pt_BR',
        background=co3, foreground='white', bordercolor=co1, headersbackground=co0
    )
    calendar.grid(row=r, column=c)
    return calendar


# coleta os valores dos campos preenchidos e conclui o cadastro de sprints, times e seus membros
def confirmar_cadastros():
    from Events import trigger
    from Models.Sprint import create_sprint
    from Models.Team import create_team

    from Authentication import CURRENT_USER, register

    # TODO: Integração com dropdown de selecionar grupo
    group_id = CURRENT_USER.group_id

    # Chama o evento para obter o retorno dos dados
    sprints = trigger('get_sprints')
    if sprints is not None:
        
        # cada item na lista representa uma sprint
        for sprint in sprints:
            create_sprint(group_id, sprint[0], sprint[1], sprint[2])

    # Chama o evento para obter o retorno dos dados
    teams = trigger('get_teams')
    if teams is not None:
        
        # cada item na lista representa um team
        for team in teams:

            # indice 0 = nome do time; indice 1 = membros
            team_id = create_team(team[0], group_id)
            for user in team[1]:

                # 0 = nome; 1 = email; 2 = role
                register(user[0], user[1], group_id, team_id, user[2])
