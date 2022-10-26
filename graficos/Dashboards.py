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
        plt.bar(positions, lst, color=colors[i], width=bar_width, label=names[i])

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
        plt.plot(positions, value, color=colors[i], label=names[i])

    plt.title(title)

    plt.xlabel(x_label)
    plt.xticks([r + barWidth for r in range(len(x_ticks))], x_ticks)

    plt.ylabel(y_label)

    plt.legend()

    plt.show()


# Retorna um Dashboard com a media de um determinado time em cada criterio por sprint
def time_media_sprints (team_id):
    # medias = [
    #     [2, 3, 4, 4, 5],
    #     [2, 5, 3, 4, 2],
    #     [5, 3, 4, 5, 2],
    #     [5, 3, 4, 5, 3]
    # ]

    from CSV.CSVHandler import find_data_by_id_csv, find_data_list_by_field_value_csv, find_data_list_by_field_values_csv
    from Settings import USERS_PATH, TEAMS_PATH, SPRINTS_PATH, RATINGS_PATH
    from Models.Sprints import to_sprint
    from Models.id_criteria import criteria

    team = find_data_by_id_csv(TEAMS_PATH, team_id)
    
    sprints = [to_sprint(x) for x in find_data_list_by_field_value_csv(SPRINTS_PATH, 'group_id', team['group_id'])]
    user_ids = [int(x['id']) for x in find_data_list_by_field_value_csv(USERS_PATH, 'team_id', team_id)]
    ratings = find_data_list_by_field_values_csv(RATINGS_PATH, 'to_user_id', user_ids)

    # [sprint] [criterio]
    sums   = [[0] * len(criteria) for _ in sprints]
    counts = [[0] * len(criteria) for _ in sprints]
    medias = [[0] * len(criteria) for _ in sprints]

    for medias_index in range(len(criteria)):
        for rating in ratings:
            r_criteria_id = int(rating['criteria'])
            if r_criteria_id != medias_index:
                continue
            r_sprint_id = int(rating['sprint_id'])
            sums[r_sprint_id][medias_index] += float(rating['value'])
            counts[r_sprint_id][medias_index] += 1.

    for medias_index, sum_sprint in enumerate(sums):
        for criteria_index, sum_criteria in enumerate(sum_sprint):
            if counts[medias_index][criteria_index] == 0:
                continue
            medias[medias_index][criteria_index] = sum_criteria / counts[medias_index][criteria_index] 

    print(f'sums: {sums}')
    print(f'counts: {counts}')

    print(f'medias: {medias}')

    multi_bar(
        f'Média do time {team["name"]} ao longo das sprints',
        [f'Sprint {i}' for i in range(len(sprints))],
        'Médias',
        medias,
        'Críterio avaliativo',
        criteria,
        ['orange', 'yellow', 'red', 'green', 'blue', 'magenta', 'cyan', 'gray', ]
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


