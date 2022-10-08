from Utils import edit_team_back
from tkinter import *

from CSV.CSVHandler import find_data_list_by_field_value_csv
from Users.Authentication import CURRENT_USER
from Settings import USERS_PATH, TEAMS_PATH
from Models.Teams import get_team_name
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

def run(frame_parent):

    # cria o frame do módulo
    module_frame = Frame(frame_parent, padx=2, pady=2, )
    # module_frame.rowconfigure(0, minsize = 0, weight = 1)
    module_frame.columnconfigure(0, minsize = 0, weight = 1)
    module_frame.grid(row=0, column=0, sticky="news")

    # section 0
    frame_title = Frame(module_frame, padx=2, pady=2, bg=co3)
    frame_title.grid(row=0, column=0, sticky='we')

    Label(frame_title, text="Editar Times", font='Calibri, 20', bg=co3, fg='white').grid(row=0, column=0)

    # section 1
    frame_teams = Frame(module_frame, padx=2, pady=2, )
    frame_teams.rowconfigure(1, minsize = 0, weight = 1)
    frame_teams.columnconfigure(0, minsize = 0, weight = 1)
    frame_teams.grid(row=1, column=0, sticky="ew")

    print(f'group_id:{CURRENT_USER.group_id}')

    # seleciona os times pertencentes ao grupo do usuario logado
    teams_list = find_data_list_by_field_value_csv(TEAMS_PATH, 'group', CURRENT_USER.group_id)
    print(f'times:{teams_list}')

    # pra cada time
    for i, time_data in enumerate(teams_list):
        create_team(frame_teams, time_data, i)

def create_team(frame_teams_parent, team_data, row):

    # cria o frame do time
    frame_team = Frame(frame_teams_parent, bg=co1)
    frame_team.columnconfigure(0, minsize = 0, weight = 1)
    frame_team.grid(row=row, column=0, sticky="ew")

    # coloca o nome do time
    Label(frame_team, text=get_team_name(int(team_data['id'])), font='Calibri, 16', bg=co1).grid(row=0, column=0)

    # seleciona os membros do time
    members_list = find_data_list_by_field_value_csv(USERS_PATH, 'team_id', row)

    frame_members_parent = Frame(frame_team)
    frame_members_parent.columnconfigure(0, minsize = 0, weight = 1)
    frame_members_parent.grid(row=row+1, column=0, sticky="ew")

    # para cada membro
    for i, member_data in enumerate(members_list):
        create_member(frame_members_parent, member_data, i)


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

    # cria o frame e dropdown de role dentro do ações
    frame_dropdown = Frame(frame_actions, bg=color)
    frame_dropdown.grid(row=0, column=0)
    role_selected = StringVar()
    role_selected.set(get_role_name(int(member_data['role_id'])))
    OptionMenu(
        frame_dropdown,

        # variavel que armazenará o valor da nova role quando selecionada no OptionMenu
        role_selected,

        # lista que contém os valores selecionaveis no OptionMenu
        *["Lider Técnico", "Product Owner", "Developer"],

        # comando que será executado ao selecionar uma opção
        command=(lambda _, md=member_data, rs = role_selected : update_role(_, md, get_role_id(rs.get())))
    ).grid(row=0, column=0)

    # cria o frame e button remover dentro do ações
    frame_remover = Frame(frame_actions)
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


from Utils import edit_team_back

def update_role(_, member_data, new_role):
    print(member_data['name'])
    print(new_role)
    edit_team_back.change_role(member_data['team_id'], member_data['email'], new_role)


def remove_member(member_data):
    print(member_data)
    edit_team_back.delete_user(member_data['email'])

