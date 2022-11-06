from Models.Sprint import Sprint
from Models.Rating import Rating

# retorna uma lista com as médias de cada critério especificado utilizando a lista de avaliações para o calculo
def medias (criteria:list[str], ratings:list[list[list[Rating]]]):

    """ estrutura da lista ratings:
    ratings [
    |-- separador1 [ 
    |   |-- criteria1 [ 
    |   |   |-- n1, 
    |   |   |-- n2, 
    |   |   |-- n3
    |   |   ], 
    |   |-- criteria2 [ ... ],
    |   |-- criteria3 [ ... ]
    |   ], 
    |-- separador2 [ ... ],
    |-- separador3 [ ... ] 
    ]
    """

    # inicializa a lista de medias 
    medias = [[[] for _ in criteria] for _ in ratings]
    # print(f'medias: {medias}')

    # Inicia um loop através dos separadores 
    # ratings[separator_index] = [ criterio1 [ n1, n2, n3], criterio2 [ ... ] ]
    for separator_index, separator_list in enumerate(ratings):

        # pra cada criterio no separador
        # separator_list[criteria_index] = [ n1, n2, n3 ]
        for criteria_index, criteria_list in enumerate(separator_list):

            # se a lista do critério não possui notas, ignore-a a vá para o próximo criterio para evitar divisão por 0
            if len(criteria_list) == 0: continue

            # define a média desse criterio nesse separador como a soma das notas dividida pela contagem de avaliações
            medias[separator_index][criteria_index] = sum(criteria_list) / len(criteria_list)
            # print(f'medias[{separator_index}][{criteria_index}] = {sum(criteria_list)} / {len(criteria_list)} = {sum(criteria_list) / len(criteria_list)}')
            
    # print(f'medias: {medias}')

    # retorna a lista de médias calculadas para cada critério
    return medias


# Retorna a média por criterio por sprint das ratings especificadas
def medias_por_sprint (criteria:list[str], sprints:list[Sprint], ratings:list[Rating]):

    # inicializa uma lista para a classificação das ratings passadas como parametro
    # classified é uma lista de separadores em que cada separador corresponde a uma sprint
    # cada separador é uma lista que possui um indice para cada critério
    # cada critério é uma lista onde será armazenado cada valor em ratings
    classified = [[[] for _ in criteria] for _ in sprints] 

    # Cria um dicionário que 
    sprint_indexes = { sprint.id : i for i, sprint in enumerate(sprints) }

    # loop através de ratings
    for rating in ratings:

        # Adiciona o valor da rating dentro da lista do critério de sua sprint
        classified[sprint_indexes[rating.sprint_id]][rating.criteria_id].append(rating.value)

    # retorna o valor de médias para a lista classificada
    return medias(criteria, classified)


# Classifica as ratings em critério
def classify_criteria (criteria:list[str], ratings:list[Rating]):

    # Cria uma lista em que cada elemento é uma lista de notas correspondendo a um critério
    # classified [ criterio1 [ n1, n2, n3 ], criterio2 [ ... ], criterio3 [ ... ] ]
    classified = [[] for _ in criteria]

    # para cada avaliação na lista
    for r in ratings:

        # adiciona à lista do critério dentro de classified
        classified[r.criteria_id].append(r.value)

    # retorna a lista classificada por critério
    return classified
