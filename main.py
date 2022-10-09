from Users.Authentication import *
from Models.Groups import create_group
from Models.Teams import create_team

def initialize_test():
    from CSV.CSVHandler import delete_csv
    delete_csv(USERS_PATH)
    delete_csv(GROUPS_PATH)
    delete_csv(SPRINTS_PATH)
    delete_csv(TEAMS_PATH)
    delete_csv(RATINGS_PATH)

    # cria 2 grupos
    create_group("Grupo do Develano")
    create_group("first group")
    create_group("second group")

    # cria 2 times no primeiro grupo
    create_team("Time do Develano", 0)
    create_team("first_team_of0", 0)
    create_team("second_team_of0", 0)

    # cria 2 times no segundo grupo
    create_team("first_team_of1", 1)
    create_team("second_team_of1", 1)

    # cadastra o develano
    register("A de Emmy", "a@d.m", None, None, 0, custom_password='123')

    # cadastra lider do grupo teste
    register("L do Gê", "l@d.g", 0, None, 1, custom_password='123')

    # # cadastra cliente teste
    # register("clielano", "c@c.c", 0, None, 2, custom_password='123')

    register("lt um", "lt1@o.com",   0, 0, 3, custom_password='123')
    register("lt dois", "lt2@o.com", 0, 1, 3, custom_password='123')
    register("lt tres", "lt3@o.com", 0, 2, 3, custom_password='123')

    register("po um", "po1@o.com",   0, 0, 4, custom_password='123')
    register("po dois", "p02@o.com", 0, 1, 4, custom_password='123')
    register("po tres", "p03@o.com", 0, 2, 4, custom_password='123')

    # # cadastra developer teste
    register("deve", "d@e.v", 0, 0, 5, custom_password='123')
    # register("developano", "develop@dev.com", 0, 0, 5, custom_password='123')
    # register("develano", "develano-dev@dev.com", 0, 0, 5, custom_password='123')
    # register("devano", "dev-ano@dev.com", 0, 0, 5, custom_password='123')
    # register("fulanodev", "fulano-dev@dev.com", 0, 0, 5, custom_password='123')
    # register("fuldev", "ful@dev.com", 0, 1, 5, custom_password='123')

    register("semtime", "st@s.t", 0, None, 5, custom_password='123')
    register("timesem", "ts@t.s", 0, None, 5, custom_password='123')
    register("emitmes", "s@e.m",  0, None, 5, custom_password='123')


# Inicializa os bancos de dados populado com informações teste caso não exista um arquivo users.csv
# import os
# if not os.path.exists(USERS_PATH + '.csv'):
initialize_test()

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

WindowManager.update()
