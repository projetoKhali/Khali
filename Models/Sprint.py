from datetime import date, timedelta
from CSV.CSVHandler import *
from Settings import SPRINTS_PATH 
from Time import today

# Define que o período avaliativo das sprints começa x dias depois do fim da sprint
# 0: começa no ultimo dia da sprint
# 1: começa no dia seguinte do fim da sprint
RATING_PERIOD_START_DELAY = 1

# Define a classe Sprint para facilitar a utilização no código
class Sprint:
    def __init__(self, group_id, start, finish, rating_period, id = None):
        self.id = id
        self.group_id = group_id
        self.start = start
        self.finish = finish
        self.rating_period = rating_period
    def __str__(self):
        return f'Sprint[id: {self.id}, group_id: {self.group_id}, start: {self.start}, finish: {self.finish}, rating_period: {self.rating_period}]'
    def rating_period_start(self):
        return self.finish + timedelta(days=RATING_PERIOD_START_DELAY)
    def rating_period_end(self):
        return self.finish + timedelta(days=self.rating_period + RATING_PERIOD_START_DELAY)

# Converte dicionario em sprint
def to_sprint(sprint_dict):
    return Sprint(
        int(sprint_dict['group_id']),
        to_date(sprint_dict['start']),
        to_date(sprint_dict['finish']),
        int(sprint_dict['rating_period']),
        int(sprint_dict['id']),
    )

# Converte uma data de str para date
def to_date(value:str):
    fields = [int(s) for s in value.split('-')]
    return date(fields[0], fields[1], fields[2])

# retorna a Sprint que corresponde ao id especificado 
def get_sprint (id:int):
    return None if id is None or id == '' else to_sprint(find_data_by_id_csv(SPRINTS_PATH, int(id)))

# Retorna a sprint atual conforme a data de hoje 
def current_sprint(group_id):
    # print('current_sprint')
    for sprint in get_group_sprints(group_id):
        # print(f'{today()} >= {sprint.start} and {today()} <= {sprint.finish + timedelta(days=sprint.rating_period)} ? {today() >= sprint.start and today() <= sprint.finish + timedelta(days=sprint.rating_period)}')
        if today() >= sprint.start and today() <= sprint.finish + timedelta(days=sprint.rating_period):
            return sprint

# Retorna a sprint do período de avaliação atual conforme a data de hoje 
def current_rating_period(group_id):
    # print('current_rating_period')
    for sprint in get_group_sprints(group_id):
        # print(f'{today()} >= {sprint.rating_period_start()} and {today()} < {sprint.rating_period_end()} ? {today() >= sprint.rating_period_start() and today() < sprint.rating_period_end()}')
        if today() >= sprint.rating_period_start() and today() < sprint.rating_period_end():
            return sprint

def previous_sprint (group_id):
    cur_sprint = current_sprint(group_id)
    if cur_sprint is None: return None
    prev_sprint = None
    for sprint in get_group_sprints(group_id):
        if sprint.id < cur_sprint.id and (lambda sprint=sprint: True if prev_sprint is None else sprint.id > prev_sprint.id):
            prev_sprint = sprint
    return prev_sprint

def next_rating_period (group_id):
    # print('\nnext_rating_period')
    next_rating_period_sprint = None
    min_time_until_start = None

    # faz um loop através das sprints do grupo
    # print(f'group_id: {group_id}')
    sprints = get_group_sprints(group_id)
    for sprint in sprints:
        # if today() < sprint.finish: continue
        time_until_start = sprint.finish + timedelta(days=1) - today()
        if time_until_start.total_seconds() < 0: continue
        # print(f'start: {sprint.start} | finish: {sprint.finish} | rps: {sprint.rating_period_start()} | rpe: {sprint.rating_period_end()} | tus: {time_until_start}')
        if min_time_until_start is None or time_until_start < min_time_until_start: 
            # print(f'NEW MIN --- start: {sprint.start} | finish: {sprint.finish} | rps: {sprint.rating_period_start()} | rpe: {sprint.rating_period_end()} | tus: {time_until_start}')
            min_time_until_start = time_until_start
            next_rating_period_sprint = sprint
    # print(f'next_rating_period_sprint: {next_rating_period_sprint} | time: {min_time_until_start}\n')
    return next_rating_period_sprint


# Retorna o indice da sprint dentro da lista com as sprints do grupo
def sprint_index(group_id, sprint_id):
    sprints = get_group_sprints(group_id)
    sprints_sorted = [None for _ in sprints]

    for i in range(len(sprints)):
        min_sprint_start = None
        next_sorted_sprint = None

        for s in sprints:
            sprint_start = s.start - (today() if i == 0 else sprints_sorted[i-1].start)
            if min_sprint_start is None or sprint_start < min_sprint_start: 
                min_sprint_start = sprint_start
                next_sorted_sprint = s
                sprints.remove(s)
                
        sprints_sorted[i] = next_sorted_sprint

    for i, s in enumerate(sprints_sorted): 
        if s.id == sprint_id: return i + 1

    return None


# Cria uma sprint e salva na database
# parametros:
# group_id - o id do grupo do qual a sprint é pertencente
# start    - a data de inicio da sprint
# finish   - a data de término da sprint
# rating_period - a quantidade de dias disponíveis para efetur as avaliações referentes a sprint
def create_sprint (group_id:int, start:date, finish:date, rating_period:int):
    return add_unique_csv_autoid(SPRINTS_PATH, [group_id, start, finish, rating_period])

# Retorna todas as sprints associadas ao grupo de id especificado após converte-las para objetos da classe Sprint
def get_group_sprints (group_id):
    return [to_sprint(x) for x in find_data_list_by_field_value_csv(SPRINTS_PATH, 'group_id', group_id)]