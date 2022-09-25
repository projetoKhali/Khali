from CSV import CSVHandler as handler
import Settings

# função para acessar os users
def get_users(email):

    # retorna a linha que tem aquele email na forma de dicionário, isto é, os dados do aluno que fez o login.
    line_dict = handler.find_data_csv(Settings.USERS_PATH, email)
    # retorna o grupo da pessoa que fez o login
    user_group = line_dict["group_id"]
    #retorna lista com todos os usuários que são do mesmo grupo que o logado
    user_group_members = handler.find_data_list_by_field_value_csv(Settings.USERS_PATH, 'group_id', user_group)

    #lista com os usuários que deverão ser avaliados pelo logado
    rate_users = []

    from Models import Role
    role = Role.get_role(line_dict["role_id"])
    for group_member in user_group_members:
        if int(group_member["role_id"]) in role.permissions_rate:
            rate_users.append(group_member)

    #se o papel do logado for Lider do Grupo
    if line_dict["role_id"] == 1:
        for group_member in user_group_members:
            #se o papel da pessoa for Líder Técnico
            if group_member["role_id"] == 3:
                rate_users.append(group_member)

    #se o papel do logado for Fake Client
    if line_dict["role_id"] == 2:
        for group_member in user_group_members:
            #se o papel da pessoa for PO
            if group_member["role_id"] == 4:
                rate_users.append(group_member)

    #se o papel do logado for estudante (lider técnico, po ou dev)
    if line_dict["role_id"] == 3 or line_dict["role_id"] == 4 or line_dict["role_id"] == 5:
        for group_member in user_group_members:
            #se a pessoa estiver no mesmo time que o logado
            if group_member["team_id"] == line_dict["team_id"]:
                rate_users.append(group_member)

    return rate_users














