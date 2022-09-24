from Users.Authentication import *

def initialize_test():

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

    # cadastra cliente teste
    register("clielano", "fulano.cliente@cliente.c", 0, None, 2)

    # cadastra developer teste
    register("developano", "developano-dev@dev.com", 0, 0, 5, custom_password='123')
    register("develano", "develano-dev@dev.com", 0, 0, 5, custom_password='123')
    register("devano", "devano-dev@dev.com", 0, 0, 5, custom_password='123')
    register("fulanodev", "fulano-dev@dev.com", 0, 0, 5, custom_password='123')


from KML import KMLTeste
KMLTeste.run()
exit()

initialize_test()

from Front import WindowManager

# register("Jhow Jhow", 'jhooliveira.lopes@gmail.com', 0, 0, 5)

WindowManager.initialize()

# teste - login automatico
# login(email='fulider_do@grupo.ldg', senha='123')
login(email='a@d.m', senha='123')

# from CSV.CSVHandler import load_file_csv
# from Settings import USERS_PATH
# if load_file_csv(USERS_PATH) is None:
#     # login(email='a@d.m', senha='123')
#     initialize_test()

WindowManager.update()

