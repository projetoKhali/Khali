from . import cadastro_adm, cadastro_lider, lista_usuarios
from Settings import COLS

# Define os módulos disponíveis
MODULES = [
    lista_usuarios,
    cadastro_adm,
    cadastro_lider,
]

# Retorna os modulos disponiveis para o usuário logado
def get_modules():
    print(COLS[6] + f'ModulesManager.get_modules -- iniciando requisição de modulos' + COLS[0])
    from Users.Authentication import CURRENT_USER
    from Models import Role 

    # define o tipo do usuário logado
    role = Role.get_role(int(CURRENT_USER.role_id))

    # inicializa uma lista de modulos a serem retornados
    allowed_modules = []

    # para cadaa modulo dentre os existentes,
    for module in MODULES:
        print(COLS[6] + f'ModulesManager.get_modules -- verifiando modulo {module.NAME}' + COLS[0])

        # verifica se as permissões do tipo do usuario logado 
        # correspondem as permissões necessárias para o modulo 
        if check_permissions(role.permissions_reg , module.REQUIRED_PERMISSIONS_REG , module.NAME+'_REG') \
        or check_permissions(role.permissions_rate, module.REQUIRED_PERMISSIONS_RATE, module.NAME+'_RATE') \
        or check_permissions(role.permissions_view, module.REQUIRED_PERMISSIONS_VIEW, module.NAME+'_VIEW') :

            # permissões necessárias cumpridas, adiciona o modulo na lista 
            allowed_modules.append(module)

    # printa a lista de modulos permitidos e a retorna
    print(COLS[6] + f'ModulesManager.get_modules -- allowed_modules: {allowed_modules}' + COLS[0])
    return allowed_modules

# Retorna True caso as permissões fornecidas correspondem as permissões necessárias do modulo target
def check_permissions(permissions, required_permissions, name = "unnamed"):
    print(COLS[5] + f'ModulesManager.check_permissions -- module {name}: ' + COLS[0])

    if None in required_permissions:
        print(COLS[2] + f'ModulesManager.check_permissions -- module {name}: \'None\' encontrado, lista será ignorada' + COLS[0])
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
    print(COLS[3] + f'ModulesManager.check_permissions -- module {name}: {p_fulfilled} of {len_required} fulfilled '+ COLS[0])

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
            print(COLS[3] + f'ModulesManager.check_required -- required permission {required} GRANTED!' + COLS[0])
            return True

    # Loop finalizado sem encontrar uma correspondencia, nenhuma permissão em 'permissions' corresponde a 'required'
    print(COLS[2] + f'ModulesManager.check_required -- required permission {required} DENIED!' + COLS[0])
    return False

# Retorna True caso a permissão fornecida corresponda a permissão 'required'
# Ou, caso 'required' seja uma lista, retorna True caso 'permission' corresponda a uma das permissões em 'required'
def check_permission(permission, required):

    # caso required seja um numero, retorna a comparação de ambas
    if type(required) is int:
        print(f'ModulesManager.check_permission -- required is int | {permission} == {required}? {permission == required}')
        return permission == required

    # caso 'required' NÃO seja uma lista, retorna False pois required deve ser apenas 'int' ou 'list'
    if type(required) is not list:
        print(f'ModulesManager.check_permission -- ERROR -- required is not list! invalid required! ')
        return False

    # 'required' é uma lista, retorna o resultado da verificação de pertinencia
    print(f'ModulesManager.check_permission -- required is list | {permission} in {required}? {permission in required}')
    return permission in required
