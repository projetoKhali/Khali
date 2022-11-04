from datetime import date, datetime
from Authentication import *
from tkinter import *


def initialize_test():

    from CSV.CSVHandler import delete_csv

    delete_csv(USERS_PATH)
    delete_csv(GROUPS_PATH)
    delete_csv(SPRINTS_PATH)
    delete_csv(TEAMS_PATH)
    delete_csv(RATINGS_PATH)

    from Models.Group import create_group

    # cria 2 grupos
    create_group("Grupo do Develano")
    create_group("first group")
    create_group("second group")

    from Models.Team import create_team

    # cria 2 times no primeiro grupo
    create_team("first_team_of_0", 0)
    create_team("second_team_of_0", 0)
    create_team("Time do Develano", 0)

    # cria 2 times no segundo grupo
    create_team("first_team_of_1", 1)
    create_team("second_team_of_1", 1)

    #           nome          email                     grupo time  role         senha

    # cadastra o develano
    register("A de Emmy",  "a@d.m",                None, None, 0,    custom_password='123')

    # cadastra lider do grupo teste
    register("L do Gê",    "l@d.g",                0,    None, 1,    custom_password='123')

    # cadastra cliente teste
    register("clielano",   "c@c.c",                0,    None, 2,    custom_password='123')
    register("lt um",      "lt1@o.com",            0,    0,    3,    custom_password='123')
    # register("lt dois",    "lt2@o.com",            0,    1,    3,    custom_password='123')
    # register("lt tres",    "lt3@o.com",            0,    2,    3,    custom_password='123')
    register("po um",      "po1@o.com",            0,    0,    4,    custom_password='123')
    # register("po dois",    "p02@o.com",            0,    1,    4,    custom_password='123')
    # register("po tres",    "p03@o.com",            0,    2,    4,    custom_password='123')

    register("deve",       "d@e.v",                0,    0,    5,    custom_password='123')
    register("developano", "develop@dev.com",      0,    0,    5,    custom_password='123')
    register("develano",   "develano-dev@dev.com", 0,    0,    5,    custom_password='123')
    register("devano",     "dev-ano@dev.com",      0,    0,    5,    custom_password='123')
    register("fulanodev",  "fulano-dev@dev.com",   0,    0,    5,    custom_password='123')
    register("dirce",      "dirc@dev.com",         0,    0,    5,    custom_password='123')
    register("cleiton",    "cleitin@dev.com",      0,    0,    5,    custom_password='123')
    register("cumpadi",    "cmp@dev.com",          0,    0,    5,    custom_password='123')
    register("washington", "wash@dev.com",         0,    0,    5,    custom_password='123')

    from Models.Sprint import create_sprint

    # create_sprint(0, date(2022, 10,  4), date(2022, 10, 11), 5)
    # create_sprint(0, date(2022, 10, 12), date(2022, 10, 19), 5)
    # create_sprint(0, date(2022, 10, 20), date(2022, 10, 27), 5)


    from Models.Rating import create_rating
    from random import randint, choice
    from Models.User import get_users_of_team
    from Models.id_criteria import criteria

    users = [x.id for x in get_users_of_team(0)]

    for s in range(4):
        create_sprint(0, date(2022, 10, 20), date(2022, 10, 27), 5)
        for f in users:
            for t in users:
                for c in range(len(criteria)):
                    create_rating(f, t, s, c, randint(0, 5), 'feedback')


# Inicializa os bancos de dados populado com informações teste caso não exista um arquivo users.csv
# import os
# if not os.path.exists(USERS_PATH + '.csv'):
# initialize_test()


from Models.Sprint import current_sprint
# print(current_sprint(0))

from random import choice
from Models.User import get_users_of_group
from graficos import Dashboards
from Front.Modules import dashboards
from tkinter import *

window = Tk()
dashboards.run(window)
window.mainloop()

users = [x.id for x in get_users_of_group(0)]

# Dashboards.user_media_sprints(choice(users))
# Dashboards.team_media_sprints(0)
# Dashboards.user_media_x_team(choice(users))
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
login(email='l@d.g', senha='123')
# login(email='c@c.c', senha='123')
# login(email='l@d.g', senha='123')
# login(email='lt1@o.com', senha='123')

WindowManager.update()
