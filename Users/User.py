
# definição do namespace de Usuário. Ao usar 'import Users', importará todos os metodos relacionados a usuários
def Users():

    # insira imports aqui

    # Define o objeto "Usuário"
    class User:

        # o nome do usuário
        name = ""

        # o email do usuário
        email = ""

        # a equipe que o usuário pertence
        group = None

        # a função do usuário na equipe
        role = None

        # método construtor para criar um novo usuário
        def __init__(self, _name, _email, _group, _role):

            # ao criar um usuário, os parametros passados serão registrados ao valor das variáveis
            name = _name
            email = _email
            group = _group
            role = _role

