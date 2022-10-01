from CSV import CSVHandler as handler
import Settings




def add_user(email, team):
    # #busca, na base de dados 'users', os dados do estudante que tem aquele email
    # data_student = handler.find_data_csv(Settings.USERS_PATH, email)
    # #no diciona
    # data_student["team_id"] = str(team)
    # line =str(data_student["id"])
    #
    # for item in list(data_student.values())[1:]:
    #     line = line + ','+ item

    with open(Settings.USERS_PATH + '.csv', 'r') as file:
        # Lê as linhas do arquivo e salva na variavel 'lines'
        lines = file.readlines()

    for i, item in enumerate(lines):
        data_student = (handler.format_line_csv(Settings.PATH_FIELDS[Settings.USERS_PATH], item))
        if data_student['email'] == email:
            data_student['team_id'] = str(team)
            line = str(data_student['id'])
            for valor in list(data_student.values())[1:]:
                line += ',' + valor
            lines[i] = line
    for item in lines:
        print(item)
    handler.save_file_csv(Settings.USERS_PATH, Settings.PATH_FIELDS[Settings.USERS_PATH], lines )






    # index = lines.index(line)
    # lines[index] = line
    # print(line)
    # print(lines)

# add_user('p1@o.com', 1)



# def delete_user(email, team_id):
#     #vai até a base de dados e tira o time, deixando um espaço em branco.

