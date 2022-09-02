
# O local onde os arquivos .csv estão localizados
USERS_PATH  = "data/users"
GROUPS_PATH = "data/groups"
TEAMS_PATH  = "data/teams"

# Mínimo e máximo número de caracteres permitido para o nome do Usuário
USER_NAME_MIN_MAX = (3, 24)

ROLES = [
    "ADM",

    # 1 por Grupo
    "Lider do Grupo",
    "Cliente",

    # 1 por Time
    "Lider Técnico",
    "Product Owner",
    "Developer"
]

