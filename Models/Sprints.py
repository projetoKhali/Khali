from datetime import date
from CSV.CSVHandler import *
from Settings import SPRINTS_PATH 

# Define a classe Sprint para facilitar a utilização no código
class Sprint:
    def __init__(self, group_id, start, finish, rating_period):
        self.group_id = group_id
        self.start = start
        self.finish = finish
        self.rating_period = rating_period
    def __str__(self):
        return f'Sprint[group_id: {self.group_id}, start: {self.start}, finish: {self.finish}, rating_period: {self.rating_period}]'

# Retorna a sprint atual conforme a data de hoje 
def current_sprint(group_id):
    from CSV.CSVHandler import find_data_list_by_field_value_csv
    import datetime

    today = date.today()

    # requisita as sprints salvas no banco de dados e faz um loop pela lista retornada
    # após converter cada sprint dicionario em objeto da classe Sprint 
    for sprint in [to_sprint(x) for x in find_data_list_by_field_value_csv(SPRINTS_PATH, 'group_id', group_id)]:
        if today >= sprint.start and today <= sprint.finish + datetime.timedelta(days=sprint.rating_period):
            return sprint

# Converte dicionario em sprint
def to_sprint(sprint_dict):
    return Sprint(
        int(sprint_dict['group_id']),
        to_date(sprint_dict['start']),
        to_date(sprint_dict['finish']),
        int(sprint_dict['rating_period'])
    )

# Converte uma data de str para date
def to_date(value:str):
    fields = [int(s) for s in value.split('-')]
    return date(fields[0], fields[1], fields[2])

# Cria uma sprint e salva na database
# parametros:
# group_id - o id do grupo do qual a sprint é pertencente
# start    - a data de inicio da sprint
# finish   - a data de término da sprint
# rating_period - a quantidade de dias disponíveis para efetur as avaliações referentes a sprint
def create_sprint (group_id:int, start:date, finish:date, rating_period:int):
    return add_unique_csv_autoid(SPRINTS_PATH, [group_id, start, finish, rating_period])
