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
    frame_header.grid_columnconfigure(0, weight=1)

    # janela_header
    titulo=Label(frame_header, text='Cadastro de Times', bg='#fae8e8', font=('Calibre', 30))
    titulo.grid(row=0, column=0, padx=30, pady=10, sticky='w')

    # frame_body = criar_frame(janela, 1, 0)
    frame_body = criar_frame(module_frame, 1, 0, 'news', co0, None, 0, 0, 0)
    frame_body.grid_rowconfigure(0, weight=1)
    frame_body.grid_columnconfigure(0, weight=1)
    from Front.Scrollbar import add_scrollbar
    frame_body = add_scrollbar(frame_body, co0, 0)
    # frame_body.grid_rowconfigure(0, weight=1)
    # frame_body.grid_columnconfigure(0, weight=1)

    titles = ['Sprints', 'Times']
    commands = [entry_sprint, entry_times]

    for i in range(2):
        create_register_container(frame_body, i, titles[i], commands[i])

    # Cria o botão responsável por efetuar os cadastros 
    Button(frame_header, text="Confirmar Cadastros", font="Calibri, 12", command=confirmar_cadastros, 
        activebackground='#c5a8b0', bg='#d9d9d9', fg='#1a1d1a', height=0).grid(row=0, column=1, sticky='e')

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

    try: valor = int(en_numsprints.get())
    except: return
    if valor < 1: return

    frame_list = criar_frame(frame_parent, 0, 0, 'new', co0, co0, 0, 0, 0)
    frame_list.columnconfigure(0, weight=1)

    # frame_sprint = criar_frame(janela, valor, 4, 3, 2)
    for i in range(min(valor, 13)):
        frame_sprint = criar_frame(frame_list, i, 0)
        criar_label(frame_sprint, f"Sprint {i+1}", "Calibri, 10", 0, 0)
        criar_label(frame_sprint, "Início:", "Calibri, 10", 0, 1)
        criar_entry(frame_sprint, "Calibri, 10", 0, 2)
        criar_label(frame_sprint, "Fim:", "Calibri, 10", 0, 3)
        criar_entry(frame_sprint, "Calibri, 10", 0, 4)
        criar_label(frame_sprint, "Dias para avaliação:", "Calibri, 10", 0, 5)
        criar_entry(frame_sprint, "Calibri, 10", 0, 6)
    if valor > 12:    
        import tkinter.messagebox
        print("número muito grande de sprints!!, por favor, insira um valor menor")
        tkinter.messagebox.showinfo("Khali Group",  "número muito grande de sprints!!, por favor, insira um valor menor")


def entry_times(en_numtimes:IntVar, frame_parent):
    children = frame_parent.winfo_children()
    if children is not None and len(children) > 0 and children[0] is not None:
        children[0].destroy()

    try: valor = get_entry_int(en_numtimes)
    except: return
    if valor < 1: return

    frame_list = criar_frame(frame_parent, 0, 0, 'new', co0, co0, 0, 0, 0)
    frame_list.columnconfigure(0, weight=1)

    for i in range(min(valor, 13)):
        frame_time = criar_frame(frame_list, i, 0, 'ew', co0, co1, 0, 0, 0)
        frame_time.columnconfigure(0, weight=1)
        frame_time_data = criar_frame(frame_time, 0, 0)
        criar_label(frame_time_data, f"Time {i+1}",          "Calibri, 10", 0, 0)
        criar_entry(frame_time_data,                          "Calibri, 10", 0, 2)
        criar_label(frame_time_data, "Quantidade de alunos:", "Calibri, 10", 0, 3)
        frame_members_wrapper = criar_frame(frame_time, 1, 0, 'ew', co0, co0, 0, 2, 2)
        frame_members_wrapper.columnconfigure(0, weight=1)
        var = IntVar(value=3)
        var.trace('w', lambda n, i, m, v=var, lw=frame_members_wrapper: update_member_forms(v, lw))
        criar_entry(frame_time_data,                          "Calibri, 10", 0, 4).config(textvariable=var)
        update_member_forms(var, frame_members_wrapper)
        # criar_button(frame_time_data, "Cadastrar",           "Calibri, 10", 0, 5, command = update_member_forms)
    if valor > 12:    
        import tkinter.messagebox
        tkinter.messagebox.showinfo("Khali Group",  "São muitos times! Insira um valor menor.")


# Atualiza a tela para criar os formularios para cada membro de acordo com o numero de membros especificado em cada time
def update_member_forms(en_num_members, frame_time):

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
        criar_formulario_aluno(frame_list, i)


# Cria os campos para o cadastro de UM aluno
def criar_formulario_aluno (parent, row):
    frame_member = criar_frame(parent, row, 0, 'ew', co1, None, 0, 4, 4)
    criar_label(frame_member, "Nome:",  "Calibri, 10", 0, 0, co1)
    criar_entry(frame_member,           "Calibri, 10", 0, 1)
    criar_label(frame_member, "E-mail:","Calibri, 10", 0, 2, co1)
    criar_entry(frame_member,           "Calibri, 10", 0, 3)
    criar_label(frame_member, "Função:","Calibri, 10", 0, 4, co1)
    criar_entry(frame_member,           "Calibri, 10", 0, 5)
    # TODO:
    # from Roles.Role import *
    # roles = ...
    # criar_dropdown(parent, roles,"Calibri, 10", row, 5)


# coleta os valores dos campos preenchidos e conclui o cadastro de sprints, times e seus membros
def confirmar_cadastros(frame_parent_sprints, frame_parent_times):

    # importa cores do console para finalidade de debug
    from Settings import COLS

    # importa o método que cria sprints
    from Models.Sprint import create_sprint

    # importa as informações do atual usuário logado no sistema
    from Authentication import CURRENT_USER

    # define a função que converte o valor do tipo string 'value' em um valor do tipo date 
    def to_date(value:str):

        # importa a biblioteca que contém a classe date
        from datetime import date

        # divide o valor fornecido em uma lista contendo as seções separadas por /
        l = value.split('/')

        # retorna uma nova date utilizando os valores 1, 2 e 3 da lista
        # l[0] = DD
        # l[1] = MM
        # l[2] = AAAA
        # Obs.: a classe date utilizada o formato americano. Para a exibição, ela retornará "AAAA/MM/DD".
        #       Para ser criada corretamente, os valores estão sendo passados na ordem 2,1,0 em vez de 0,1,2.
        #       Caso contrário, o usuário teria que preencher 'AAAA/MM/DD' na entry da tela
        return date(
            int(l[2]),
            int(l[1]),
            int(l[0])
        )

    # acessa as children to frame_parent_sprints e executa o próximo loop
    sprints = frame_parent_sprints.winfo_children()
    for frame_sprint in sprints:

        # acessa o frame que contém as informações do time
        #           frame_parent_times
        #           |  [x] frame_sprint.get_entries():         <--
        #           |   |  [0] inicio
        #           |   |  [1] fim
        #           |   |  [2] periodo de avaliação
        try:
            s_entries = get_entries(frame_sprint)
            inicio = to_date(s_entries[0].get())
            fim =    to_date(s_entries[1].get())
            periodo = get_entry_int(s_entries[2])
            create_sprint(CURRENT_USER.group_id, inicio, fim, periodo)
        except:
            print(COLS[2] + f'Erro ao criar sprint: {frame_sprint}' + COLS[0])

    # Importa as funções de criar time e cadastro de usuário
    from Authentication import register
    from Models.Team import create_team

    # acessa as children do frame_parent_times e executa o próximo loop
    times = frame_parent_times.winfo_children()
    for frame_time in times:

        # acessa o frame que contém as informações do time
        #           frame_parent_times
        #           |  [x] frame_time
        #           |   |  [0] time_data        <--
        #           |   |   |   nome
        #           |   |   |   qtd alunos
        time_data = frame_time.winfo_children()[0]
        name = str(get_entries(time_data)[0].get())
        team_id = create_team(name, CURRENT_USER.group_id)

        # acessa os frames de 'member' dentro do child 1 do frame_time
        #           |   |  [x] frame_time
        #           |   |   |  [1] members      <--
        #           |   |   |   |  [0] member 0
        #           |   |   |   |  [1] member 1
        #           |   |   |   |  [2] member 2
        for member in frame_time.winfo_children()[1].winfo_children():

            # print(f'member {member}')
            # m_entries = get_entries(member)
            # print(f'm_entries {member.winfo_children()}')

            # Acessa as entries dentro do frame 'member' para adquirir os valores necessarios pro cadastro
            #       |   |   |   |  [x] member x
            #       |   |   |   |   |  [0] label "nome:"
            #       |   |   |   |   |  [1] entry {nome}
            #       |   |   |   |   |  [2] label "email:"
            #       |   |   |   |   |  [3] entry {email}
            #       |   |   |   |   |  [4] label "role:"
            #       |   |   |   |   |  [5] entry {role}
            try:
                m_name = member.winfo_children()[1].get()
                m_email = member.winfo_children()[3].get()
                m_role = get_entry_int(member.winfo_children()[5])
                register(m_name, m_email, CURRENT_USER.group_id, team_id, m_role)
            except:
                print(COLS[2] + f'Erro ao criar membro: {member}' + COLS[0])
                continue

