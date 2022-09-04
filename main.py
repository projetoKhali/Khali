from CSV.CSVHandler import *
import Settings
from Users.Authentication import *
from Users.Roles.Role import *

# Remove todas as databases
def initialize_databases ():
    delete_csv(Settings.USERS_PATH)
    delete_csv(Settings.GROUPS_PATH)
    delete_csv(Settings.TEAMS_PATH)

# !TODO!: Limpa as databases toda vez que o programa for executado
# !TODO!:  
# !TODO!: remover essa linha antes da entrega 
# !TODO!:  
initialize_databases()


# area de testes:

fields = [ 1, 2, 3 ]
rows = ( ( 'a', 'b', 'c'), ('a2', 'b2', 'c2' ) )

save_file_csv("data/users", fields, rows)

with open("data/users.csv", 'r') as data:
    print(line_len_csv("data/users"))

print ("find_data: " + str(find_data_csv(Settings.USERS_PATH, str("a"))))


create_group("new group name")
create_team("1")
create_team("2")
create_team("3")
create_team("4")
create_team("5")
