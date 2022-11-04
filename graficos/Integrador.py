
def medias (criteria, ratings):


    # inicializa a lista de medias 
    medias = [[[] for _ in criteria] for _ in ratings]
    print(f'medias: {medias}')

    # Inicia um novo loop atraves da lista de somas 
    for separator_index, separator_list in enumerate(ratings):

        # print(f'separator_list: {separator_list}')

        # pra cada criterio na sprint
        for criteria_index, criteria_list in enumerate(separator_list):
            if len(criteria_list) == 0: continue

            # print(f'criteria_list: {criteria_list}')

            # define a média desse criterio nessa sprint como a soma das notas dividida pela contagem de avaliações
            medias[separator_index][criteria_index] = sum(criteria_list) / len(criteria_list)
            print(f'medias[{separator_index}][{criteria_index}] = {sum(criteria_list)} / {len(criteria_list)} = {sum(criteria_list) / len(criteria_list)}')
            
    print(f'medias: {medias}')

    return medias


# Retorna a média por criterio por sprint das ratings especificadas
def medias_por_sprint (criteria, sprints, ratings):

    aisuh = [f'{str(r.value)}' for r in ratings]
    # print(f'ratings: {aisuh}')

    # inicializa uma lista para a classificação das ratings passadas como parametro
    # classified é uma lista de separadores em que cada separador corresponde a uma sprint
    # cada separador é uma lista que possui um indice para cada critério
    # cada critério é uma lista onde será armazenado cada valor em ratings
    # classified [
    #     separator [
    #         criteria [
    #             nota
    #             ...
    #         ]
    #     ]
    # ]
    classified = [[[] for _ in criteria] for _ in sprints]

    print(f'classified: {classified}')

    # loop através de ratings
    for rating in ratings:

        # Adiciona o valor da rating dentro da lista do critério de sua sprint
        classified[rating.sprint_id][rating.criteria_id].append(rating.value)

    # print(f'classified: {classified}')

    # retorna o valor de médias para a lista classificada
    return medias(criteria, classified)


# Classifica as ratings em critério
def classify_criteria (criteria, ratings):
    classified = [[] for _ in criteria]
    # print(f'classified: {classified}')
    for r in ratings:
        classified[r.criteria_id].append(r.value)
    # print(f'classified: {classified}')
    return classified
