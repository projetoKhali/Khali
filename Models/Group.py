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
    )

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

def get_group_name_especifc(leader_id):
        return None if leader_id == '' or leader_id is None else to_group(find_data_by_id_csv(GROUPS_PATH, int(leader_id)))