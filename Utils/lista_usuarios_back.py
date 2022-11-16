from CSV import CSVHandler as handler
import Settings


# função para acessar os users
def get_users(email):

    # retorna a linha que tem aquele email na forma de dicionário, isto é, os dados do aluno que fez o login.
    user = handler.find_data_csv(Settings.USERS_PATH, email)


    if user == None:
        # print ('nenhum usuário encontrado, lista_usuarios_back.get_users.user')
        return

    from Models import Role
    #pego o nome e funções da pessoa que logou
    role = Role.get_role(int(user["role_id"]))

    #lista com as linhas da tabela ratings que correspondem a avaliações do usuário logado
    ratings = handler.find_data_list_by_field_value_csv(Settings.RATINGS_PATH, 'from_user_id', user['id'])
    grade_submitted = []
    grade_to_submit = []



    if int(user["role_id"]) in [3, 4, 5]:
        # retorna lista com todos os usuários que são do mesmo time que o logado
        rate_users = handler.find_data_list_by_field_value_csv(Settings.USERS_PATH, 'team_id', user["team_id"])
        for member in rate_users:
            auxiliar = 0
            if ratings is not None:
                for rating in ratings:
                    if member["id"] == rating["to_user_id"] and rating["value"] != '':
                        auxiliar = 1
                        break
            if auxiliar == 1:
                grade_submitted.append(member)
            else:
                grade_to_submit.append(member)



        # print('a avaliar')
        # for item in (grade_to_submit):
        #     print(item["email"])
        # print('avaliados')
        # for item in (grade_submitted):
        #     print(item["email"])

        return (grade_submitted, grade_to_submit)




    rate_users = handler.find_data_list_by_field_value_csv(Settings.USERS_PATH, 'group_id', user["group_id"])
    for group_member in rate_users:
        # print(group_member)
        # print(type(role.permissions_rate[0]))


        if (int(group_member["role_id"]) not in role.permissions_rate) or (group_member["team_id"] == ''):
            # print('pular iteração')
            continue

        auxiliar = 0

        if ratings is not None:
            for rating in ratings:
                if group_member["id"] == rating["to_user_id"] and rating["value"] != '':
                    auxiliar = 1
                    # print('incluiu na sumbmitted')
                    break
        if auxiliar == 1:
            grade_submitted.append(group_member)
        else:
            # print('incluiu na to_submit')
            grade_to_submit.append(group_member)

        # # rate_users.append(group_member)
        # for rating in ratings:
        #     id_rated = rating['to_user_id']
        #     # for member in rate_users:
        #     if group_member['id'] == id_rated and rating['value'] != '':
        #         grade_submitted.append(group_member)
        #     else:
        #         grade_to_submit.append(group_member)

    # print(grade_submitted)
    # print(grade_to_submit)
    return [grade_to_submit, grade_submitted]


# print(get_users('lt1@o.com'))





















