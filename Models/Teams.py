from Settings import TEAMS_PATH

# Cria e armazena um novo Time com o nome fornecido
def create_team (name:str, group:int):
    from CSV.CSVHandler import add_unique_csv_autoid
    return add_unique_csv_autoid(TEAMS_PATH, [group, name])

# Verifica se um Time com o id forneido existe armazenado no banco de dados
def exists_team (id:int):
    if id is None:
        return True
    from CSV.CSVHandler import find_data_by_id_csv
    return find_data_by_id_csv(TEAMS_PATH, id) is not None 

def get_team_id (name:str):
    from CSV.CSVHandler import find_data_list_by_field_value_csv
    for team in find_data_list_by_field_value_csv(TEAMS_PATH, 'name', name):
        if team['name'] == name:
            return team['id']
    return None

# retorna o nome do Time que corresponde ao id especificado 
def get_team_name (id:int):
    from CSV.CSVHandler import find_data_by_id_csv
    return find_data_by_id_csv(TEAMS_PATH, id)['name'] 

