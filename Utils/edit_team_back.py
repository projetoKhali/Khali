from operator import index
from CSV import CSVHandler as handler
import Settings
from array import *

# mudo o time de um estudante já cadastrado para um novo time
def add_user(email, team):

    #abre e lê arquivo csv
    with open(Settings.USERS_PATH + '.csv', 'r') as file:
        # Lê as linhas do arquivo e salva na variavel 'lines'. Cada linha é uma única string
        lines = file.readlines()

    matriz = []

    for i, item in enumerate(lines[1:]):
        #retorna a linha no formato de string em um dicionário e armazena em data_student
        data_student = (handler.format_line_csv(Settings.PATH_FIELDS[Settings.USERS_PATH], item))
        #se a linha for a do aluno que quero adicionar
        if data_student['email'] == email:
            data_student['team_id'] = str(team)
            #o estudante adicionado entra como dev
            data_student['role_id'] = str(5)

        #transformar o dicionário em uma lista line.
        line = []

        #pego apenas os valores do dicionários, sem os fields, e coloco na lista line
        for valor in list(data_student.values()):
            line.append(str(valor))
            # print(f'line: {line}')

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
        # se a linha for a do aluno que quero deletar, mudarei seu time para vazio
        if data_student['email'] == email:
            data_student['team_id'] = ''

        # transformar o dicionário em uma lista line.
        line = []

        # pego apenas os valores do dicionários, sem os fields, e coloco na lista line
        for valor in list(data_student.values()):
            line.append(str(valor))
            # print(f'line: {line}')

        matriz.append(line)

    handler.save_file_csv(Settings.USERS_PATH, Settings.PATH_FIELDS[Settings.USERS_PATH], matriz)

# team se refere ao id do time que estou editando, email é o email do aluno que quero mudar de papel,
# e role é o id do papel que quero atribuir a esse aluno
def change_role(team, email, role):
    # abre e lê arquivo csv
    with open(Settings.USERS_PATH + '.csv', 'r') as file:
        # Lê as linhas do arquivo e salva na variavel 'lines'. Cada linha é uma única string
        lines = file.readlines()

    matriz = []


    for i, item in enumerate(lines[1:]):
        # retorna a linha em um dicionário e armazena em data_student
        data_student = (handler.format_line_csv(Settings.PATH_FIELDS[Settings.USERS_PATH], item))
        # se o papel que quero atribuir ao aluno for o de lider técnico, preciso trocar o papel do lt anterior para dev.
        if role == 3:
            # procuro na users quem atende dois requisitos: estão no mesmo time que estou editando e tem o papel de lt.
            # Atribuo a essa pessoa o papel de dev

            if data_student['team_id'] == str(team) and data_student['role_id'] == str(3):
                data_student['role_id'] = 5
        # se o papel que quero atribuir ao aluno for o de po, preciso trocar o papel do po anterior para dev.
        if role == 4:
            # procuro na users quem atende dois requisitos: estão no mesmo time que estou editando e tem o papel de po.
            # Atribuo a essa pessoa o papel de dev.
            if data_student['team_id'] == str(team) and data_student['role_id'] == str(4):
                data_student['role_id'] = 5

        # se o aluno for aquele cujo papel quero editar
        if data_student['email'] == email:
           data_student['role_id'] = str(role)


        # transformar o dicionário em uma lista line.
        line = []

        # pego apenas os valores do dicionários, sem os fields, e coloco na lista line
        for valor in list(data_student.values()):
            line.append(str(valor))
            # print(f'line: {line}')

        matriz.append(line)

    handler.save_file_csv(Settings.USERS_PATH, Settings.PATH_FIELDS[Settings.USERS_PATH], matriz)

def unsubscribe_student(email):
     # abre e lê arquivo csv
    with open(Settings.USERS_PATH + '.csv', 'r') as file:
        # Lê as linhas do arquivo e salva na variavel 'lines'. Cada linha é uma única string
        lines = file.readlines()

    matriz = []

    for i, item in enumerate(lines[1:]):
        # retorna a linha em um dicionário e armazena em data_student
        data_student = (handler.format_line_csv(Settings.PATH_FIELDS[Settings.USERS_PATH], item))
        if data_student['email'] == email:
            index_to_delete = i + 1
    
    data_to_delete = lines[index_to_delete]
    lines.remove(data_to_delete)
    
    for i,item in enumerate(lines[1:]):
        data_student = (handler.format_line_csv(Settings.PATH_FIELDS[Settings.USERS_PATH], item))
        line = []
        for valor in list(data_student.values()):
            line.append(str(valor))
            # print(f'line: {line}')

        matriz.append(line)

    handler.save_file_csv(Settings.USERS_PATH, Settings.PATH_FIELDS[Settings.USERS_PATH], matriz)



            

    
    
