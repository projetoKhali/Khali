from CSV.CSVHandler import *
from Settings import GROUPS_PATH

# Define a classe Group para facilitar a utilização no código
class Group:
    def __init__(self, id, name, leader_id, client_id):
        self.id = id
        self.name = name
        self.leader_id = leader_id
        self.client_id = client_id
    def __str__(self):
        return f'Group[id: {self.id}, name: {self.name}, leader_id: {self.leader_id}, client_id: {self.client_id}]'


# Converte dicionario em rating
def to_group(group_dict):
    return Group(
        int(group_dict['id']),
        group_dict['name'],
        int(group_dict['leader_id']),
        int(group_dict['client_id']),
    ) # if group_dict is not None else None

# Cria e armazena um novo Grupo com o nome fornecido
def create_group (name:str, leader_id, client_id):
    return add_unique_csv_autoid(GROUPS_PATH, [name, leader_id, client_id])

# Verifica se um Grupo com o id forneido existe armazenado no banco de dados
def exists_group (id:int):
    if id is None:
        return True
    return get_group(id) is not None 

# retorna o nome do Grupo que corresponde ao id especificado 
def get_group_name (id:int):
    return None if id == '' or id is None else get_group(id).name 

# retorna o Grupo que corresponde ao id especificado 
def get_group (id:int):
    return None if id == '' or id is None else to_group(find_data_by_id_csv(GROUPS_PATH, int(id)))

# Retorna todos os Gruposs
def get_groups ():
    return [to_group(x) for x in load_all_csv(GROUPS_PATH)]

# Retorna todos o Grupos em que o usuário de id especificado posssui a função de Lider
def get_groups_of_leader (id:int):
    return None if id == '' or id is None else [to_group(x) for x in find_data_list_by_field_value_csv(GROUPS_PATH, 'leader_id', int(id))]


def edit_group(id, name = 'IGNORE', leader_id = 'IGNORE', client_id = 'IGNORE'):
    kvps = {}
    if name != 'IGNORE': kvps.update({'name': name})
    if leader_id != 'IGNORE': kvps.update({'leader_id': leader_id})
    if client_id != 'IGNORE': kvps.update({'client_id': client_id})
    return edit_line_csv(GROUPS_PATH, id, kvps)


def delete_group(id):
    delete_line_csv(GROUPS_PATH, id)