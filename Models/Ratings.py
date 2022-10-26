from CSV.CSVHandler import *
from Settings import RATINGS_PATH 

# Cria uma avaliação e salva na database
# parametros:
# from_user_id  - O usuário que está avaliando
# to_user_id    - O usuário que está sendo avaliado
# value         - O valor da avaliação
# comment       - Feedback
# sprint        - Número da sprint
# criterio      - 1 dos 5 critérios avaliativos
def create_rating (from_user_id, to_user_id, sprint, criteria, value, comment):
    return add_unique_csv_autoid(RATINGS_PATH, [from_user_id, to_user_id, sprint, criteria, value, comment])
