from Settings import GROUPS_PATH

# Cria e armazena um novo Grupo com o nome fornecido
def create_group (name:str):
    from CSV.CSVHandler import add_unique_csv_autoid
    return add_unique_csv_autoid(GROUPS_PATH, [name])

# Verifica se um Grupo com o id forneido existe armazenado no banco de dados
def exists_group (id:int):
    if id is None:
        return True
    from CSV.CSVHandler import find_data_by_id_csv
    return find_data_by_id_csv(GROUPS_PATH, id) is not None 

# retorna o nome do Grupo que corresponde ao id especificado 
def get_group_name (id:int):
    from CSV.CSVHandler import find_data_by_id_csv
    return find_data_by_id_csv(GROUPS_PATH, id)['name'] 
