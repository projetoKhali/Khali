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
rows = ( )

save_file_csv("data/users", fields, rows)

with open("data/users.csv", 'r') as data:
    print(line_count_csv("data/users"))


create_group("first group")
create_group("second group")

print("groups linelen: " + str(line_count_csv(Settings.GROUPS_PATH)))
