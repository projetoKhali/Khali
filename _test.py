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
        ni, ei = '' if i == 0 else ' Second', '' if i == 0 else 'r'

        from Models.Group import create_group

        # cadastra lider do grupo e cliente
        leader_id = register("Joao LG"+ni,    ei+"l@d.g",    i,    None, 1,    custom_password='123')
        client_id = register("Clara FC"+ni,   ei+"c@c.c",    i,    None, 2,    custom_password='123')

        # cadastra time utilizando o id do lider do grupo e cliente recem cadastrados
        create_group("Grupo dos Devs"+ni, leader_id, client_id)

        from Models.Team import create_team

        # cria times no primeiro grupo
        t = [
            create_team("first team"+str(i), i),
            create_team("second team"+str(i), i),
            create_team("third team"+ni, i)
        ]

        #           nome             email                  grupo  time    role        senha
        # LTs
        register("Moacir LTum"+ni,      ei+"lt1@o.com",            i,    t[0],    3,    custom_password='123')
        register("Maria LTdois"+ni,    ei+"lt2@o.com",            i,    t[1],    3,    custom_password='123')
        register("Ana LTtres"+ni,    ei+"lt3@o.com",            i,    t[2],    3,    custom_password='123')

        # POs
        register("Diego POum"+ni,      ei+"po-um@o.com",            i,    t[0],    4,    custom_password='123')
        register("Caio POdois"+ni,    ei+"p0-dois@o.com",            i,    t[1],    4,    custom_password='123')
        register("Maira POtres"+ni,    ei+"p0-três@o.com",            i,    t[2],    4,    custom_password='123')

        # devs
        register("Felipe Dev"+ni,   ei+"d@e.v",                i,    t[0],    5,    custom_password='123')
        register("Dora Dev"+ni,    ei+"dora@dev.com",      i,    t[0],    5,    custom_password='123')
        register("Lucas Dev"+ni, ei+"luc@dev.com",         i,    t[0],    5,    custom_password='123')
        register("Matheus Dev"+ni,       ei+"mat@dev.dev",         i,    t[1],    5,    custom_password='123')
        register("Lais Dev"+ni, ei+"dev-lais@dev.com",      i,    t[1],    5,    custom_password='123')
        register("Lara Dev"+ni,      ei+"dlara@dev.com",         i,    t[1],    5,    custom_password='123')
        register("Ignacio Dev"+ni,    ei+"na-dev@dev.com",          i,    t[2],    5,    custom_password='123')
        register("Marcia Dev"+ni,     ei+"marcia@dev.com",      i,    t[2],    5,    custom_password='123')
        register("Olga Dev"+ni,  ei+"ol@dev.com",   i,    t[2],    5,    custom_password='123')

        from Models.User import get_users_of_group
        from Models.Sprint import create_sprint
        from Models.Rating import create_rating
        from Models.id_criteria import criteria
        from random import randint

        # pega o id dos usuários do grupo i que foram cadrastados
        users = [x.id for x in get_users_of_group(i)]

        u = len(users)*len(users)*5*4
        j = 0

        sprint_dates = [
            [date(2022, 8,  29), date(2022, 9,  18)],
            [date(2022, 9,  19), date(2022, 10,  9)],
            [date(2022, 10, 17), date(2022, 11,  14)],
            [date(2022, 11,  15), date(2022, 11, 27)]
        ]

        # pra cada sprint
        for s in range((4 * i), 4 + (4 * i)):

            # cria a sprint
            create_sprint(i, sprint_dates[s % 4][0], sprint_dates[s % 4][1], 5)

            # pra cada usuário do grupo
            for f in users:

                # pra cada usuário do grupo novamente
                for t in users:

                    # pra cada critério de avaliação
                    for c in range(len(criteria)):

                        # cria uma nota aleatória entre 1 (inclusivo) e 6 (exclusivo)
                        n = randint(1, 6)

                        p = (j/(u+1))
                        j += 1

                        # printa a avaliação que será criada
                        print(f'grupo {i}: {int(p*100)}% |Criando avaliação teste: id({f}) avalia id({t}) na sprint {s} e critério {c} com a nota {n}')

                        # cria a avaliação
                        create_rating(f, t, s, c, n, 'feedback')


    # print do sucesso
    print("Geração de dados teste finalizada!")

