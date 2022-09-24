from . import cadastro_adm, cadastro_lider, lista_usuarios
from Settings import COLS

MODULES = [
    lista_usuarios,
    cadastro_adm,
    cadastro_lider,
]

def get_modules():
    from Users.Authentication import CURRENT_USER
    from Models import Role 
    role = Role.get_role(int(CURRENT_USER.role_id))
    allowed_modules = []
    for module in MODULES:
        if check_permissions(role.permissions, module):
            allowed_modules.append(module)
    print(f'allowed_modules: {allowed_modules}')
    return allowed_modules

def check_permissions(permissions, target_module):
    print(COLS[6] + f'check_permissions(): module {target_module.MODULE_NAME}: ' + COLS[0])
    p_fulfilled = 0
    for required in target_module.REQUIRED_PERMISSIONS:
        if check_required(permissions, required):
            p_fulfilled +=1
    len_required = len(target_module.REQUIRED_PERMISSIONS)
    print(COLS[7] + f'check_permissions for module {target_module.MODULE_NAME}: {p_fulfilled} of {len_required} fulfilled '+COLS[0])
    return p_fulfilled == len_required

def check_required(permissions, required):
    for permission in permissions:
        if check_permission(permission, required):
            print(COLS[3] + f'required permission {required} GRANTED!' + COLS[0])
            return True
    print(COLS[2] + f'required permission {required} DENIED!' + COLS[0])
    return False

def check_permission(permission, required):
    print(f'checking permission {permission}({type(permission)}) against {required}({type(required)})')
    if type(required) is int:
        print(f'int against int: {permission == required}')
        return permission == required
    if type(required) is not list:
        print(f'ERROR --- required is not list! invalid required! ')
        return False
    print('required is list')
    for r in required:
        print(f'required[{r}]')
        if permission == r:
            print(COLS[3] + 'GRANTED' + COLS[0])
            return True
        print(COLS[4] + f'not yet...{r}' + COLS[0])
    print(COLS[2] + 'DENIED' + COLS[0])
    return False
