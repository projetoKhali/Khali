# O caminho onde os arquivos .csv estão/estarão localizados
USERS_PATH  = "data/users"
GROUPS_PATH = "data/groups"
SPRINTS_PATH = "data/sprints"
TEAMS_PATH  = "data/teams"

RESOURCES_PATH  = "resources"

# Os campos que cada banco de dados irá possuir ao ser inicializado
PATH_FIELDS = [
#   Caminho do arquivo .csv   |           | id |                        campos                         | 
    { 'path': USERS_PATH,       'fields': ['id', 'name', 'email', 'group_id', 'team_id', 'role_id', 'password'] },
    { 'path': GROUPS_PATH,      'fields': ['id', 'name'] },
    { 'path': SPRINTS_PATH,     'fields': ['id', 'group', 'start', 'finish', 'rating period'] },
    { 'path': TEAMS_PATH,       'fields': ['id', 'group', 'name',] },
]

SEND_EMAIL_ON_REGISTER = False

# Mínimo e máximo número de caracteres permitido para o nome do Usuário
USER_NAME_MIN_MAX = (3, 24)

# Mínimo e máximo número de caracteres permitido para o nome do Usuário
PASSWORD_MIN_MAX = (3, 24)

# Tamanho da senha autogerada para cadastro de usuários
AUTO_GEN_PW_SIZE = 7

# Cores do Console
COLS = [
    '\u001b[0m',  # [0] Reset

    '\u001b[37m', # [1] White

    '\u001b[31m', # [2] Red
    '\u001b[32m', # [3] Green
    '\u001b[33m', # [4] Yellow

    '\u001b[34m', # [5] Blue
    '\u001b[35m', # [6] Magenta
    '\u001b[36m', # [7] Cyan
]

# Cores hash (front / tkinter)
co0 = "#FAE8E8" #rosa
co1 = "#D9D9D9" #cinza
co2 = "1A1D1A" #preta
