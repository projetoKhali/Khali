from CSV.CSVHandler import *
from Settings import RATINGS_PATH 

# Define a classe Rating para facilitar a utilização no código
class Rating:
    def __init__(self, from_user_id, to_user_id, sprint_id, criteria_id, value, comment):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.sprint_id = sprint_id
        self.criteria_id = criteria_id
        self.value = value
        self.comment = comment
    def __str__(self):
        return f'Rating[from_user_id: {self.from_user_id}, to_user_id: {self.to_user_id}, sprint_id: {self.sprint_id}, criteria_id: {self.criteria_id}, value: {self.value}, comment: {self.comment}]'


# Converte dicionario em rating
def to_rating(rating_dict):
    return Rating(
        int(rating_dict['from_user_id']),
        int(rating_dict['to_user_id']),
        int(rating_dict['sprint_id']),
        int(rating_dict['criteria_id']),
        int(rating_dict['value']),
        rating_dict['comment']
    ) if rating_dict is not None else None

# Cria uma avaliação e salva na database
# parametros:
# from_user_id  - O usuário que está avaliando
# to_user_id    - O usuário que está sendo avaliado
# value         - O valor da avaliação
# comment       - Feedback
# sprint        - Número da sprint
# criterio      - 1 dos 5 critérios avaliativos
def create_rating (from_user_id, to_user_id, sprint_id, criteria_id, value, comment):
    return add_unique_csv_autoid(RATINGS_PATH, [from_user_id, to_user_id, sprint_id, criteria_id, value, comment])


def get_ratings(from_user_id='IGNORE', to_user_id='IGNORE', sprint_id='IGNORE', criteria_id='IGNORE', value='IGNORE', comment='IGNORE'):
    kvps = {}
    if from_user_id != 'IGNORE': kvps.update({'from_user_id':from_user_id})
    if to_user_id != 'IGNORE': kvps.update({'to_user_id':to_user_id})
    if sprint_id != 'IGNORE': kvps.update({'sprint_id':sprint_id})
    if criteria_id != 'IGNORE': kvps.update({'criteria_id':criteria_id})
    if value != 'IGNORE': kvps.update({'value':value})
    if comment != 'IGNORE': kvps.update({'comment':comment})
    return [to_rating(x) for x in find_data_list_by_fields_value_csv(RATINGS_PATH, kvps)]

# Retorna todas as avaliações feitas pelo usuário de id especificado
def get_ratings_from_user (user_id):
    return [to_rating(x) for x in find_data_list_by_field_value_csv(RATINGS_PATH, 'from_user_id', user_id)]

# Retorna todas as avaliações feitas ao usuário de id especificado
def get_ratings_to_user (user_id):
    return [to_rating(x) for x in find_data_list_by_field_value_csv(RATINGS_PATH, 'to_user_id', user_id)]

# Retorna todas as avaliações feitas a qualquer usuário em que o id esteja presente nas lista especificada 
def get_ratings_to_users (user_ids):
    return [to_rating(x) for x in find_data_list_by_field_values_csv(RATINGS_PATH, 'to_user_id', user_ids)]

# Retorna todas as avaliações feitas aos usuários do time especificado
def get_ratings_to_team (team_id):
    from Models.User import get_users_of_team
    return get_ratings_to_users([x.id for x in get_users_of_team(team_id)])

# Retorna as avaliações feitas aos usuários de todos os times especificados
# def get_ratings_to_teams (team_ids):
#     from Models.User import get_users_of_team
#     return get_ratings_to_users([x.id for x in get_users_of_team(team_ids)])

# Retorna s avaliações de todos os usuários do grupo especificado
def get_ratings_to_group (group_id):
    from Models.User import get_users_of_group
    return get_ratings_to_users([x.id for x in get_users_of_group(group_id)])

