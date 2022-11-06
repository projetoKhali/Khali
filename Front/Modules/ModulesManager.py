from . import cadastro_adm, cadastro_lider, lista_usuarios, edit_team
from Settings import COLS

# Define se o acompanhamento de processo via console será habilitado durante a execução
DEBUG = False

# Define os módulos disponíveis
MODULES = [
    lista_usuarios,
    cadastro_adm,
    cadastro_lider,
    edit_team
]

# Retorna os modulos disponiveis para o usuário logado
def get_modules():
    console(6, f'ModulesManager.get_modules -- iniciando requisição de modulos')
    from Authentication import CURRENT_USER
    from Models import Role 

    from Models.Group import get_group

    # define o tipo do usuário logado
    role = Role.get_role(CURRENT_USER.role_id)

    # Caso o usuário logado seja o lider ou cliente do próprio grupo, sobreescreva a função armazenada
    # em role pela função que consta no csv do grupo
    group = get_group(CURRENT_USER.group_id)
    if CURRENT_USER.role_id == group.leader_id:
        role = Role.get_role(group.leader_id)
    if CURRENT_USER.role_id == group.client_id:
        role = Role.get_role(group.client_id)

    # inicializa uma lista de modulos a serem retornados
    allowed_modules = []

    # para cadaa modulo dentre os existentes,
    for module in MODULES:
        console(6, f'ModulesManager.get_modules -- verifiando modulo {module.NAME}')

        # verifica se as permissões do tipo do usuario logado 
        # correspondem as permissões necessárias para o modulo 
        if check_permissions(role.permissions_reg , module.REQUIRED_PERMISSIONS_REG , module.NAME+'_REG' ) \
        or check_permissions(role.permissions_rate, module.REQUIRED_PERMISSIONS_RATE, module.NAME+'_RATE') \
        or check_permissions(role.permissions_view, module.REQUIRED_PERMISSIONS_VIEW, module.NAME+'_VIEW') :

            # permissões necessárias cumpridas, adiciona o modulo na lista 
            allowed_modules.append(module)

    # printa a lista de modulos permitidos e a retorna
    console(6, f'ModulesManager.get_modules -- allowed_modules: {allowed_modules}')
    return allowed_modules

# Retorna True caso as permissões fornecidas correspondem as permissões necessárias do modulo target
def check_permissions(permissions, required_permissions, name = "unnamed"):
    console(5, f'ModulesManager.check_permissions -- module {name}: ')

    if None in required_permissions:
        console(2, f'ModulesManager.check_permissions -- module {name}: \'None\' encontrado, lista será ignorada')
        return False

    # inicializa a contagem de permissões cumpridas
    p_fulfilled = 0

    # para cada permissão requerida do modulo,
    for required in required_permissions:

        # verifica se a lista de permissões do usuário contém a permissão necessária
        # caso possua, acrescenta a variavel de contagem em 1
        if check_required(permissions, required):
            p_fulfilled +=1

    # define a quantidade de permissões necessárias que devem ser cumpridas para o modulo target 
    len_required = len(required_permissions)
    console(3, f'ModulesManager.check_permissions -- module {name}: {p_fulfilled} of {len_required} fulfilled ')

    # retorna True se a contagem de permissões cumpridas for igual a quantidade de permissões solicitadas
    # caso contrario retorna False
    return p_fulfilled == len_required

# Retorna True caso a lista de permissões fornecidas contenha a permissão necessária 'required'
# Ou, caso 'required' seja uma lista, retorna True caso 'permissions' contenha uma das permissões de 'required'
def check_required(permissions, required):

    # para cada permissão em permissions,
    for permission in permissions:

        # verifica se essa permissão corresponde a 'required'
        if check_permission(permission, required):
            console(3, f'ModulesManager.check_required -- required permission {required} GRANTED!')
            return True

    # Loop finalizado sem encontrar uma correspondencia, nenhuma permissão em 'permissions' corresponde a 'required'
    console(2, f'ModulesManager.check_required -- required permission {required} DENIED!')
    return False

# Retorna True caso a permissão fornecida corresponda a permissão 'required'
# Ou, caso 'required' seja uma lista, retorna True caso 'permission' corresponda a uma das permissões em 'required'
def check_permission(permission, required):

    # caso required seja um numero, retorna a comparação de ambas
    if type(required) is int:
        console(0, f'ModulesManager.check_permission -- required is int | {permission} == {required}? {permission == required}')
        return permission == required

    # caso 'required' NÃO seja uma lista, retorna False pois required deve ser apenas 'int' ou 'list'
    if type(required) is not list:
        console(0, f'ModulesManager.check_permission -- ERROR -- required is not list! invalid required! ')
        return False

    # 'required' é uma lista, retorna o resultado da verificação de pertinencia
    console(0, f'ModulesManager.check_permission -- required is list | {permission} in {required}? {permission in required}')
    return permission in required

def console (col, message):
    if DEBUG:
        print(COLS[col] + message + COLS[0])