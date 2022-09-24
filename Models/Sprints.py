from datetime import date
from CSV.CSVHandler import *
from Settings import SPRINTS_PATH 

# Cria uma sprint e salva na database
# parametros:
# group_id - o id do grupo do qual a sprint é pertencente
# start    - a data de inicio da sprint
# finish   - a data de término da sprint
# rating_period - a quantidade de dias disponíveis para efetur as avaliações referentes a sprint
def create_sprint (group_id:int, start:date, finish:date, rating_period:int):
    return add_unique_csv_autoid(SPRINTS_PATH, [group_id, start, finish, rating_period])
