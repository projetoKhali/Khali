from CSV.CSVHandler import *
import Settings
from Users.Authentication import *
from Users.Roles.Role import *


# Inicializa todas as databases
def initialize_databases ():
    initialize_csv(Settings.USERS_PATH)
    initialize_csv(Settings.GROUPS_PATH)
    initialize_csv(Settings.TEAMS_PATH)

# !TODO!: Limpa as databases toda vez que o programa for executado
# !TODO!: 'Inicialize_databases' deverá ser executado APENAS na primeira execução do programa
initialize_databases()

create_group("group")
create_team("team", 0)

register("teste", "teste@teste.teste", 0, 0, 0)

# area de testes:

# # printa a quantidade de linhas na database de usuarios
# print(line_count_csv(USERS_PATH))

# cria 2 grupos
create_group("first group")
create_group("second group")

# cria 2 times no primeiro grupo
create_team("first_team_of0", 0)
create_team("second_team_of0", 0)

# cria 2 times no segundo grupo
create_team("first_team_of1", 1)
create_team("second_team_of1", 1)

# cadastra ADM teste
register("fulanoADM", "fulano.adm@adm.adm", 0, 0, 0)

# cadastra lider do grupo teste
register("fulanoLdG", "fulider_do@grupo.ldg", 0, 0, 1)

# cadastra cliente teste
register("clielano", "fulano.cliente@cliente.c", 0, 0, 2)

# cadastra developer teste
register("develano", "fulano-dev@dev.com", 0, 0, 5)

