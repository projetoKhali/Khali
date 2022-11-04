import matplotlib
import matplotlib.pyplot as  plt 
from .Integrador import *
import numpy as np
def teste():

    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Men')
    rects2 = ax.bar(x + width/2, women_means, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    return fig

########################################################################
# reescrevendo as funções
def multi_bar_fig (matriz, names=list, y_label=str, title=str, x_label = list):
    ind = np.arange(len(x_label))  # the x locations for the groups
    # width = 0.2  # the width of the bars
    fig, ax = plt.subplots()
    width = 1. / (len(matriz) + 1.75)

    rects = []
    for i, lista in enumerate(matriz):
        
        if i % 2 == 0:
            rect = ax.bar(ind[i] - width/2, lista, width, label=names[i])
        else: 
            rect = ax.bar(ind[i] + width/2, lista, width, label=names[i])
        rects.append(rect)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.set_xticks(ind)
    ax.set_xticklabels(x_label)
    ax.legend()
    for item in rects:
        ax.bar_label(item, padding=3)
    fig.tight_layout()
    # plt.show()
    return fig

  
from Models.id_criteria import criteria
from Models.Sprint import get_group_sprints

def user_media_sprints_fig (user_id):
     # importa as funções de acesso ao banco de dados de cada modelo
    from Models.User import get_user
    from Models.Rating import get_ratings_to_user

    # carrega as informações do usuário
    user = get_user(user_id)

    # Lista as sprints (em objeto da classe Sprint)
    sprints = get_group_sprints(user.group_id)

    # Lista todas as avaliações em que o usuário está sendo avaliado 
    ratings = get_ratings_to_user(user.id)

    matrix = medias_por_sprint(criteria, sprints, ratings)

    names =[]
    for i in range(len(sprints)):
        names.append(f'Sprint {i}')

    # names = (f'Sprint {i}' for i in range(len(sprints)))

    fig = multi_bar_fig(matrix, names, 'Médias', f'Média de {user.name} ao longo das sprints', criteria)
    return fig
    
########################################################################
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

    plt.ylim([0, 5])

    # Adiciona o título
    plt.title(title)

    # Adiciona a label e os marcadores x
    plt.xlabel(x_label)
    plt.xticks([r for r in range(len(x_ticks))], x_ticks)

    # Adiciona a label y
    plt.ylabel(y_label)

    # Adiciona a legenda representando cada lista da matriz
    plt.legend()
    # return plt
    # plt.figure(figsize = (10, 5))
    # Renderiza o grafico
    # plt.show()


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

    plt.ylim([0, 5])

    plt.title(title)

    plt.xlabel(x_label)
    plt.xticks([r + barWidth for r in range(len(x_ticks))], x_ticks)

    plt.ylabel(y_label)

    plt.legend()

    plt.show()

# |------------------------------------------------------------------------------------------------------------------|
# |
# |------------------------------------------------------------------------------------------------------------------|
# |                         |    calculo    |    barras     |      label      |    acesso     |       função         |
# |------------------------------------------------------------------------------------------------------------------|
# | media membro            |    sprint     |    sprint     |     criterio    | PO LT DEV     |  user_media_sprints  |
# | media membro / time     |    sprints    | membro / time |     criterio    | PO LT DEV     |  user_media_x_team   |
# | media de cada time      |    sprints    |     time      |     criterio    | LG FK         |     teams_media      |
# | media membros da função |    sprints    |    membro     |       time      | LG FK         |      role_media      |
# |------------------------------------------------------------------------------------------------------------------|
# | media do time           |    sprint     |    sprint     |     criterio    | PO LT         |  team_media_sprints  |
# |------------------------------------------------------------------------------------------------------------------|
# | media membros time      |    sprint     |    membro     |     criterio    | PO LT         |                      |
# | media do grupo          |    sprint     |    sprint     |     criterio    | PO LT         |                      |
# |------------------------------------------------------------------------------------------------------------------|


# importa a lista de criterios utilizados nas avaliações
from Models.id_criteria import criteria
from Models.Sprint import get_group_sprints


# Renderiza um Dashboard comparando a media de um usuário com a média de seu time em cada criterio de cada sprint
def user_media_sprints (user_id):

    # importa as funções de acesso ao banco de dados de cada modelo
    from Models.User import get_user
    from Models.Rating import get_ratings_to_user

    # carrega as informações do usuário
    user = get_user(user_id)

    # Lista as sprints (em objeto da classe Sprint)
    sprints = get_group_sprints(user.group_id)

    # Lista todas as avaliações em que o usuário está sendo avaliado 
    ratings = get_ratings_to_user(user.id)

    # Renderiza o grafico representando as médias calculadas 
    multi_bar(
        f'Média de {user.name} ao longo das sprints',
        [f'Sprint {i}' for i in range(len(sprints))],
        'Médias',
        medias_por_sprint(criteria, sprints, ratings),
        'Critério avaliativo',
        criteria,
        ['orange', 'yellow', 'red', 'green', 'darkgoldenrod', 'brown', 'lightgreen', 'magenta', 'royalblue', 'pink', ]
    )


# Renderiza um Dashboard comparando a media de um usuário com a média de seu time em cada criterio
def user_media_x_team (user_id):

    # importa as funções de acesso ao banco de dados de cada modelo
    from Models.User import get_user
    from Models.Team import get_team
    from Models.Rating import get_ratings_to_team ,get_ratings_to_user

    # carrega as informações do usuário
    user = get_user(user_id)

    # carrega todas as avaliações do time
    user_ratings = get_ratings_to_user(user_id)
    team_ratings = get_ratings_to_team(user.team_id)
    print(user_ratings)
    # cria uma lista de avaliações em que o primeiro indice corresponde às avaliações do usuário
    # e o segundo índice corresponde às avaliações do time
    ratings = [
        classify_criteria(criteria, user_ratings), 
        classify_criteria(criteria, team_ratings)
    ]

    team_name = get_team(user.team_id).name

    # Renderiza o grafico representando as médias calculadas 
    multi_bar(
        f'Médias de {user.name} em comparativo ao time {team_name}',
        [user.name, team_name],
        'Médias',
        medias(criteria, ratings),
        'Critério avaliativo',
        criteria,
        ['orange', 'yellow', 'red', 'green', 'darkgoldenrod', 'brown', 'lightgreen', 'magenta', 'royalblue', 'pink', ]
    )


# Renderiza um Dashboard com a media de um determinado time em cada criterio de cada sprint
def team_media_sprints (team_id):

    # importa as funções de acesso ao banco de dados de cada modelo
    from Models.Team import get_team
    from Models.Rating import get_ratings_to_team

    # carrega o time com o id especificado
    team = get_team(team_id)
    
    # Lista as sprints (em objeto da classe Sprint)
    sprints = get_group_sprints(team.group_id)

    # Lista todas as avaliações em que o id do usuário avaliado corresponda a qualquer id da lista 'user_ids' 
    ratings = get_ratings_to_team(team_id)

    # Renderiza o grafico representando as médias calculadas 
    multi_bar(
        f'Média do time {team.name} ao longo das sprints',
        [f'Sprint {i}' for i in range(len(sprints))],
        'Médias',
        medias_por_sprint(criteria, sprints, ratings),
        'Critério avaliativo',
        criteria,
        ['orange', 'yellow', 'red', 'green', 'darkgoldenrod', 'brown', 'lightgreen', 'magenta', 'royalblue', 'pink', ]
    )


# Renderiza um Dashboard com a media de uma determinada função de cada time
def role_media (group_id, role_id):

    # importa as funções de acesso ao banco de dados de cada modelo
    from Models.Rating import get_ratings_to_team
    from Models.Team import get_teams_of_group
    from Models.Role import get_role
    from Models.User import get_user

    role = get_role(role_id)
    teams = get_teams_of_group(group_id)
    
    # Lista todas as avaliações em que o id do usuário avaliado corresponda a qualquer id da lista 'user_ids' 
    ratings = [[]] * len(teams)
    for i, team in enumerate(teams):
        ratings[i] = [r for r in get_ratings_to_team(team) if get_user(r.to_user_id).role_id != role_id]

    # Renderiza o grafico representando as médias calculadas 
    multi_bar(
        f'Média dos {role.name}s',
        [team.name for team in teams],
        'Médias',
        medias(criteria, ratings),
        'Critério avaliativo',
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
        'Critério avaliativo',
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


