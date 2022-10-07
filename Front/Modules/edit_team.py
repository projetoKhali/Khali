from Utils import edit_team_back
from tkinter import *

# cores
co0 = "#FAE8E8"  # rosa
co1 = "#D9D9D9"  # cinza
co2 = "#1A1D1A"  # preta

# Informações do modulo
NAME = 'Editar'
REQUIRED_PERMISSIONS_REG  = [
    [3, 4, 5]
]
REQUIRED_PERMISSIONS_RATE = [None]
REQUIRED_PERMISSIONS_VIEW = [None]

def run(frame_parent):

    # cria o frame do módulo
    module_frame = Frame(frame_parent, padx=2, pady=2, bg='magenta')
    # module_frame.rowconfigure(0, minsize = 0, weight = 1)
    module_frame.columnconfigure(0, minsize = 0, weight = 1)
    module_frame.grid(row=0, column=0, sticky="news")

    # section 0
    frame_title = Frame(module_frame, padx=2, pady=2, bg='blue')
    frame_title.grid(row=0, column=0, sticky='we')

    Label(frame_title, text="Editar", font='Calibri, 20').grid(row=0, column=0)

    # section 1
    frame_teams = Frame(module_frame, padx=2, pady=2, bg='cyan')
    frame_teams.rowconfigure(1, minsize = 0, weight = 1)
    frame_teams.columnconfigure(0, minsize = 0, weight = 1)
    frame_teams.grid(row=1, column=0, sticky="ew")

    from CSV.CSVHandler import find_data_list_by_field_value_csv
    from Users.Authentication import CURRENT_USER
    from Settings import USERS_PATH, TEAMS_PATH
    print(f'group_id:{CURRENT_USER.group_id}')

    # seleciona os times pertencentes ao grupo do usuario logado
    times = find_data_list_by_field_value_csv(TEAMS_PATH, 'group', CURRENT_USER.group_id)
    print(f'times:{times}')

    from Models.Teams import get_team_name

    # pra cada time
    for i, time_data in enumerate(times):
        print(f'i: [{i}]: time "{time_data}"')

        # cria o frame do time
        frame_team = Frame(frame_teams, padx=2, pady=2, bg="yellow")
        frame_team.columnconfigure(0, minsize = 0, weight = 1)
        frame_team.grid(row=i, column=0, sticky="ew")

        # coloca o nome do time
        Label(frame_team, text=get_team_name(int(time_data['id'])), font='Calibri, 16').grid(row=0, column=0)

        # seleciona os membros do time
        members = find_data_list_by_field_value_csv(USERS_PATH, 'team_id', i)

        # para cada membro
        for j, member_data in enumerate(members):

            print(f'member: {member_data}')

            # cria um frame para o membro dentro do frame_time
            frame_member = Frame(frame_team, padx=2, pady=2)
            frame_member.columnconfigure(0, minsize = 0, weight = 1)
            frame_member.grid(row=j+1, column=0, sticky="we")

            # coloca o nome do membro
            frame_member_name = Frame(frame_team, padx=2, pady=2)
            # frame_member_name.columnconfigure(0, minsize = 0, weight = 1)
            frame_member_name.grid(row=j+1, column=0, sticky="w")
            Label(frame_member_name, text=member_data['name'], font='Calibri, 12', justify='left', bg='green', padx=2, pady=2).grid(row=0, column=0, sticky="ew")

            # cria um frame parent para as ações
            frame_actions = Frame(frame_member)
            frame_actions.columnconfigure(0, minsize = 0, weight = 1)
            frame_actions.grid(row=0, column=1, sticky="w")

            # cria o frame e dropdown de role dentro do ações
            frame_dropdown = Frame(frame_actions)
            frame_dropdown.grid(row=0, column=0)
            Label(frame_dropdown, text='dropdown', font='Calibri, 12', padx=8, pady=2, bg='blue').grid(row=0, column=0)

            # cria o frame e button remover dentro do ações
            frame_remover = Frame(frame_actions)
            frame_remover.grid(row=0, column=1)
            Label(frame_remover, text='remover', font='Calibri, 12', padx=8, pady=2, bg='red').grid(row=0, column=0)





