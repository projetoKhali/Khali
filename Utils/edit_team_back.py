from CSV import CSVHandler as handler
import Settings
from array import *




def add_user(email, team):

    #abre e lê arquivo csv
    with open(Settings.USERS_PATH + '.csv', 'r') as file:
        # Lê as linhas do arquivo e salva na variavel 'lines'. Cada linha é uma única string
        lines = file.readlines()

    matriz = []

    for i, item in enumerate(lines[1:]):
        #retorna a linha no formato de string em um dicionário e armazena em data_student
        data_student = (handler.format_line_csv(Settings.PATH_FIELDS[Settings.USERS_PATH], item))
        if data_student['email'] == email:
            data_student['team_id'] = str(team)

        #transformar o dicionário em uma lista line. O primeiro item dessa lista é o id
        line = []

        for valor in list(data_student.values()):
            line.append(str(valor))
            print(line)


            # #armazeno, no item de index i do arquivo csv, a line
            # lines[i] = line
        matriz.append(line)
        # for i in range ()

    # for item in lines:
    #     dicionario = handler.format_line_csv(Settings.PATH_FIELDS[Settings.USERS_PATH], item)
    #     print(item)
    handler.save_file_csv(Settings.USERS_PATH, Settings.PATH_FIELDS[Settings.USERS_PATH], matriz)






    # index = lines.index(line)
    # lines[index] = line
    # print(line)
    # print(lines)

# add_user('p1@o.com', 1)



# def delete_user(email, team_id):
#     #vai até a base de dados e tira o time, deixando um espaço em branco.

