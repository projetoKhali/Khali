from Front.Core import *
from tkinter import *


# Informações do modulo
NAME = 'Cadastrar'
REQUIRED_PERMISSIONS_REG = [3, 4, 5, 6, 7]
REQUIRED_PERMISSIONS_RATE = [None]
REQUIRED_PERMISSIONS_VIEW = [None]

# executa o modulo e retorna
def run (frame_parent):
    # HIERARQUIA:
    #            janela
    #            |   janela_header                       # contém o titulo "Cadastro"
    #            |   frame_section0                      # separa a primeira seção da janela
    #            |   |   sprints_header                  # contem o cabeçalho do cadastro de sprints
    #            |   |   frame_parent_sprints            # contem cada sprint
    #            |   |   |   sprint_form                 # um sprint_form para cada sprint
    #            |   |   |   ...
    #            |   frame_section1                      # separa a segunda seção da janela
    #            |   |   teams_header                    # contem o cabeçalho do cacdastro de times
    #            |   |   frame_parent_times              # contem cada frame_time
    #            |   |   |   frame_time                  # um frame_time para cada time
    #            |   |   |   |   members_parent          # intermédio entre frame_time e cada membro
    #            |   |   |   |   |   member_form         # contem o formulário de um membro
    #            |   |   |   frame_time[...]
    #            |   |   |   frame_time[...]

    module_frame=criar_frame(frame_parent, 0, 0, 'news', '#fae8e8', None, 0, 0, 0)
    module_frame.columnconfigure(0, weight=1) 
    module_frame.rowconfigure(1, weight=1) 

    frame_header = criar_frame(module_frame, 0, 0, 'new', co0)
    frame_header.columnconfigure(0, weight=4)
    frame_header.columnconfigure(1, weight=1) 

    # janela_header
    titulo=Label(frame_header, text='Cadastro de Sprints e Times', bg='#fae8e8', font='Calibre, 24')
    titulo.grid(row=0, column=0, padx=4, pady=10, sticky='w')

    # frame_body = criar_frame(janela, 1, 0)
    frame_body = criar_frame(module_frame, 1, 0, 'news', co0, None, 0, 0, 0)
    frame_body.rowconfigure(0, weight=1)
    frame_body.columnconfigure(0, weight=1)
    from Front.Scrollbar import add_scrollbar
    frame_body = add_scrollbar(frame_body, co0, 0)
    # frame_body.rowconfigure(0, weight=1)
    # frame_body.columnconfigure(0, weight=1)

    titles = ['Sprints', 'Times']
    commands = [entry_sprint, entry_times]

    for i in range(2):
        create_register_container(frame_body, i, titles[i], commands[i])

    # Cria o botão responsável por efetuar os cadastros 
    frame_confirm_btn = criar_frame(frame_header, 0, 1, 'ew', 'red', px=8)
    frame_confirm_btn.grid_columnconfigure(0, weight=1)
    Button(frame_confirm_btn, text="Confirmar Cadastros", font="Calibri, 12", command=confirmar_cadastros, 
        activebackground='#c5a8b0', bg='#d9d9d9', fg='#1a1d1a', height=0).grid(row=0, column=0, sticky='news')

    # retorna o modulo
    return module_frame


# Retorna o valor na entry especificada
def get_entry_int (entry):

    # tenta acessar o valor na entry especificada e retorná-lo como int
    try: return int(entry.get())

    # em caso de erro, retorne 0
    except: print("cadastro_lider.get_entry_int -- erro")
    return 0


def get_entries(parent):
    lista = []
    for child in parent.winfo_children():
        if type(child) is Entry:
            lista.append(child)
    return lista


def create_register_container(frame_parent, row, title, command):

    # cria a seção de sprints
    frame_container = criar_frame(frame_parent, row, 0, 'news', co0)
    frame_container.columnconfigure(0, weight=1)

    frame_header = criar_frame(frame_container, 0, 0, 'new', co3)
    frame_header.columnconfigure(0, weight=1)

    frame_title = criar_frame(frame_header, 0, 0, 'w', co3)
    frame_title.columnconfigure(0, weight=1)

    # título, input
    criar_label(frame_title, f"Número de {title}:", "Calibri 12 bold", 0, 0, None, 'w').configure(width=20)
    # criar_label(frame_header, f"Número de {title}: ", "Calibri 10", 1, 0, 'pink', 'w')

    frame_list_wrapper = criar_frame(frame_container, 1, 0, 'news', co0, co0, 0, 4, 4)
    frame_list_wrapper.columnconfigure(0, weight=1)

    var = IntVar()
    var.trace('w', lambda n, i, m, v=var, lw=frame_list_wrapper: command(v, lw))
    criar_entry(frame_title, "Calibri, 10", 0, 1, 'w', 8, 2).config(textvariable=var)

    # frame_btn = criar_frame(frame_header, 0, 1, 'w', co3)
    # frame_btn.columnconfigure(0, weight=1)

    # criar_button(frame_btn, "Aplicar", "Calibri, 10", 0, 0, (lambda var=var, lw=frame_list_wrapper: command(var, lw)), 'e')

# função que pegar o valor da caixa de entrada do "n° de sprints, ao apertar o button.
# essa função também "abre um frame" para que as linhas referentes ao cadastro da sprint sejam encaixadas
def entry_sprint(en_numsprints:IntVar, frame_parent):
    
    children = frame_parent.winfo_children()
    if children is not None and len(children) > 0 and children[0] is not None:
        children[0].destroy()

    from Events import register, trigger, unregister_all
    trigger('reset_sprints')
    unregister_all('reset_sprints')
    unregister_all('get_sprints')

    try: valor = int(en_numsprints.get())
    except: return
    if valor < 1: return

    frame_parent.config(bg='green')

    frame_list = criar_frame(frame_parent, 0, 0, 'new', co0, co0, 0, 0, 0)
    frame_list.columnconfigure(0, weight=1)

    n_sprints = min(valor, 13)

    register('reset_sprints', lambda n=n_sprints: [unregister_all(f'get_sprint_{i}') for i in range(n)])
    register('get_sprints', lambda n=n_sprints: [trigger(f'get_sprint_{i}') for i in range(n)])

    # frame_sprint = criar_frame(janela, valor, 4, 3, 2)
    for i in range(n_sprints):
        frame_sprint = criar_frame(frame_list, i, 0, bg='blue')

        criar_label(frame_sprint, f"Sprint {i+1}", "Calibri, 10 bold", 0, 0).config(padx=8)

        calendars = []

        for j, label_text in enumerate(['Início: ', 'Fim: ']):
            criar_label(frame_sprint, label_text, "Calibri, 10", 0, j*2 + 1)
            calendars.append(create_calendar(frame_sprint, 0, j*2 + 2))

        criar_label(frame_sprint, "Dias para avaliação:", "Calibri, 10", 0, 5)
        entry_rating_period = criar_entry(frame_sprint, "Calibri, 10", 0, 6)
        entry_rating_period.insert(0, '5')
        entry_rating_period.config(width=4)

        register(f'get_sprint_{i}', lambda s=calendars[0], e=calendars[1], r=entry_rating_period: [s.get_date(), e.get_date(), r.get()])

    if valor > 12:    
        import tkinter.messagebox
        print("número muito grande de sprints!!, por favor, insira um valor menor")
        tkinter.messagebox.showinfo("Khali Group",  "número muito grande de sprints!!, por favor, insira um valor menor")

def create_calendar(parent, r, c):
    from tkcalendar import DateEntry
    calendar = DateEntry(
        parent, date_pattern='dd/mm/yyyy', firstweekday='sunday', showweeknumbers=False, locale='pt_BR',
        background=co3, foreground='white', bordercolor=co1, headersbackground=co0
    )
    calendar.grid(row=r, column=c)
    return calendar

def entry_times(en_numtimes:IntVar, frame_parent):
    children = frame_parent.winfo_children()
    if children is not None and len(children) > 0 and children[0] is not None:
        children[0].destroy()

    from Events import register, trigger, unregister_all
    trigger('reset_times')
    unregister_all('reset_times')
    unregister_all('get_teams')

    try: valor = get_entry_int(en_numtimes)
    except: return
    if valor < 1: return

    frame_list = criar_frame(frame_parent, 0, 0, 'new', co0, co0, 0, 0, 0)
    frame_list.columnconfigure(0, weight=1)

    n_times = min(valor, 13)

    register('reset_times', lambda n=n_times: [unregister_all(f'get_team_{i}') for i in range(n)])
    register('reset_times', lambda n=n_times: [unregister_all(f'get_team_members_{i}') for i in range(n)])
    register('get_teams', lambda n=n_times: [trigger(f'get_team_{i}') for i in range(n)])

    for i in range(n_times):
        frame_time = criar_frame(frame_list, i, 0, 'ew', co0, co1, 0, 0, 0)
        frame_time.columnconfigure(0, weight=1)

        frame_time_data = criar_frame(frame_time, 0, 0)

        criar_label(frame_time_data, f"Time {i+1}", "Calibri, 10", 0, 0)
        entry_name = criar_entry(frame_time_data,                          "Calibri, 10", 0, 2)
        criar_label(frame_time_data, "Quantidade de alunos:", "Calibri, 10", 0, 3)

        frame_members_wrapper = criar_frame(frame_time, 1, 0, 'ew', co0, co0, 0, 2, 2)
        frame_members_wrapper.columnconfigure(0, weight=1)

        var = IntVar(value=3)
        var.trace('w', lambda n, i, m, v=var, lw=frame_members_wrapper, ti=i: update_member_forms(v, lw, ti))

        criar_entry(frame_time_data, "Calibri, 10", 0, 4).config(textvariable=var)

        update_member_forms(var, frame_members_wrapper, i)
        
        register(f'get_team_{i}', lambda n=entry_name, ti=i: [n.get(), trigger(f'get_team_members_{ti}')])


    if valor > 12:    
        import tkinter.messagebox
        tkinter.messagebox.showinfo("Khali Group",  "São muitos times! Insira um valor menor.")


# Atualiza a tela para criar os formularios para cada membro de acordo com o numero de membros especificado em cada time
def update_member_forms(en_num_members, frame_time, team_index):
    children = frame_time.winfo_children()
    if children is not None and len(children) > 0 and children[0] is not None:
        children[0].destroy()

    try: valor = get_entry_int(en_num_members)
    except: return
    if valor < 1: return

    frame_list = criar_frame(frame_time, 0, 0, 'new', co1, co1, 0, 0, 0)
    frame_list.columnconfigure(0, weight=1)

    # para cada aluno, cria um formulário de cadastro
    for i in range(min(max(valor, 3), 9)):
        criar_formulario_aluno(frame_list, i, team_index)


# Cria os campos para o cadastro de UM aluno
def criar_formulario_aluno (parent, row, team_index):
    frame_member = criar_frame(parent, row, 0, 'ew', co1, None, 0, 4, 4)
    criar_label(frame_member, "Nome:",  "Calibri, 10", 0, 0, co1)
    entry_name = criar_entry(frame_member, "Calibri, 10", 0, 1)
    criar_label(frame_member, "E-mail:","Calibri, 10", 0, 2, co1)
    entry_email = criar_entry(frame_member, "Calibri, 10", 0, 3)
    criar_label(frame_member, "Função:","Calibri, 10", 0, 4, co1)

    from Models.Role import get_role_name, get_role_id

    entry_role = StringVar()
    role_names = [get_role_name(i) for i in [3, 4, 5]]
    entry_role.set(role_names[min(row, 2)])
    OptionMenu(
        frame_member,

        # variavel que armazenará o valor da nova role quando selecionada no OptionMenu
        entry_role,

        # lista que contém os valores selecionaveis no OptionMenu
        *role_names,

        # comando que será executado ao selecionar uma opção
        # command=(lambda _, md=member_data, rs = role_selected : update_role(_, md, get_role_id(rs.get())))
    ).grid(row=0, column=5)

    from Events import register
    register(f'get_team_members_{team_index}', lambda n=entry_name, e=entry_email, r=entry_role: [n.get(), e.get(), get_role_id(r.get())])


# coleta os valores dos campos preenchidos e conclui o cadastro de sprints, times e seus membros
def confirmar_cadastros():
    from Events import trigger
    from Models.Sprint import create_sprint
    from Models.Team import create_team

    from Authentication import CURRENT_USER, register

    group_id = CURRENT_USER.group_id

    sprints = trigger('get_sprints')
    if sprints is not None:
        for sprint in sprints:
            create_sprint(group_id, sprint[0], sprint[1], sprint[2])

    teams = trigger('get_teams')
    if teams is not None:
        for team in teams:
            team_id = create_team(team[0], group_id)
            for user in team[1]:
                register(user[0], user[1], group_id, team_id, user[2])
