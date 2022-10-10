from Utils import edit_team_back
from tkinter import *

from CSV.CSVHandler import find_data_list_by_field_value_csv
from Users.Authentication import CURRENT_USER
from Settings import USERS_PATH, TEAMS_PATH
from Models.Teams import get_team_name, get_team_id
from Models.Role import get_role_name, get_role_id

# cores
co0 = "#FAE8E8"  # rosa
co1 = "#D9D9D9"  # cinza
co2 = "#1A1D1A"  # preta
co3 = "#26413C"  # verde

# Informações do modulo
NAME = 'Editar'
REQUIRED_PERMISSIONS_REG  = [
    [3, 4, 5]
]
REQUIRED_PERMISSIONS_RATE = [None]
REQUIRED_PERMISSIONS_VIEW = [None]

master_frame = None

def run(frame_parent):

    global master_frame

    # module_frame = Frame(frame_parent)
    # module_frame.columnconfigure(0, minsize = 0, weight = 1)
    # module_frame.grid(row=0, column=0, sticky='nsew')



    # Criar um frame para comportar o canvas
    frm_main=Frame(frame_parent, bg=co0)
    # frm_main.pack(fill=BOTH, expand=1) 
    frm_main.columnconfigure(0, minsize = 0, weight = 1)
    frm_main.rowconfigure(0, minsize = 0, weight = 1)
    frm_main.grid(row=0, column=0, sticky='nsew')

    # O canvas aceita o scrollbar, mas ela só faz o papel da responsividade
    canvas=Canvas(frm_main, bg=co0)
    # canvas.pack(side=LEFT, fill=BOTH, expand=1)
    canvas.columnconfigure(0, minsize = 0, weight = 1)
    canvas.grid(row=0, column=0, sticky='nsew')

    # Configurações do scrollbar
    scrollbar_ver = Scrollbar(frm_main, orient=VERTICAL, command=canvas.yview) # Comando xview para orientação HORIZONTAL
    # scrollbar_ver.pack(side=RIGHT, fill=Y)
    scrollbar_ver.grid(row=0, column=1, sticky='nsw')

    # Configurações do canvas
    canvas.configure(yscrollcommand=scrollbar_ver.set) # xscrollcomand para barra horizontal

    parent_module=Frame(canvas, bg=co0, relief=FLAT, bd=3,) # Não colocamos o frame com o .pack nesse caso
    parent_module.columnconfigure(0, minsize = 0, weight = 1)
    parent_module.grid(row=0, column=0, sticky='nsew')
    # parent_module.pack(side=LEFT, fill=X, expand=1)

    parent_module.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar

    # inbetween_frame = Frame(parent_module, bg='yellow', padx=2, pady=2)
    # inbetween_frame.columnconfigure(0, minsize = 0, weight = 1)
    # inbetween_frame.grid(row=0, column=0, sticky='nsew')

    module_frame = Frame(parent_module, bg=co0)
    module_frame.columnconfigure(0, minsize = 800, weight = 1)
    module_frame.grid(row=0, column=0, sticky="news")
    # module_frame.pack(side=LEFT, fill=BOTH, expand=1)

    # return 

    # Integração do frame geral a uma janela do canvas
    canvas.create_window((0,0), window=parent_module, anchor='nw')


    master_frame = frm_main

    # section 0
    frame_title = Frame(module_frame, padx=2, pady=2, bg=co3)
    frame_title.grid(row=0, column=0, sticky='we')

    Label(frame_title, text="Editar Times", font='Calibri, 20', bg=co3, fg='white').grid(row=0, column=0)

    # section 1
    frame_teams = Frame(module_frame, padx=2, pady=2, bg=co0)
    frame_teams.rowconfigure(1, minsize = 0, weight = 1)
    frame_teams.columnconfigure(0, minsize = 0, weight = 1)
    frame_teams.grid(row=1, column=0, sticky="ew")

    # print(f'group_id:{CURRENT_USER.group_id}')

    # seleciona os times pertencentes ao grupo do usuario logado
    teams_list = find_data_list_by_field_value_csv(TEAMS_PATH, 'group', CURRENT_USER.group_id)
    # print(f'times:{teams_list}')

    # pra cada time
    for team_id, time_data in enumerate(teams_list):
        frame_members_parent = create_team(frame_teams, time_data, team_id)

        # seleciona os membros do time
        members_list = find_data_list_by_field_value_csv(USERS_PATH, 'team_id', team_id)

        # para cada membro
        for member_id, member_data in enumerate(members_list):
            frame_member_actions = create_member(frame_members_parent, member_data, member_id)
            create_member_role(frame_member_actions, member_data, co0 if member_id % 2 == 1 else 'white')
            create_member_remove(frame_member_actions, member_data)


    # seleciona todos os usuarios com role 3, 4 ou 5 que não possuam time 
    no_team_users = [i for i in find_data_list_by_field_value_csv(USERS_PATH, 'team_id', '') if int(i['role_id']) in [3, 4, 5]]

    # retorna caso não existam usuários sem time
    # print(len(no_team_users))
    if len(no_team_users) > 0:

        frame_no_team_members_parent = create_team(frame_teams, None, team_id+1)

        for user_id, no_team_user_data in enumerate(no_team_users):
            frame_member_actions = create_member(frame_no_team_members_parent, no_team_user_data, user_id)
            create_member_add(frame_member_actions, no_team_user_data, teams_list)

    f = Frame(module_frame, pady=100, bg=co0)
    Label(f, text='', bg=co0).grid(row=0, column=0, sticky="s")
    f.grid(row=100, column=0, sticky="s")


def create_team(frame_teams_parent, team_data, team_id):

    # cria o frame do time
    frame_team = Frame(frame_teams_parent, bg=co1)
    frame_team.columnconfigure(0, minsize = 0, weight = 1)
    frame_team.grid(row=team_id, column=0, sticky="ew")

    # coloca o nome do time
    team_name = 'Usuários sem time'
    if team_data is not None: team_name = get_team_name(int(team_data['id']))
    Label(frame_team, text=team_name, font='Calibri, 16', bg=co1).grid(row=0, column=0)

    frame_members_parent = Frame(frame_team)
    frame_members_parent.columnconfigure(0, minsize = 0, weight = 1)
    frame_members_parent.grid(row=team_id+1, column=0, sticky="ew")

    return frame_members_parent

def create_member(frame_members_parent, member_data, row):

    color = co0 if row % 2 == 1 else 'white'

    # cria um frame para o membro dentro do frame_time
    frame_member = Frame(frame_members_parent, padx=2, pady=2, bg=color)
    frame_member.columnconfigure(0, minsize = 0, weight = 1)
    frame_member.grid(row=row, column=0, sticky="we")

    # coloca o nome do membro
    frame_member_name = Frame(frame_members_parent, padx=2, pady=2, bg=color)
    # frame_member_name.columnconfigure(0, minsize = 0, weight = 1)
    frame_member_name.grid(row=row, column=0, sticky="w")
    Label(frame_member_name, text=member_data['name'], font='Calibri, 12', justify='left', padx=2, pady=2, bg=color).grid(row=0, column=0, sticky="ew")

    # cria um frame parent para as ações
    frame_actions = Frame(frame_member, bg=color)
    frame_actions.columnconfigure(0, minsize = 0, weight = 1)
    frame_actions.grid(row=0, column=1, sticky="w")

    return frame_actions

def create_member_role(frame_member_actions, member_data, color):

    # cria o frame e dropdown de role dentro do ações
    frame_dropdown = Frame(frame_member_actions, bg=color)
    frame_dropdown.grid(row=0, column=0)
    role_selected = StringVar()

    role_selected.set(get_role_name(int(member_data['role_id'])))
    OptionMenu(
        frame_dropdown,

        # variavel que armazenará o valor da nova role quando selecionada no OptionMenu
        role_selected,

        # lista que contém os valores selecionaveis no OptionMenu
        *["Líder Técnico", "Product Owner", "Developer"],

        # comando que será executado ao selecionar uma opção
        command=(lambda _, md=member_data, rs = role_selected : update_role(_, md, get_role_id(rs.get())))
    ).grid(row=0, column=0)

def create_member_add(frame_member_actions, member_data, teams_list):

    frame_adicionar = Frame(frame_member_actions)
    frame_adicionar.grid(row=0, column=1)
    team_selected = StringVar()
    team_selected.set('Adicionar ao Time')
    OptionMenu(
        frame_adicionar,

        # variavel que armazenará o valor da nova role quando selecionada no OptionMenu
        team_selected,

        # lista que contém os valores selecionaveis no OptionMenu
        *[team['name'] for team in teams_list],

        # comando que será executado ao selecionar uma opção
        command=(lambda _, md=member_data, ts = team_selected : add_member(md, get_team_id(ts.get())))
    ).grid(row=0, column=0)

def create_member_remove(frame_member_actions, member_data):

    # cria o frame e button remover dentro do ações
    frame_remover = Frame(frame_member_actions)
    frame_remover.grid(row=0, column=1)
    Button(
        frame_remover,
        text='remover',
        font='Calibri, 12',
        padx=8, pady=2,

        # comando que será executado ao clicar: 
        # chama a função remove_member com o member_data atual do loop como parametro
        command=lambda md=member_data:remove_member(md)
    ).grid(row=0, column=0)

def redraw():
    global master_frame
    if master_frame is None:
        print(f'edit_team.redraw -- ERRO: redraw() sendo executado enquanto master_frame é None')
    frame_parent = master_frame.master
    master_frame.destroy()
    run(frame_parent)

from Utils import edit_team_back

def update_role(_, member_data, new_role):
    # print(member_data['name'])
    # print(new_role)
    edit_team_back.change_role(member_data['team_id'], member_data['email'], new_role)
    redraw()

def add_member(member_data, team_id):
    # print(member_data)
    edit_team_back.add_user(member_data['email'], team_id)
    redraw()

def remove_member(member_data):
    # print(member_data)
    edit_team_back.delete_user(member_data['email'])
    redraw()

