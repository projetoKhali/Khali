from datetime import date
from Authentication import *


def create_test_data():
    from Settings import USERS_PATH, GROUPS_PATH, SPRINTS_PATH, TEAMS_PATH, RATINGS_PATH
    from CSV.CSVHandler import delete_csv

    delete_csv(USERS_PATH)
    delete_csv(GROUPS_PATH)
    delete_csv(SPRINTS_PATH)
    delete_csv(TEAMS_PATH)
    delete_csv(RATINGS_PATH)

    # cadastra o ADM
    register("A de Emmy",  "a@d.m",                None, None, 0,    custom_password='123')

    # pra cada grupo
    for i in range(2):

        # string shenanigans pra diferenciar nomes de times e usuários entre grupo 0 e 1
        ni, ei = '' if i == 0 else ' reverso', '' if i == 0 else 'r'

        from Models.Group import create_group

        # cadastra lider do grupo e cliente
        leader_id = register("L do Gê"+ni,    ei+"l@d.g",    i,    None, 1,    custom_password='123')
        client_id = register("clielano"+ni,   ei+"c@c.c",    i,    None, 2,    custom_password='123')

        # cadastra time utilizando o id do lider do grupo e cliente recem cadastrados
        create_group("Grupo do Develano"+ni, leader_id, client_id)

        from Models.Team import create_team

        # cria times no primeiro grupo
        to_user_id = [
            create_team("first_team_of_"+str(i), i),
            create_team("second_team_of_"+str(i), i),
            create_team("Time do Develano"+ni, i)
        ]

        #           nome             email                  grupo  time    role        senha
        # LTs
        register("lt um"+ni,      ei+"lt1@o.com",            i,    to_user_id[0],    3,    custom_password='123')
        register("lt dois"+ni,    ei+"lt2@o.com",            i,    to_user_id[1],    3,    custom_password='123')
        register("lt tres"+ni,    ei+"lt3@o.com",            i,    to_user_id[2],    3,    custom_password='123')

        # POs
        register("po um"+ni,      ei+"po1@o.com",            i,    to_user_id[0],    4,    custom_password='123')
        register("po dois"+ni,    ei+"p02@o.com",            i,    to_user_id[1],    4,    custom_password='123')
        register("po tres"+ni,    ei+"p03@o.com",            i,    to_user_id[2],    4,    custom_password='123')

        # devs
        register("develano"+ni,   ei+"d@e.v",                i,    to_user_id[0],    5,    custom_password='123')
        register("cleiton"+ni,    ei+"cleitin@dev.com",      i,    to_user_id[0],    5,    custom_password='123')
        register("washington"+ni, ei+"wash@dev.com",         i,    to_user_id[0],    5,    custom_password='123')
        register("deve"+ni,       ei+"deve@dev.dev",         i,    to_user_id[1],    5,    custom_password='123')
        register("developano"+ni, ei+"develop@dev.com",      i,    to_user_id[1],    5,    custom_password='123')
        register("dirce"+ni,      ei+"dirc@dev.com",         i,    to_user_id[1],    5,    custom_password='123')
        register("cumpadi"+ni,    ei+"cmp@dev.com",          i,    to_user_id[2],    5,    custom_password='123')
        register("devano"+ni,     ei+"dev-ano@dev.com",      i,    to_user_id[2],    5,    custom_password='123')
        register("fulanodev"+ni,  ei+"fulano-dev@dev.com",   i,    to_user_id[2],    5,    custom_password='123')

        from Models.User import get_users_of_team
        from Models.Team import get_teams_of_group
        from Models.Sprint import create_sprint
        from Models.Rating import create_rating
        from Models.id_criteria import criteria
        from random import randint

        # pega o id dos usuários do grupo i que foram cadrastados
        teams = [x.id for x in get_teams_of_group(i)]

        total_ratings = 5 * 4 * sum([len(get_users_of_team(t)) ** 2 for t in teams])
        current_rating_count = 0

        sprint_dates = [
            [date(2022, 8,  29), date(2022, 9,  18)],
            [date(2022, 9,  19), date(2022, 10,  9)],
            [date(2022, 10, 17), date(2022, 11,  14)],
            [date(2022, 11,  15), date(2022, 11, 27)]
        ]

        # pra cada sprint
        for sprint in range((4 * i), 4 + (4 * i)):

            # cria a sprint
            create_sprint(i, sprint_dates[sprint % 4][0], sprint_dates[sprint % 4][1], 5)

            for team_id in teams:
                users_of_team = [user.id for user in get_users_of_team(team_id)]

                # pra cada usuário do grupo
                for from_user_id in users_of_team:
                    if (randint(0, 100) < 60): continue

                    # pra cada usuário do grupo novamente
                    for to_user_id in users_of_team:
                        if (randint(0, 100) < 60): continue

                        # pra cada critério de avaliação
                        for criterio in range(len(criteria)):

                            # cria uma nota aleatória entre 1 (inclusivo) e 6 (exclusivo)
                            nota = randint(1, 5)

                            current_rating_count += 1
                            percent = (current_rating_count/(total_ratings))

                            # printa a avaliação que será criada
                            print(f'grupo {i}: {int(percent*100)}% |Criando avaliação teste: id({from_user_id}) avalia id({to_user_id}) na sprint {sprint} e critério {criterio} com a nota {nota}')

                            # cria a avaliação
                            create_rating(from_user_id, to_user_id, sprint, criterio, nota, 'feedback')


    # print do sucesso
    print("Geração de dados teste finalizada!")

