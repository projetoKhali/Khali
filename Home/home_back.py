from CSV import CSVHandler as handler
import Settings

#função para acessar os users

#variável do tipo dicionario onde irei armazenar dados dos users que devem retornar na home de quem está logado


# def get_users(email, grupo, time):
def get_users(email):
    #retorna a linha que tem aquele email na forma de dicionário, isto é, os dados do aluno que fez o login.
    line_dict = handler.find_data_csv(Settings.USERS_PATH, email)

    print (line_dict)

    #pego grupo e time da linha referente ao aluno que fez login
    grupo_id = line_dict["group_id"]
    time_id = line_dict["team_id"]

    #armazenar em data os dados dos usuários que pertencem ao grupo
    user_group_members = handler.find_data_list_by_field_value_csv(Settings.USERS_PATH, 'group_id', grupo_id)
    users_time_members = []

    for group_member in user_group_members:
        print(f'group_member: {group_member}')
        if group_member['team_id'] == str(time_id):
            users_time_members.append(group_member)
    return users_time_members



