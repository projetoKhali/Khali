from datetime import date
from Authentication import *
from Front.Modules import ModulesManager

def initialize_test():

    from CSV.CSVHandler import delete_csv

    delete_csv(USERS_PATH)
    delete_csv(GROUPS_PATH)
    delete_csv(SPRINTS_PATH)
    delete_csv(TEAMS_PATH)
    delete_csv(RATINGS_PATH)

    # cadastra o ADM
    register("A de Emmy",  "a@d.m",                None, None, 0,    custom_password='123')

    for i in range(2):

        ni, ei = '' if i == 0 else ' reverso', '' if i == 0 else 'r'

        from Models.Group import create_group

        # cadastra lider do grupo e cliente
        leader_id = register("L do Gê"+ni,    ei+"l@d.g",    i,    None, 1,    custom_password='123')
        client_id = register("clielano"+ni,   ei+"c@c.c",    i,    None, 2,    custom_password='123')
        create_group("Grupo do Develano"+ni, leader_id, client_id)

        # cadastra lider do grupo e cliente
        # register("Lider dodois",    "l@d.h",           0,    None, 1,    custom_password='123')
        # register("cliedois",   "c@c.d",                0,    None, 2,    custom_password='123')
        # create_group("Grupo Dois", 3, 4)

        from Models.Team import create_team

        # cria times no primeiro grupo
        t = [
            create_team("first_team_of_"+str(i), i),
            create_team("second_team_of_"+str(i), i),
            create_team("Time do Develano"+ni, i)
        ]

        #           nome             email                  grupo  time role         senha
        register("lt um"+ni,      ei+"lt1@o.com",            i,    t[0],    3,    custom_password='123')
        register("lt dois"+ni,    ei+"lt2@o.com",            i,    t[1],    3,    custom_password='123')
        register("lt tres"+ni,    ei+"lt3@o.com",            i,    t[2],    3,    custom_password='123')
        register("po um"+ni,      ei+"po1@o.com",            i,    t[0],    4,    custom_password='123')
        register("po dois"+ni,    ei+"p02@o.com",            i,    t[1],    4,    custom_password='123')
        register("po tres"+ni,    ei+"p03@o.com",            i,    t[2],    4,    custom_password='123')

        register("develano"+ni,   ei+"develano-dev@dev.com", i,    t[0],    5,    custom_password='123')
        register("cleiton"+ni,    ei+"cleitin@dev.com",      i,    t[0],    5,    custom_password='123')
        register("washington"+ni, ei+"wash@dev.com",         i,    t[0],    5,    custom_password='123')
        register("deve"+ni,       ei+"d@e.v",                i,    t[1],    5,    custom_password='123')
        register("developano"+ni, ei+"develop@dev.com",      i,    t[1],    5,    custom_password='123')
        register("dirce"+ni,      ei+"dirc@dev.com",         i,    t[1],    5,    custom_password='123')
        register("cumpadi"+ni,    ei+"cmp@dev.com",          i,    t[2],    5,    custom_password='123')
        register("devano"+ni,     ei+"dev-ano@dev.com",      i,    t[2],    5,    custom_password='123')
        register("fulanodev"+ni,  ei+"fulano-dev@dev.com",   i,    t[2],    5,    custom_password='123')

        from Models.User import get_users_of_group
        from Models.Sprint import create_sprint
        from Models.Rating import create_rating
        from Models.id_criteria import criteria
        from random import randint

        users = [x.id for x in get_users_of_group(i)]

        for s in range((4 * i), 4 + (4 * i)):
            create_sprint(i, date(2022, 10, 20), date(2022, 11, 27), 5)
            for f in users:
                for t in users:
                    for c in range(len(criteria)):
                        n = randint(0, 5)
                        print(f'Criando avaliação teste: id({f}) avalia id({t}) na sprint {s} e critério {c} com a nota {n}')
                        create_rating(f, t, s, c, n, 'feedback')


# Inicializa os bancos de dados populado com informações teste caso não exista um arquivo users.csv
# import os
# if not os.path.exists(USERS_PATH + '.csv'):


# initialize_test()


# from Models.Sprint import current_sprint
# print(f'current sprint(0): {current_sprint(0)}')

from random import choice
from Models.User import get_users_of_group
from graficos import Dashboards

users = [x.id for x in get_users_of_group(0)]

# Dashboards.user_media_sprints(choice(users))
Dashboards.team_media_sprints(0)                    # !!!!!!!!
# Dashboards.user_media_x_team(choice(users))
# Dashboards.role_media(3, 0)
# Dashboards.users_media_team(0)
# Dashboards.group_media_sprints(1)
# Dashboards.teams_media(0)
exit()

# from Utils.edit_team_back import *

# print(add_user("ful@dev.com", 0))
# exit()

# print(delete_user('ful@dev.com'))
# exit()

# print(change_role(1, 'lt2@o.com', 5))
# exit()


from Front import WindowManager

# register("Jhow Jhow", 'jhooliveira.lopes@gmail.com', 0, 0, 5)

WindowManager.initialize()

# teste - login automatico
# login(email='a@d.m', senha='123')
# login(email='l@d.g', senha='123')
# login(email='c@c.c', senha='123')
# login(email='l@d.g', senha='123')
login(email='lt1@o.com', senha='123')

WindowManager.update()
