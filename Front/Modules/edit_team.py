from Utils import edit_team_back
from tkinter import *

from Models.Team import Team, get_team, get_teams_of_group
from Models.Role import get_role_name, get_role_id
from Models.User import User, get_users_of_team, get_users_of_group
from Front.Core import *

# Informações do modulo
NAME = 'Editar'
REQUIRED_PERMISSIONS_REG  = [
    [3, 4, 5]
]
REQUIRED_PERMISSIONS_RATE = [None]
REQUIRED_PERMISSIONS_VIEW = [None]

module_frame = None

def run(frame_parent):

    global module_frame

    from Authentication import CURRENT_USER

    module_frame = Frame(frame_parent, padx=2, pady=2, bg=co0)
    module_frame.rowconfigure(1, weight = 1)
    module_frame.columnconfigure(0, weight = 1)
    module_frame.grid(row=0, column=0, sticky="news")

    # section 0
    frame_header = Frame(module_frame, padx=2, pady=2, bg=co3)
    frame_header.columnconfigure(0, weight=1)
    frame_header.grid(row=0, column=0, sticky='we')

    Label(frame_header, text="Editar Times", font='Calibri, 24 bold', bg=co3, fg=co0).grid(row=0, column=0)

    from Models.Group import get_groups_of_leader, get_group_of_name
    create_dropdown(
        criar_frame(frame_header, 0, 1, "ew", co3, px=12, py=0),0,0, 
        [i.name for i in get_groups_of_leader(CURRENT_USER.id)], 
        'get_group_id', lambda v: get_group_of_name(v).id, lambda _, __, ___: create_body()
    )

    create_body()


def create_body():

    # deleta o frame_body caso já exista
    children = module_frame.winfo_children()
    if children is not None and len(children) > 1 and children[1] is not None:
        children[1].destroy()

    # section 1
    frame_body = Frame(module_frame, padx=2, pady=2, bg=co0)
    frame_body.rowconfigure(0, weight = 12)
    frame_body.rowconfigure(1, weight = 1)
    frame_body.columnconfigure(0, weight = 1)
    frame_body.grid(row=1, column=0, sticky="news")

    frame_whitespace = Frame(frame_body, padx=0, pady=0, bg=co0)
    frame_whitespace.grid(row=1, column=0, sticky='news')

    from Front.Scrollbar import add_scrollbar
    frame_body = add_scrollbar(frame_body)
    frame_body.rowconfigure(1, weight = 1)
    frame_body.columnconfigure(0, weight = 1)

    # seleciona os times pertencentes ao grupo do usuario logado
    from Events import trigger
    teams_list = get_teams_of_group(trigger('get_group_id'))
    # print(f'times:{teams_list}')

    # pra cada time
    for team_index, team in enumerate(teams_list):
        frame_members_parent = create_team(frame_body, team, team_index)

        # seleciona os membros do time
        members_list = get_users_of_team(team.id)

        # para cada membro
        for member_index, member in enumerate(members_list):
            frame_member_actions = create_member(frame_members_parent, member, member_index)
            create_member_role(frame_member_actions, member, co0 if member_index % 2 == 1 else gr0)
            create_member_remove(frame_member_actions, member)


    # seleciona todos os usuarios com role 3, 4 ou 5 que não possuam time 
    no_team_users = [user for user in get_users_of_group(None) if int(user.role_id) in [3, 4, 5]]

    # retorna caso não existam usuários sem time
    # print(len(no_team_users))
    if len(no_team_users) > 0:

        frame_no_team_members_parent = create_team(frame_body, None, team_index+1)

        for user_id, no_team_user_data in enumerate(no_team_users):
            frame_member_actions = create_member(frame_no_team_members_parent, no_team_user_data, user_id)
            create_member_add(frame_member_actions, no_team_user_data, teams_list)
            create_member_unsubscribe(frame_member_actions, no_team_user_data)

    frame_bandaid = Frame(module_frame, pady=16, bg=co0)
    Label(frame_bandaid, text='', bg=co0).grid(row=0, column=0, sticky="s")
    frame_bandaid.grid(row=100, column=0, sticky="s")


def create_team(frame_teams_parent, team, team_index):

    # cria o frame do time
    frame_team = Frame(frame_teams_parent, bg=co4)
    frame_team.columnconfigure(0, weight = 1)
    frame_team.grid(row=team_index, column=0, sticky="ew")

    frame_team_header = criar_frame(frame_team, 0, 0, 'ew', co4, co4, 0, 0, 0)
    frame_team_header.columnconfigure(0, weight = 1)

    # coloca o nome do time
    label_team_name = Label(frame_team_header, text='Usuários sem time' if team is None else team.name, font='Calibri, 16', bg=co4)
    label_team_name.grid(row=0, column=0)
    if team is not None: label_team_name.bind("<Button-1>", lambda _, lbl=label_team_name, t=team, fg=frame_team_header: bind_edit_label(fg, lbl, t.name, 'Calibri, 16', 0, 0, lambda l, e, t=t: save_team_name(l, e, t)))

    if team is not None: criar_button(frame_team_header, 'Excluir Time', 'Calibri, 11', 0, 1, lambda t=team: [delete_team(t), create_body()], 'ew').config(takefocus = 0)


    frame_members_parent = Frame(frame_team)
    frame_members_parent.columnconfigure(0, weight = 1)
    frame_members_parent.grid(row=team_index+1, column=0, sticky="ew")

    return frame_members_parent


def save_team_name (label, entry, team):
    try: new_name = entry.get()
    except: return
    from Models.Team import edit_team
    edit_team(team.id, name=new_name)
    team.name=new_name
    label.config(text=new_name)

def delete_team(team):
    from tkinter import messagebox
    if messagebox.askquestion('Deletar time', f"Deseja deletar o time {team.name}?", icon='question') == 'yes':
        from Models.Team import delete_team
        delete_team(team.id)
        create_body()


def create_member(frame_members_parent, user:User, row):

    color = co0 if row % 2 == 1 else gr0

    # cria um frame para o membro dentro do frame_time
    frame_member = Frame(frame_members_parent, padx=2, pady=2, bg=color)
    frame_member.columnconfigure(0, weight = 1)
    frame_member.grid(row=row, column=0, sticky="we")

    # coloca o nome do membro
    frame_member_name = Frame(frame_members_parent, padx=2, pady=2, bg=color)
    # frame_member_name.columnconfigure(0, weight = 1)
    frame_member_name.grid(row=row, column=0, sticky="w")
    Label(frame_member_name, text=user.name, font='Calibri, 12', justify='left', padx=2, pady=2, bg=color).grid(row=0, column=0, sticky="ew")

    # cria um frame parent para as ações
    frame_actions = Frame(frame_member, bg=color)
    frame_actions.columnconfigure(0, weight = 1)
    frame_actions.grid(row=0, column=1, sticky="w")

    return frame_actions

def create_member_role(frame_member_actions, user:User, color):
    from Utils.edit_team_back import change_role

    # cria o frame e dropdown de role dentro do ações
    frame_dropdown = Frame(frame_member_actions, bg=color)
    frame_dropdown.grid(row=0, column=0)
    role_selected = StringVar()

    role_selected.set(get_role_name(user.role_id))
    role_dropdown = OptionMenu(
        frame_dropdown,

        # variavel que armazenará o valor da nova role quando selecionada no OptionMenu
        role_selected,

        # lista que contém os valores selecionaveis no OptionMenu
        *["Líder Técnico", "Product Owner", "Developer"],

        # comando que será executado ao selecionar uma opção
        command=(lambda _, u=user, rs = role_selected : change_role(u.team_id, u.email, get_role_id(rs.get())))
    )
    role_dropdown.grid(row=0, column=0, padx = 1)
    role_dropdown.config(width=16, height = 1, font = 'Calibri, 10')


def create_member_add(frame_member_actions, user:User, teams_list:list[Team]):
    from Utils.edit_team_back import add_user

    frame_adicionar = Frame(frame_member_actions)
    frame_adicionar.grid(row=0, column=1)
    team_selected = StringVar()
    team_selected.set('Adicionar ao Time')
    menu_adicionar = OptionMenu(
        frame_adicionar,

        # variavel que armazenará o valor da nova role quando selecionada no OptionMenu
        team_selected,

        # lista que contém os valores selecionaveis no OptionMenu
        *[team.name for team in teams_list],

        # comando que será executado ao selecionar uma opção
        command=(lambda _, u=user, ts = team_selected : add_user(u.email, get_team(ts.get()).id))
    )
    menu_adicionar.grid(row=0, column=0, padx=1)
    menu_adicionar.config(width=16, height = 1, font = 'Calibri, 10')

def create_member_remove(frame_member_actions, user:User):
    from Utils.edit_team_back import remove_user

    # cria o frame e button remover dentro do ações
    frame_remover = Frame(frame_member_actions)
    frame_remover.grid(row=0, column=1)
    Button(
        frame_remover,
        text='Remover',
        font='Calibri, 10',
        padx=1, width = 7, height=1,

        # comando que será executado ao clicar: 
        # chama a função remove_user com o user atual do loop como parametro
        command=lambda u=user:remove_user(u.email)
    ).grid(row=0, column=0)

def create_member_unsubscribe(frame_member_actions, user:User):
    from Utils.edit_team_back import unsubscribe_user

    # cria o frame e button remover dentro do ações
    frame_remover = Frame(frame_member_actions)
    frame_remover.grid(row=0, column=2)
    Button(
        frame_remover,
        text='Deletar',
        font='Calibri, 10',
        padx=1, width = 7, height=1,

        # comando que será executado ao clicar: 
        # chama a função remove_member com o user atual do loop como parametro
        command=lambda u=user:unsubscribe_user(u.email)
    ).grid(row=0, column=0)

