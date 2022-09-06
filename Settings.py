
# O local onde os arquivos .csv estão localizados
USERS_PATH  = "data/users"
GROUPS_PATH = "data/groups"
TEAMS_PATH  = "data/teams"

# Os campos que cada banco de dados irá possuir ao ser inicializado
PATH_FIELDS = [
#   Caminho do arquivo .csv   |           | id |                  campos                   | 
    { 'path': USERS_PATH,       'fields': ['id', 'name', 'email', 'group', 'team', 'role'] },
    { 'path': GROUPS_PATH,      'fields': ['id', 'name'] },
    { 'path': TEAMS_PATH,       'fields': ['id', 'group', 'name',] },
]

# Tamanho da senha autogerada para cadastro de usuários
AUTO_GEN_PW_SIZE = 7

# Mínimo e máximo número de caracteres permitido para o nome do Usuário
USER_NAME_MIN_MAX = (3, 24)

# Cores do Console
COLS = [
    '\u001b[0m', # Reset

    '\u001b[37m', # White

    '\u001b[31m', # Red
    '\u001b[32m', # Green
    '\u001b[33m', # Yellow

    '\u001b[34m', # Blue
    '\u001b[35m', # Magenta
    '\u001b[36m', # Cyan
]