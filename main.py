
# 
from CSV.CSVHandler import *
from Users import UserSettings as settings
from Users.Roles.Role import *

fields = [ 1, 2, 3 ]
rows = ( ( 'a', 'b', 'c'), ('a2', 'b2', 'c2' ) )

save_file("data/users", fields, rows)

with open("data/users.csv", 'r') as data:
    print(line_len("data/users"))

print ("find_data: " + str(find_data(settings.USERS_PATH, str("a"))))