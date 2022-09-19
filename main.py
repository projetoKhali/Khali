from datetime import date
from CSV.CSVHandler import *
import Settings
from Users.Authentication import *
from Users.Roles.Role import *


# Inicializa todas as databases
def initialize_databases ():
    initialize_csv(Settings.USERS_PATH)
    initialize_csv(Settings.GROUPS_PATH)
    initialize_csv(Settings.SPRINTS_PATH)
    initialize_csv(Settings.TEAMS_PATH)

# !TODO!: Limpa as databases toda vez que o programa for executado
# !TODO!: 'Inicialize_databases' deverá ser executado APENAS na primeira execução do programa

initialize_databases()

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
register("A de Emmy", "adm@a.dm", None, None, 0, custom_password='123')

# cadastra lider do grupo teste
register("fulanoLdG", "fulider_do@grupo.ldg", 0, None, 1, custom_password='123')

# cadastra cliente teste
register("clielano", "fulano.cliente@cliente.c", 0, None, 2)

# cadastra developer teste
register("developano", "developano-dev@dev.com", 0, 0, 5, custom_password='123')
register("develano", "develano-dev@dev.com", 0, 0, 5, custom_password='123')
register("devano", "devano-dev@dev.com", 0, 0, 5, custom_password='123')
register("fulanodev", "fulano-dev@dev.com", 0, 0, 5, custom_password='123')

from Front import WindowManager

WindowManager.initialize()

# teste
login(email='fulider_do@grupo.ldg', senha='123')

WindowManager.update()

