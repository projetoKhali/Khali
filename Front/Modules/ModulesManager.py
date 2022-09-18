from . import cadastro_adm, lista_usuarios

MODULES = [
    cadastro_adm,
    lista_usuarios,
]

def get_modules():
    from Users.Authentication import CURRENT_USER
    from Users.Roles import Role 
    role = Role.get_role(int(CURRENT_USER.role_id))
    allowed_modules = []
    for module in MODULES:
        if check_permissions(role.permissions, module):
            allowed_modules.append(module)
    return allowed_modules

def check_permissions(permissions, target_module):
    p_fulfilled = 0
    for permission in permissions:
        for required in target_module.REQUIRED_PERMISSIONS:
            if not check_permission(permission, required):
                break
            p_fulfilled +=1
    len_required = len(target_module.REQUIRED_PERMISSIONS)
    print(f'check_permissions for module {target_module.MODULE_NAME}: {p_fulfilled} of {len_required} fulfilled ')
    return p_fulfilled == len_required

def check_permission(permission, required):
    print(f'checking permission {permission} against {required}')
    if type(required) is int:
        return permission == required
    if type(required) is not list:
        return False
    for r in required:
        if permission == r:
            return True
    return False
