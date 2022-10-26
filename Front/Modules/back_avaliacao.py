from CSV import CSVHandler as handler
from Front.Modules.avaliacao import resposta
import Settings
from Models import Ratings as rt
from Users.Authentication import CURRENT_USER


# Enviar as respotas para o banco de dados, com as identificações necessárias:
# - Id de quem está avaliando
# - Id de quem está sendo avaliado
# - Sprint da avaliação
# - Nota (1 a 5)
# - Critério avaliativo

# def create_rating (from_user_id, to_user_id, value, comment, sprint, criteria):
    # return add_unique_csv_autoid(RATINGS_PATH, [from_user_id, to_user_id, value, comment, sprint, criteria])

# def criar_dados():
#     rt.create_rating(CURRENT_USER.id, 'to_user_id', resposta, resposta(p1, criar_entrada), 'sprint', 't_e')
#     rt.create_rating(CURRENT_USER.id, 'to_user_id', resposta(p2), resposta(p2, criar_entrada), 'sprint', 'i_p')
#     rt.create_rating(CURRENT_USER.id, 'to_user_id', resposta(p3), resposta(p3, criar_entrada), 'sprint', 'a_a')
#     rt.create_rating(CURRENT_USER.id, 'to_user_id', resposta(p4), resposta(p4, criar_entrada), 'sprint', 'e_r')
#     rt.create_rating(CURRENT_USER.id, 'to_user_id', resposta(p5), resposta(p5, criar_entrada), 'sprint', 'c_t')

# Localizar banco que registra os ids e vincular avaliador e avaliado
# Localizar banco que registra sprints
# Criar id do critério para facilitar a localização dos dados nos Dashboards

# Como chamar as respostas das escalas?
# Como chamar as respostas descritivas?