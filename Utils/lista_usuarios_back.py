from CSV import CSVHandler as handler
import Settings

# função para acessar os users
def get_users(email):

    # retorna a linha que tem aquele email na forma de dicionário, isto é, os dados do aluno que fez o login.
    user = handler.find_data_csv(Settings.USERS_PATH, email)

    from Models import Role
    #pego o nome e funções da pessoa que logou
    role = Role.get_role(user["role_id"])



    if user["role_id"] in [3, 4, 5]:
        # retorna lista com todos os usuários que são do mesmo time que o logado
        return handler.find_data_list_by_field_value_csv(Settings.USERS_PATH, 'team_id', user["team_id"])

    rate_users = []

    for group_member in handler.find_data_list_by_field_value_csv(Settings.USERS_PATH, 'group_id', user["group_id"]):
        if (int(group_member["role_id"]) in role.ratings) and (group_member["team_id"] != ''):
            rate_users.append(group_member)
    return rate_users
























