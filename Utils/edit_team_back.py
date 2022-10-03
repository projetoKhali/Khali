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
        #se o email do estudante for aquele digitado, seu time será alterado para o digitado
        if data_student['email'] == email:
            data_student['team_id'] = str(team)

        #transformar o dicionário em uma lista line.
        line = []

        #pego apenas os valores do dicionários, sem os fields, e coloco na lista line
        for valor in list(data_student.values()):
            line.append(str(valor))
            print(line)

        matriz.append(line)

    handler.save_file_csv(Settings.USERS_PATH, Settings.PATH_FIELDS[Settings.USERS_PATH], matriz)

def delete_user(email):
    # abre e lê arquivo csv
    with open(Settings.USERS_PATH + '.csv', 'r') as file:
        # Lê as linhas do arquivo e salva na variavel 'lines'. Cada linha é uma única string
        lines = file.readlines()

    matriz = []

    for i, item in enumerate(lines[1:]):
        # retorna a linha no formato de string em um dicionário e armazena em data_student
        data_student = (handler.format_line_csv(Settings.PATH_FIELDS[Settings.USERS_PATH], item))
        # se o email do estudante for aquele digitado, seu time será alterado para o digitado
        if data_student['email'] == email:
            data_student['team_id'] = ''

        # transformar o dicionário em uma lista line.
        line = []

        # pego apenas os valores do dicionários, sem os fields, e coloco na lista line
        for valor in list(data_student.values()):
            line.append(str(valor))
            print(line)

        matriz.append(line)

    handler.save_file_csv(Settings.USERS_PATH, Settings.PATH_FIELDS[Settings.USERS_PATH], matriz)




