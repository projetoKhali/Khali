import enum
import  matplotlib.pyplot as  plt 

# Gera um grafico multi barra
def multi_bar (title, names, y_label, matrix, x_label, x_ticks, colors):

    # Esconde a barra de comandos do matplotlib
    plt.rcParams['toolbar'] = 'None'

    # Define a ampliação do grafico
    # plt.figure(figsize = (10, 5))
    
    # Define a largura de cada barra individual sendo 1 dividido pela quantidade de listas da matriz
    # somado por um valor constante de espaçamento entre cada x_tick
    bar_width = 1. / (len(matrix) + 1.75)

    # Para cada lista na matriz
    for i, lst in enumerate(matrix):

        # Define a posição da barra. Indice da barra * espaçamento definido pela quantidade de barras por x_tick
        offset = (i * bar_width) 

        # move todas as barras para esquerda em (tamanho total da soma das barras / 2)
        offset -= bar_width * int(len(matrix) / 2)

        # caso o numero de barras seja par, move o metade do tamanho de UMA barra para a direita
        if len(matrix) % 2 == 0: offset += bar_width / 2

        # define a posição de cada barra da lista de indice 'i'
        positions = [j + offset for j in range(len(x_ticks))]
        
        # Cria um grafico de barras para cada item da lista 'lst'  
        plt.bar(positions, lst, color=colors[i % len(colors)], width=bar_width, label=names[i])

    # Adiciona o título
    plt.title(title)

    # Adiciona a label e os marcadores x
    plt.xlabel(x_label)
    plt.xticks([r for r in range(len(x_ticks))], x_ticks)

    # Adiciona a label y
    plt.ylabel(y_label)

    # Adiciona a legenda representando cada lista da matriz
    plt.legend()

    # Renderiza o grafico
    plt.show()


# Gera um grafico de linha
def line (title, names, y_label, values, x_label, x_ticks, colors):
    plt.rcParams['toolbar'] = 'None'

    # Define a ampliação do grafico
    # plt.figure(figsize = (10, 5))
    barWidth = .2 

    for i, value in enumerate(values):

        # Aqui eu construo a barra
        positions = [j + barWidth for j in range(len(x_ticks))]
        plt.plot(positions, value, color=colors[i % len(colors)], label=names[i])

    plt.title(title)

    plt.xlabel(x_label)
    plt.xticks([r + barWidth for r in range(len(x_ticks))], x_ticks)

    plt.ylabel(y_label)

    plt.legend()

    plt.show()


# Retorna um Dashboard com a media de um determinado time em cada criterio de cada sprint
def time_media_sprints (team_id):

    # importa as funções do CSVHandler que serão usadas para requisitar informações dos bancos de dados
    from CSV.CSVHandler import find_data_by_id_csv, find_data_list_by_field_value_csv, find_data_list_by_field_values_csv
    # importa as variaveis em Settings que correspondem ao caminho de cada banco de dados que será acessado
    from Settings import USERS_PATH, TEAMS_PATH, SPRINTS_PATH, RATINGS_PATH
    # importa de Models.Sprints a função que converte um dicionario com os valores de uma sprint em um objeto da classe
    from Models.Sprints import to_sprint
    # importa a lista de criterios utilizados nas avaliações
    from Models.id_criteria import criteria

    # Objetivo:
    #   - calcular a média do time para cada criterio em cada sprint
    # Passos executados:
    # 1 - Requisitar do banco de dados o time do id especifiado, o id dos usuarios do time e as sprints do grupo do time
    # 2 - Requisitar do banco de dados todas as avaliações em que o usuario avaliado pertence ao time
    # 3 - Calcular a média do time em cada criterio de cada sprint utilizando as avaliações do passo 2
    # 4 - Gerar o gráfico com as informações adquiridas no passo 3

    # carrega o time com o id especificado
    team = find_data_by_id_csv(TEAMS_PATH, team_id)
    
    # Lista as sprints associadas ao grupo do time após converte-las para objetos da classe Sprint
    sprints = [to_sprint(x) for x in find_data_list_by_field_value_csv(SPRINTS_PATH, 'group_id', team['group_id'])]

    # Lista o id de cada usuário pertencente ao time especificado após convertelos para numero inteiro
    user_ids = [int(x['id']) for x in find_data_list_by_field_value_csv(USERS_PATH, 'team_id', team_id)]

    # Lista todas as avaliações em que o id do usuário avaliado corresponda a qualquer id da lista 'user_ids' 
    ratings = find_data_list_by_field_values_csv(RATINGS_PATH, 'to_user_id', user_ids)

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
            r_criteria_id = int(rating['criteria'])

            # ignora a avaliação caso o criterio não seja o criterio da iteração atual do loop de criterios
            if r_criteria_id != criteria_index:
                continue

            # criterio da avaliação é o criterio atual do loop
            # adquire o indice da sprint especificado na avaliação 
            r_sprint_id = int(rating['sprint_id'])

            # soma o valor da avaliação na lista de somas com o indice da sprint seguido por indice do criterio
            sums[r_sprint_id][criteria_index] += float(rating['value'])

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

    print(f'sums: {sums}')
    print(f'medias: {medias}')

    # Retorna o grafico representando as médias calculadas 
    multi_bar(
        f'Média do time {team["name"]} ao longo das sprints',
        [f'Sprint {i}' for i in range(len(sprints))],
        'Médias',
        medias,
        'Críterio avaliativo',
        criteria,
        ['orange', 'yellow', 'red', 'green', 'darkgoldenrod', 'brown', 'lightgreen', 'magenta', 'royalblue', 'pink', ]
    )






def PO():
    multi_bar(
        'desempenho individual',
        ['Rodrigo', 'rogerio', 'marta', 'Cleitinho'],
        'Notas',
        [
            [4, 3, 5, 4, 2],
            [5, 4, 3, 4, 6],
            [4, 2, 4, 5, 4],
            [4, 2, 4, 5, 4],
            [2, 3, 4, 5, 3]
        ],
        'Críterio avaliativo',
        ['TG', 'PO', 'KE', 'PT', 'QU'],
        ['orange', 'green', 'blue', 'pink']
    )




def estudantes ():
    multi_bar(
        'Seu desempenho em comparativo ao seu time',
        ['Sua média', 'Média dos seu time'],
        'Criterios',
        [
            [2, 3, 2, 4, 5],
            [3, 4, 2, 5, 4]
        ],
        None,
        ['TG', 'PO', 'KE', 'PT', 'QU'],
        ['orange', 'green']
    )





def Estudante_2 ():
    multi_bar(
        'Desempenho ao decorrer das Sprints',
        ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4'],
        'Criterios',
        [
            [2, 3, 2, 4, 5],
            [3, 4, 2, 5, 4],
            [4, 4, 3, 4, 3],
            [4, 5, 4, 5, 4]
        ],
        None,
        ['TG', 'PO', 'KE', 'PT', 'QU'],
        ['orange', 'green', 'blue', 'red']
    )


