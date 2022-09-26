# Importa a biblioteca que permite manipular arquivos .csv
import os
from array import array
import csv
from Settings import *
# Definição do namespace, ao usar 'import ...', importará todos os metodos dentro do namespace

def initialize_csv (path:str):
    delete_csv(path)
    fields = get_path_fields(path)
    save_file_csv(path, fields, [])

def check_path(path, debug):
    if not os.path.exists(path + '.csv'):
        print(f"{debug}: path doesn't exist")
        initialize_csv(path)

# Retorna o conteudo da linha onde estiver localizada a informação fornecida
def find_data_csv (path:str, key:str):
    # check_path(path, 'find_data_csv')

    # Tenta executar o próximo código
    try:
    
        # Abre o arquivo
        with open(path + '.csv', 'r') as file:

            # Lê as linhas do arquivo e salva na variavel 'lines'
            lines = file.readlines()

    # Em caso de falha
    except:
        print(COLS[2] + "CSVHandler.find_data: Erro ao ler arquivo" + COLS[0])
        return None

    # Pra cada linha carregada na variavel 'lines'
    for line in lines:

        # Se a linha atual contem a chave fornecida
        if key in line:

            # Retorna a linha formatada para dicionario
            return format_line_csv(lines[0].strip('\n').split(','), line)

    # Loop finalizado sem encontrar nenhum resultado
    return None

# Retorna o conteudo da linha onde estiver localizada a informação fornecida
def find_data_by_id_csv (path:str, key:str):
    # check_path(path, 'find_data_by_id_csv')

    # Tenta executar o próximo código
    try:
    
        # Abre o arquivo
        with open(path + '.csv', 'r') as file:

            # Lê as linhas do arquivo e salva na variavel 'lines'
            lines = file.readlines()

    # Em caso de falha
    except:
        print(COLS[2] + "CSVHandler.find_data: Erro ao ler arquivo" + COLS[0])
        return None

    # Pra cada linha carregada na variavel 'lines'
    for line in lines:

        line_values = line.strip('\n').split(',')

        try:
            line_key = line_values[0]
        except:
            continue

        # Se a linha atual contem a chave fornecida
        if line_key == str(key):

            # Retorna a linha formatada para dicionario
            return format_line_csv(lines[0].strip('\n').split(','), line)

    # Loop finalizado sem encontrar nenhum resultado
    return None

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
        print(COLS[2] + "CSVHandler.find_data: Erro ao ler arquivo" + COLS[0])
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

def get_path_fields (path:str):
    for path_fields in PATH_FIELDS:
        if path_fields['path'] == path:
            return path_fields['fields']
    return ("id","data")

# Salva um banco de dados CSV
# Parametros:
# Path      =   O caminho até o arquivo ('pasta/pasta/pasta/nome_do_arquivo.csv')
# Fields    =   Os campos que estarão presentes na tabela { name, email, group, role }      <--- linha 0
# Rows      =   A lista de arrays em que cada array representa uma linha na tabela {[linha1], [linha2], [linha3]}
def save_file_csv (path:str, fields:array, rows:array):
    # check_path(path, 'save_file_csv')
    
    # Acompanhamento de processo pelo terminal
    print(COLS[6] + "Iniciando processo de salvamento de um arquivo csv\t" + f"Caminho: {path}" + COLS[0])

    # Abre o arquivo localizado em 'path' em modo de escrita ('w') e o armazena na memoria como 'file'
    with open(path + '.csv', 'w', newline='') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o nome de cada campo na primeira linha
        writer.writerow(fields)

        # Para cada linha subsequente, coloca os valores dos campos correspondentes 
        writer.writerows(rows)

        print(COLS[3] + "Arquivo .csv salvo com sucesso!" + COLS[0])

# Escreve a linha espeificada no arquivo .csv especificado
def add_line_csv (path:str, row:str):
    # check_path(path, 'add_line_csv')

    # Acompanhamento de processo pelo terminal
    print(COLS[6] + "CSVHandler.add_line: Iniciando processo de acrescentamento de um arquivo csv\t" + f"Caminho: {path}" + COLS[0])

    # Abre o arquivo localizado em 'path' em modo de acrescentação ('a') e o armazena na memoria como 'file'
    with open(path + '.csv', 'a', newline='') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o nome de cada campo na primeira linha
        writer.writerow(row)

        print(COLS[3] + "CSVHandler.add_line: Arquivo .csv acrescentado com sucesso!" + COLS[0])

# Escreve uma linha de informação "Unica" com o chave 'id' e valor especificado 'row'
def add_unique_csv (path:str, id:int, row):
    # check_path(path, 'add_unique_csv')

    # Acompanhamento de processo pelo terminal
    print(COLS[6] + "CSVHandler.add_unique_csv: Iniciando processo de armazenamento de informação identificada por id" + COLS[0])

    if id < 0:
        print(COLS[2] + f"CSVHandler.add_unique_csv -- Erro: O id fornecido é invalido" + COLS[0]) 

    # Abre o arquivo localizado em 'path' em modo de acrescentação ('a') e o armazena na memoria como 'file'
    with open(path + '.csv', 'a', newline='') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o id como primeiro item da linha (index 0)
        row.insert(0, str(id))

        # Insere o nome de cada campo na primeira linha
        writer.writerow(row)

        print(COLS[3] + "CSVHandler.add_unique_csv: Arquivo .csv acrescentado com sucesso!" + COLS[0])

# Escreve uma linha de informação "Unica" o valor especificado 'row'
# A chave 'id' será definida como o proximo valor disponivel
def add_unique_csv_autoid (path:str, row):
    check_path(path, 'add_unique_csv_autoid')

    # Acompanhamento de processo pelo terminal
    print(COLS[6] + "CSVHandler.add_unique_csv_autoid: Iniciando processo de armazenamento de informação identificada utilizando associação automatica de id" + COLS[0])

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
        print(COLS[2] + f"CSVHandler.add_unique_csv_autoid -- Erro: O id invalido autogerado" + COLS[0]) 

    # printa para acompanhamento de processo
    print(COLS[7] + "CSVHandler.add_unique_csv_autoid: id definido com sucesso: " + str(id))

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
        print(COLS[2] + f"Erro ao ler a linha {line} no arquivo de caminho {path}" + COLS[0])

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
        print(COLS[2] + "CSVHandler.line_len: arquivo não encontrado" + COLS[0])

    return 0

def delete_csv (path:str):
    import os
    if os.path.isfile(path + '.csv'):
        os.remove(path + '.csv')
