
# O local onde os arquivos .csv estão localizados
users_path  = "data/users"
groups_path = "data/groups"
teams_path  = "data/teams"

# Mínimo e máximo número de caracteres permitido para o nome do Usuário
NAME_MIN_MAX = (3, 24)

roles = [
    "ADM",

    # 1 por turma
    "Lider do Grupo",
    "Cliente",

    # 1 por time
    "Lider Técnico",
    "Product Owner",
    "Developer"
]

