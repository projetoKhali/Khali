from datetime import date
from CSV.CSVHandler import *
import Settings
from Users.Authentication import *
from Users.Roles.Role import *

from Front import cadastroadm, login_front

# Inicializa todas as databases
def initialize_databases ():
    initialize_csv(Settings.USERS_PATH)
    initialize_csv(Settings.GROUPS_PATH)
    initialize_csv(Settings.TEAMS_PATH)

# !TODO!: Limpa as databases toda vez que o programa for executado
# !TODO!: 'Inicialize_databases' deverá ser executado APENAS na primeira execução do programa

initialize_databases()

# cria grupo e time do develano
create_group("Grupo do Develano")
create_team("Time do Develano", 0)

# cadastra o develano
register("develano", "dev.lano@dev.lano", 0, 0, 0)


# window = cadastroadm.run()
# window = login_front.run()

# window.mainloop()  # Método que executa eventos como cliques de botão e mantém a janela aberta

# from Sprints.Sprints import create_sprint
# create_sprint(0, date.)

# faz login com o develano
# login("develano", input("texto"))

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

from Front.Home import lista_usuarios

lista_usuarios.run("fulider_do@grupo.ldg")

