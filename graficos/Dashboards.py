# from matplotlib.figure import Figure
from .Integrador import *

def multi_bar (title, names, y_label, matriz, x_label, x_ticks):
    from matplotlib import pyplot

    # ind = np.arange(len(x_ticks))  # the x locations for the groups
    fig, ax = pyplot.subplots(figsize = (5,5))
    ax.set_ylim([1, 5])
    bar_width = 1. / (len(matriz) + 1.75)

    for i, lst in enumerate(matriz):

        # Define a posição da barra. Indice da barra * espaçamento definido pela quantidade de barras por x_tick
        offset = (i * bar_width) 

        # move todas as barras para esquerda em (tamanho total da soma das barras / 2)
        offset -= bar_width * int(len(matriz) / 2)

        # caso o numero de barras seja par, move o metade do tamanho de UMA barra para a direita
        if len(matriz) % 2 == 0: offset += bar_width / 2

        # define a posição de cada barra da lista de indice 'i'
        positions = [j + offset for j in range(len(x_ticks))]

        ax.bar_label(
            ax.bar(positions, lst, width=bar_width, label=names[i]
        ), fmt='%.1f', padding=3)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    ax.set_title(title)

    ax.set_xticks([i for i in range(len(x_ticks))])
    ax.set_xticklabels(x_ticks)

    ax.legend()

    fig.tight_layout()

    return fig

# Gera um grafico de linha
def line (title, names, y_label, values, x_label, x_ticks, colors):
    from matplotlib import pyplot

    pyplot.rcParams['toolbar'] = 'None'

    # Define a ampliação do grafico
    # pyplot.figure(figsize = (10, 5))
    barWidth = .2 

    for i, value in enumerate(values):

        # Aqui eu construo a barra
        positions = [j + barWidth for j in range(len(x_ticks))]
        pyplot.plot(positions, value, color=colors[i % len(colors)], label=names[i])

    pyplot.ylim([0, 5])

    pyplot.title(title)

    pyplot.xlabel(x_label)
    pyplot.xticks([r + barWidth for r in range(len(x_ticks))], x_ticks)

    pyplot.ylabel(y_label)

    pyplot.legend()

    pyplot.show()


def pie_chart ():
    pass

# |--------------------------------------------------------------------------------------------------------------------|
# |                                         Gráficos a serem desenvolvidos                                             |
# |--------------------------------------------------------------------------------------------------------------------|
# |                         |    calculo    |     barras     |      label       |    acesso     |       função         |
# |--------------------------------------------------------------------------------------------------------------------|
# | media membro            |    sprint     |     sprint     |     criterio     |   PO LT DEV   |  user_media_sprints  |
# | media membro / time     |    sprints    | membro / time  |     criterio     |   PO LT DEV   |  user_media_x_team   |
# | media de cada time      |    sprints    |      time      |     criterio     |     LG FK     |     teams_media      |!
# | media membros da função |    sprints    |      time      |     criterio     |     LG FK     |      role_media      |!
# |--------------------------------------------------------------------------------------------------------------------|
# | media do time           |    sprint     |     sprint     |     criterio     |     PO LT     |  team_media_sprints  |
# |--------------------------------------------------------------------------------------------------------------------|
# | media membros time      |    sprint     |     membro     |     criterio     |     PO LT     |   users_media_team   |!
# | media do grupo          |    sprints    |     sprint     |     criterio     |     PO LT     | group_media_sprints  |!
# |--------------------------------------------------------------------------------------------------------------------|


from Models.id_criteria import criteria         # importa a lista de criterios utilizados nas avaliações
from Models.Sprint import get_group_sprints     # função usada para durante a classificação de valores por sprint


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
    return multi_bar(
        f'Média de {user.name} ao longo das sprints',
        [f'Sprint {i}' for i in range(len(sprints))],
        'Médias',
        medias_por_sprint(criteria, sprints, ratings),
        'Critério avaliativo',
        criteria
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
    # print(user_ratings)
    # cria uma lista de avaliações em que o primeiro indice corresponde às avaliações do usuário
    # e o segundo índice corresponde às avaliações do time
    ratings = [
        classify_criteria(criteria, user_ratings), 
        classify_criteria(criteria, team_ratings)
    ]

    team_name = get_team(user.team_id).name

    # Renderiza o grafico representando as médias calculadas 
    return multi_bar(
        f'Médias de {user.name} em comparativo ao time {team_name}',
        [user.name, team_name],
        'Médias',
        medias(criteria, ratings),
        'Critério avaliativo',
        criteria,
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
    return multi_bar(
        f'Média do time {team.name} ao longo das sprints',
        [f'Sprint {i}' for i in range(len(sprints))],
        'Médias',
        medias_por_sprint(criteria, sprints, ratings),
        'Critério avaliativo',
        criteria,
    )


# Renderiza um Dashboard com a media de uma determinada função de cada time
def teams_media (group_id):

    # importa as funções de acesso ao banco de dados de cada modelo
    from Models.Rating import get_ratings_to_team
    from Models.Team import get_teams_of_group
    from Models.Group import get_group

    # Pega todos os times do grupo especificado
    teams = get_teams_of_group(group_id)
    
    # Inicializa uma lista para as avaliações que serão classificadas / filtradas
    ratings = [[] for _ in teams]

    # Adiciona a lista de avaliações filtrada para a lista ratings 
    for i, team in enumerate(teams):
        ratings[i] = classify_criteria(criteria, get_ratings_to_team(team.id))

    # print(ratings)

    # Renderiza o grafico representando as médias calculadas 
    return multi_bar(
        f'Média dos times no grupo {get_group(group_id).name}',
        [team.name for team in teams],
        'Médias',
        medias(criteria, ratings),
        'Critério avaliativo',
        criteria,
        )


# Renderiza um Dashboard com a media de uma determinada função de cada time
def role_media (role_id, group_id):

    # importa as funções de acesso ao banco de dados de cada modelo
    from Models.Rating import get_ratings_to_team
    from Models.Team import get_teams_of_group

    # Pega todos os times do grupo especificado
    teams = get_teams_of_group(group_id)
    
    # Inicializa uma lista para as avaliações que serão classificadas / filtradas
    ratings = []

    # para cada time do grupo
    for team in teams:

        # Adquire todas as avaliações do time
        ratings_team = get_ratings_to_team(team.id)
        # print(f'team {team.name}: {len(ratings_team)} ratings')

        # Caso o time não possua avaliações, oculta ele do dashboard
        if len(ratings_team) == 0: continue

        # Para cada avaliação do time
        for r in ratings_team:

            # Caso o usuário avaliado na avaliação não seja da role especificada 
            if r.to_user_id != role_id:

                # remova-o da lista de avaliações do time
                ratings_team.remove(r)

        # Adiciona a lista de avaliações filtrada para a lista ratings 
        ratings.append(classify_criteria(criteria, ratings_team))

    # Renderiza o grafico representando as médias calculadas 
    return multi_bar(
        f'Média dos {["Líderes Técnicos", "Product Owners", "Desenvolvedores"][role_id-3]}',
        [team.name for team in teams],
        'Médias',
        medias(criteria, ratings),
        'Critério avaliativo',
        criteria
    )


# Renderiza um Dashboard com a media de cada usuário de um time em cada criterio
def users_media_team (team_id):

    # importa as funções de acesso ao banco de dados de cada modelo
    from Models.Team import get_team
    from Models.User import get_users_of_team
    from Models.Rating import get_ratings_to_user

    # carrega o time com o id especificado e seus membros
    team = get_team(team_id)
    users = get_users_of_team(team_id)
    
    # Lista todas as avaliações em que o id do usuário avaliado corresponda a qualquer id da lista 'user_ids' 
    ratings = [classify_criteria(criteria, get_ratings_to_user(user.id)) for user in users]

    # Renderiza o grafico representando as médias calculadas 
    line(
        f'Média do time {team.name}',
        [x.name for x in users],
        'Médias',
        medias(criteria, ratings),
        'Critério avaliativo',
        criteria
    )


# Renderiza um Dashboard com a media de um determinado time em cada criterio de cada sprint
def group_media_sprints (group_id):

    # importa as funções de acesso ao banco de dados de cada modelo
    from Models.Group import get_group
    from Models.Rating import get_ratings_to_group

    # carrega o time com o id especificado
    group = get_group(group_id)
    
    # Lista as sprints (em objeto da classe Sprint)
    sprints = get_group_sprints(group_id)

    # Lista todas as avaliações em que o id do usuário avaliado corresponda a qualquer id da lista 'user_ids' 
    ratings = get_ratings_to_group(group_id)

    # Renderiza o grafico representando as médias calculadas 
    return multi_bar(
        f'Média do grupo {group.name} ao longo das sprints',
        [f'Sprint {i}' for i in range(len(sprints))],
        'Médias',
        medias_por_sprint(criteria, sprints, ratings),
        'Critério avaliativo',
        criteria
    )
