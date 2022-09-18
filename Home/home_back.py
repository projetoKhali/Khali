from CSV import CSVHandler as handler
import Settings

#função para acessar os users

#variável do tipo dicionario onde irei armazenar dados dos users que devem retornar na home de quem está logado


# def get_users(email, grupo, time):
def get_users(email):
    #retorna a linha que tem aquele email na forma de dicionário, isto é, os dados do aluno que fez o login.
    line_dict = handler.find_data_csv(Settings.USERS_PATH , email)

    #pego grupo e time da linha referente ao aluno que fez login
    grupo = line_dict["group"]
    time = line_dict["team"]

    #armazenar em data os dados dos usuários que pertencem ao grupo
    user_group = handler.find_data_list_csv(Settings.USERS_PATH, key = grupo)
    users_time = []

    for line in user_group:
        if line['team'] == time:
            users_time.append(line)
    return users_time



