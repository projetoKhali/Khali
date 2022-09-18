# Define as permissoes disponiveis
PERMISSIONS = [

    # Cadastros exclusivos do ADM
    'REG_USER_GROUPLEADER',             # 0  # Lider do grupo
    'REG_USER_CLIENT',                  # 1  # Cliente
    'REG_GROUP',                        # 2  # Grupo

    # Cadastros exclusivos do Lider do Grupo
    'REG_SPRINT',                       # 3  # Sprint
    'REG_TEAM',                         # 4  # Time
    'REG_USER_TECHLEADER',              # 5  # Lider Técnico / Lider do Time
    'REG_USER_PRODUCTOWNER',            # 6  # Product Owner / PO
    'REG_USER_DEVELOPER',               # 7  # Developer / Integrante

    # Avaliação de usuários 
    'RATE_USER_TECHLEADER',             # 8  #
    'RATE_USER_PRODUCTOWNER',           # 9  #
    'RATE_USER_DEVELOPER',              # 10 #

    # # Visualização de avaliações de usuários
    # 'VIEW_USER_RATING_PRODUCTOWNER',    # 11 #
    # 'VIEW_USER_RATING_TECHLEADER',      # 12 #
    # 'VIEW_USER_RATING_DEVELOPER',       # 13 #
]
