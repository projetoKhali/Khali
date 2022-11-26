# Importa a biblioteca que permite manipular arquivos .csv
import os
import csv
from Settings import *
# Definição do namespace, ao usar 'import ...', importará todos os metodos dentro do namespace

# Define se o CSVHandler deve printar no console
LOG = False

# Deleta o arquivo .csv caso exista e inicializa um novo com os campos apropriados
def initialize_csv (path:str):
    delete_csv(path)
    fields = PATH_FIELDS[path]
    save_file_csv(path, fields, [])

# Executa initialize_csv caso o arquivo .csv no caminho especificado não exista
def check_path(path, debug = None):
    if not os.path.exists(path + '.csv'):
        if LOG and debug:
            log(f"CSVHandler -- check_path (from {debug}): path doesn't exist")
        initialize_csv(path)

# Retorna a primeira linha encontrada que contenha o valor fornecido
def find_data_csv (path:str, value:str):
    # check_path(path, 'find_data_csv')

    # Tenta executar o próximo código
    try:
    
        # Abre o arquivo
        with open(path + '.csv', 'r') as file:

            # Lê as linhas do arquivo e salva na variavel 'lines'
            lines = file.readlines()

    # Em caso de falha
    except:
        log(COLS[2] + "CSVHandler.find_data: Erro ao ler arquivo" + COLS[0])
        return None

    # Pra cada linha carregada na variavel 'lines'
    for line in lines:

        # Se a linha atual contem a chave fornecida
        if value in line:

            # Retorna a linha formatada para dicionario
            return format_line_csv(lines[0].strip('\n').split(','), line)

    # Loop finalizado sem encontrar nenhum resultado
    return None


# Retorna a linha em que o id seja igual ao id especificado
def find_data_by_id_csv (path:str, id:str):
    # check_path(path, 'find_data_by_id_csv')

    # Tenta executar o próximo código
    try:
    
        # Abre o arquivo
        with open(path + '.csv', 'r') as file:

            # Lê as linhas do arquivo e salva na variavel 'lines'
            lines = file.readlines()

    # Em caso de falha
    except:
        log(COLS[2] + "CSVHandler.find_data_by_id: Erro ao ler arquivo" + COLS[0])
        return None

    # Pra cada linha carregada na variavel 'lines'
    for line in lines:

        line_values = line.strip('\n').split(',')

        try:
            line_key = line_values[0]
        except:
            continue

        # Se a linha atual contem a chave fornecida
        if line_key == str(id):

            # Retorna a linha formatada para dicionario
            return format_line_csv(lines[0].strip('\n').split(','), line)

    # Loop finalizado sem encontrar nenhum resultado
    return None


# Retorna uma lista contendo todas as linhas em que o campo 'field' possua o valor 'value'
def find_data_list_by_field_value_csv(path:str, field:str, value:str):
    # check_path(path, 'find_data_list_by_field_value_csv')

    # Tenta executar o próximo código
    try:
    
        # Abre o arquivo
        with open(path + '.csv', 'r') as file:

            # Lê as linhas do arquivo e salva na variavel 'lines'
            lines = file.readlines()

    # Em caso de falha
    except:
        log(COLS[2] + "CSVHandler.find_data_list_by_field_value_csv: Erro ao ler arquivo" + COLS[0])
        return None

    lista = []

    # Pra cada linha carregada na variavel 'lines'
    for line in lines:

        line_values = format_line_csv(lines[0].strip('\n').split(','), line)

        try:
            line_key = line_values[field]
        except:
            continue

        # Se a linha atual contem a chave fornecida
        if line_key == str(value):

            # Retorna a linha formatada para dicionario
            lista.append(format_line_csv(lines[0].strip('\n').split(','), line))

    # Loop finalizado sem encontrar nenhum resultado
    return lista


# Retorna uma lista contendo todas as linhas em que o campo 'field' possua qualquer um dos valores 'values'
def find_data_list_by_field_values_csv(path:str, field:str, values):

    # Tenta executar o próximo código
    try:
    
        # Abre o arquivo
        with open(path + '.csv', 'r') as file:

            # Lê as linhas do arquivo e salva na variavel 'lines'
            lines = file.readlines()

    # Em caso de falha
    except:
        log(COLS[2] + "CSVHandler.find_data_list_by_field_value_csv: Erro ao ler arquivo" + COLS[0])
        return None

    lista = []

    # Pra cada linha carregada na variavel 'lines'
    for line in lines:

        line_values = format_line_csv(lines[0].strip('\n').split(','), line)

        try:
            line_key = line_values[field]
        except:
            continue

        # Se a linha atual contem a chave fornecida
        if line_key in [str(v) for v in values]:

            # Retorna a linha formatada para dicionario
            lista.append(format_line_csv(lines[0].strip('\n').split(','), line))


    # Loop finalizado sem encontrar nenhum resultado
    return lista


# Retorna uma lista contendo todas as linhas em que o cada campo possua o valor especificado por chave no dicionario 'kvps' 
def find_data_list_by_fields_value_csv(path:str, kvps:dict):
    
    # Tenta executar o próximo código
    try:
    
        # Abre o arquivo
        with open(path + '.csv', 'r') as file:

            # Lê as linhas do arquivo e salva na variavel 'lines'
            lines = file.readlines()

    # Em caso de falha
    except:
        log(COLS[2] + "CSVHandler.find_data_list_by_field_value_csv: Erro ao ler arquivo" + COLS[0])
        return None

    lista = []

    # Pra cada linha carregada na variavel 'lines'
    for line in lines:

        # adquire os valores dessa linha
        line_values = format_line_csv(lines[0].strip('\n').split(','), line)

        # para cada valor especificado no dicionario
        for key in kvps:

            # Se o valor da chave key na linha corresponde ao valor da mesma chave no dicionario kvps
            if line_values[key] != str(kvps[key]):
                # sai do loop kvps
                break

        else:
            # adiciona a linha formatada para a lista de retorno
            lista.append(format_line_csv(lines[0].strip('\n').split(','), line))

    # Loop finalizado sem encontrar nenhum resultado
    return lista


# Formata uma linha de arquivo .csv em um dicionario python
def format_line_csv (fields, line:str):

    # Inicializa um dicionario vazio
    data = dict()

    # Converte a linha fornecida em uma lista de valores.
    # Cada valor corresponde ao texto separado por ',' na linha
    values = line.strip('\n').split(',')

    # Inicia um loop pra cada campo especificado, mantendo como referencia pra cada iteração:
    # 'i'     = o index atual no loop
    # 'field' = o campo referente ao index atual do loop
    for i, field in enumerate(fields):

        # Adiciona ao dicionario a chave field com o valor values[i]
        data.update({field: values[i]})

    # Retorna o dicionario gerado pelo loop
    return data


# Retorna todas as linhas do arquivo especificado
def load_all_csv (path:str):
    # Tenta executar o próximo código
    try:
    
        # Abre o arquivo
        with open(path + '.csv', 'r') as file:

            # Lê as linhas do arquivo e salva na variavel 'lines'
            lines = file.readlines()
            return [format_line_csv(lines[0].strip('\n').split(','), line) for line in lines[1:]]

    # Em caso de falha
    except:log(COLS[2] + "CSVHandler.find_data_list_by_field_value_csv: Erro ao ler arquivo" + COLS[0])

    return None


# Salva um banco de dados CSV
# Parametros:
# Path      =   O caminho até o arquivo ('pasta/pasta/pasta/nome_do_arquivo.csv')
# Fields    =   Os campos que estarão presentes na tabela { name, email, group, role }      <--- linha 0
# Rows      =   A lista de linhas a serem colocadas na tabela, cada linha é representada por uma lista própria
def save_file_csv (path:str, fields:list, rows:list):
    # check_path(path, 'save_file_csv')
    
    # Acompanhamento de processo pelo terminal
    log(COLS[6] + "CSVHandler.save_file_csv -- Iniciando processo de salvamento de um arquivo csv\t" + f"Caminho: {path}" + COLS[0])

    # Abre o arquivo localizado em 'path' em modo de escrita ('w') e o armazena na memoria como 'file'
    with open(path + '.csv', 'w', newline='') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o nome de cada campo na primeira linha
        writer.writerow(fields)

        # Para cada linha subsequente, coloca os valores dos campos correspondentes 
        writer.writerows(rows)

        log(COLS[3] + "CSVHandler.save_file_csv -- Arquivo .csv salvo com sucesso!" + COLS[0])


# Escreve a linha espeificada no arquivo .csv especificado
def add_line_csv (path:str, row:str):
    # check_path(path, 'add_line_csv')

    # Acompanhamento de processo pelo terminal
    log(COLS[6] + "CSVHandler.add_line: Iniciando processo de acrescentamento de um arquivo csv\t" + f"Caminho: {path}" + COLS[0])

    # Abre o arquivo localizado em 'path' em modo de acrescentação ('a') e o armazena na memoria como 'file'
    with open(path + '.csv', 'a', newline='') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o nome de cada campo na primeira linha
        writer.writerow(row)

        log(COLS[3] + "CSVHandler.add_line: Arquivo .csv acrescentado com sucesso!" + COLS[0])


# Escreve uma linha de informação "Unica" com o chave 'id' e valor especificado 'row'
def add_unique_csv (path:str, id:int, row):
    # check_path(path, 'add_unique_csv')

    # Acompanhamento de processo pelo terminal
    log(COLS[6] + "CSVHandler.add_unique_csv: Iniciando processo de armazenamento de informação identificada por id" + COLS[0])

    if id < 0:
        if log: print(COLS[2] + f"CSVHandler.add_unique_csv -- Erro: O id fornecido é invalido" + COLS[0]) 

    # Abre o arquivo localizado em 'path' em modo de acrescentação ('a') e o armazena na memoria como 'file'
    with open(path + '.csv', 'a', newline='') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o id como primeiro item da linha (index 0)
        row.insert(0, str(id))

        # Insere o nome de cada campo na primeira linha
        writer.writerow(row)

        log(COLS[3] + "CSVHandler.add_unique_csv: Arquivo .csv acrescentado com sucesso!" + COLS[0])


# Escreve uma linha de informação "Unica" o valor especificado 'row'
# A chave 'id' será definida como o proximo valor disponivel
def add_unique_csv_autoid (path:str, row):
    check_path(path, 'add_unique_csv_autoid')

    # Acompanhamento de processo pelo terminal
    log(COLS[6] + "CSVHandler.add_unique_csv_autoid: Iniciando processo de armazenamento de informação identificada utilizando associação automatica de id" + COLS[0])

    # Verifica se o caminho existe, se não: inicia o arquivo com o texto a seguir na primeira linha
    if not os.path.exists(path + '.csv'):
        add_line_csv(path, ["id","data"])

    # Declara uma variavel para armazenar o maior id encontrado no arquivo
    max_id = -1

    # Abre o arquivo especificado
    with open(path + '.csv', 'r') as file:

        # Verifica cada linha do arquivo
        for line in file.readlines():

            # Tenta executaro o proximo comando
            try:
                
                # declara a variavel 'line_id' e atribui o valor como a conversão do primeiro campo na linha para numero
                # strip:  remove '\n' da linha 
                # split:  converte a linha em uma lista ao separar a linha a cada ','
                # [0]:    acessa o primeiro item da lista, onde estará o id
                # int(x): converte o valor adquirido em int, x sendo o resultado dos passos anteriores
                line_id = int(line.strip('\n').split(',')[0])

            # Em caso de erro durante o processo:
            except:
                continue

            # Apos adquirir o id da linha atual, compare-o com o atual "maior id"
            if line_id > max_id:

                # id é maior que 'maior id', id se torna o novo 'maior id'
                max_id = line_id

    # Define o id da linha a ser adicionada como sendo o maior id encontrado no loop + 1
    id = max_id + 1

    if id < 0:
        if log: print(COLS[2] + f"CSVHandler.add_unique_csv_autoid -- Erro: O id invalido autogerado" + COLS[0]) 

    # printa para acompanhamento de processo
    log(COLS[7] + "CSVHandler.add_unique_csv_autoid: id definido com sucesso: " + str(id))

    # Chama a versão da função que inclui especificação por id para continuar o processo
    add_unique_csv(path, id, row)

    # Retorna o id escolhido como resultado dessa função
    return id


# Carrega o arquivo especificado e retorna o conteudo da linha de numero 'line' 
def read_line_csv (path:str, line:int):

    # Tenta executar o proximo código 
    try:

        with open(path + '.csv', 'r') as file:

            # Converte os dados em uma lista de linhas e retorna o item 'line' da lista 
            return file.readlines()[line]

    # Em caso de erro (mais provavel: numero da linha maior ou igual o numero total de linhas do arquivo / OutOfBouds)
    except:
        log(COLS[2] + f"Erro ao ler a linha {line} no arquivo de caminho {path}" + COLS[0])


# Retorna o numero de linhas do arquivo especificado
def line_count_csv (path:str):

    # Tenta executar o proximo codigo
    try:

        # Abre o arquivo genericamente
        with open(path + '.csv', 'r') as file:

            # Retorna o comprimento da lista retornada por file.readlines()
            return len(file.readlines())

    # falha
    except:
        log(COLS[2] + "CSVHandler.line_len: arquivo não encontrado" + COLS[0])

    return 0


# Remove a linha do id especificado
def delete_line_csv (path:str, id:int):

    # abre e lê arquivo csv
    with open(path + '.csv', 'r') as file: lines = file.readlines()

    new_lines = []

    for line in lines[1:]:
        line_data = format_line_csv(PATH_FIELDS[path], line)
        if line_data['id'] == str(id): continue
        new_lines.append([field[1] for field in line_data.items()])
    save_file_csv(path, PATH_FIELDS[path], new_lines)


# Edita a linha de id especificado 
def edit_line_csv (path:str, id:int, kvps:dict):

    # abre e lê arquivo csv
    with open(path + '.csv', 'r') as file: lines = file.readlines()

    for line_index, line in enumerate(lines[1:]):
        line_data = format_line_csv(PATH_FIELDS[path], line)
        if line_data['id'] == str(id):
            for field in kvps:
                line_data[field] = kvps[field]
        line_list = [field[1] for field in line_data.items()]
        lines[line_index + 1] = line_list
    save_file_csv(path, PATH_FIELDS[path], lines[1:])


# Deleta um arquivo .csv do caminho especificado
def delete_csv (path:str):
    import os
    if os.path.isfile(path + '.csv'):
        os.remove(path + '.csv')


# cutom console
def log (message):
    if not LOG: return
    print(message)