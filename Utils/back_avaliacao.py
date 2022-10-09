from Models.Ratings import create_rating
from Users.Authentication import CURRENT_USER

# Enviar as respotas para o banco de dados, com as identificações necessárias:
# - Id de quem está avaliando
# - Id de quem está sendo avaliado
# - Sprint da avaliação
# - Nota (1 a 5)
# - Critério avaliativo

# def create_rating (from_user_id, to_user_id, value, comment, sprint, criteria):
    # return add_unique_csv_autoid(RATINGS_PATH, [from_user_id, to_user_id, value, comment, sprint, criteria])

def dados_autoavaliacao(notas, feedback):
    from Models.id_criteria import criteria
    for i, c in enumerate(criteria):
        create_rating(CURRENT_USER.id, CURRENT_USER.id, notas[i], feedback[i], 'sprint', c)

def dados_avaliacao(to_user_id, notas, feedback):
    from Models.id_criteria import criteria
    for i, c in enumerate(criteria):
        create_rating(CURRENT_USER.id, to_user_id, notas[i], feedback[i], 'sprint', c)
        
# Localizar banco que registra os ids e vincular avaliador e avaliado
# Localizar banco que registra sprints
# Criar id do critério para facilitar a localização dos dados nos Dashboards

# Como chamar as respostas das escalas?
# Como chamar as respostas descritivas?