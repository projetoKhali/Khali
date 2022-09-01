
# Insira imports aqui para utilizá-los sem incluir no namespace (ao importar Users, NÃO importará também estes imports)
from CSV import CSVHandler
from Users.User import User

import UserSettings as settings

# Definição do namespace Authentication referente ao Cadastro & Login de usuários 
def Authentication():

    # Insira imports aqui para incluí-los dentro do namespace (ao importar Users, importará também estes outros imports)

#region Users

    # Efetua o Cadastro de um novo Usuário e, se efetuado com sucesso, o armazena na database .csv
    def register (name, email, group_id, team_id, role_id):

        # Verifica se o email fornecido é valido
        if not validate_email(email):
            print(f'Erro ao cadastrar usuario: Email fornecido não é válido')

        user = User(name, email, group_id, team_id, role_id)

        # Adiciona o usuário para a database
        CSVHandler.add_line_csv(settings.users_path, get_user_fields(user))


    # Retorna uma lista com as informações de um Usuário
    def get_user_fields (user:User):
        return list({
            user.name,
            user.email,
            get_group_name(user.group_id),
            get_team_name(user.team_id),
            settings.roles[user.role_id]
        })

    # Retorna True se o email especificado é valido e False se não
    def validate_email(email:str):

        # Importa (localmente dentro do escopo da função) a biblioteca 're' 
        # que corresponde a funcionalidade de regex (Regular Expressions)
        import re

        # Define o padrão regex a ser comparado: Deve conter exatamente um '@' e um '.' após o '@'
        email_regex_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")

        # Compara o email especificado utilizando o padrão regex e retorna o resultado
        return email_regex_pattern.match(email)


#endregion

#region Grupos

    # retorna o nome do xxxxxxx que corresponde ao id especificado 
    def get_group_name (id:int):
        CSVHandler.load_line(settings.groups_path, id)

#endregion

#region Times

    # retorna o nome do xxxxxxx que corresponde ao id especificado 
    def get_team_name (id:int):
        CSVHandler.load_line(settings.teams_path, id)

#endregion
