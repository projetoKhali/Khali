

# calcula as medias por sprint utilizando as avaliações especificadas
def medias_por_sprint (criteria, sprints, ratings):

    # inicializa as listas de soma, contagem e medias 
    # em que cada item da lista corresponde a uma lista com o valor para cada criterio:
    # lista [index_sprint] [index_criterio] = valor
    #
    # lista [
    #   sprint 1 [
    #       valor criterio 1
    #       ...
    #   ]
    #   sprint 2 [...]
    #   sprint 3 [...]
    # ]
    #
    sums   = [[0] * len(criteria) for _ in sprints]
    counts = [[0] * len(criteria) for _ in sprints]
    medias = [[0] * len(criteria) for _ in sprints]

    # Loop atraves do indice de cada criterio
    for criteria_index in range(len(criteria)):

        # verifica cada avaliação da lista 
        for rating in ratings:

            # adquire o indice do criterio da avaliação
            r_criteria_id = rating.criteria_id

            # ignora a avaliação caso o criterio não seja o criterio da iteração atual do loop de criterios
            if r_criteria_id != criteria_index:
                continue

            # criterio da avaliação é o criterio atual do loop
            # adquire o indice da sprint especificado na avaliação 
            r_sprint_id = rating.sprint_id

            # soma o valor da avaliação na lista de somas com o indice da sprint seguido por indice do criterio
            sums[r_sprint_id][criteria_index] += rating.value

            # incrementa o contador do criterio na sprint
            counts[r_sprint_id][criteria_index] += 1.

            # Ao terminar o loop teremos uma lista de somas em que cada item é uma lista correspondendo a uma sprint
            # & cada lista de sprint possui um valor de soma e de contagem para cada criterio

    # Inicia um novo loop atraves da lista de somas 
    for sprint_index, sum_sprint in enumerate(sums):

        # pra cada criterio na sprint
        for criteria_index, sum_criteria in enumerate(sum_sprint):

            # ignora a media desse criterio na sprint caso não hajam avaliações (evvita divisão por 0)
            if counts[sprint_index][criteria_index] == 0:
                continue

            # define a média desse criterio nessa sprint como a soma das notas dividida pela contagem de avaliações
            medias[sprint_index][criteria_index] = sum_criteria / counts[sprint_index][criteria_index] 

    # print(f'sums: {sums}')
    # print(f'medias: {medias}')
    return medias
