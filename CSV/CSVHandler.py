
# Importa a biblioteca que permite manipular arquivos .csv
from pathlib import Path
from array import array
import csv

# Definição do namespace, ao usar 'import ...', importará todos os metodos dentro do namespace

# Retorna o conteudo da linha onde estiver localizada a informação fornecida
def find_data (path:str, key:str):

    # Tenta executar o próximo código
    try:
    
        # Abre o arquivo; Lê as linhas do arquivo e salva na variavel 'lines'
        lines = open(path + '.csv', 'r').readlines()

    # Em caso de falha
    except:
        print("CSVHandler.find_data: Erro ao ler arquivo")
        return None

    # Pra cada linha carregada na variavel 'lines'
    for line in lines:

        # Se a linha atual contem a chave fornecida
        if key in line:

            # Retorna a linha formatada para dicionario
            return format_line(lines[0].strip('\n').split(','), line)

    # Loop finalizado sem encontrar nenhum resultado
    return None


# Formata uma linha de arquivo .csv em um dicionario python
def format_line(fields, line:str):

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


# Salva um banco de dados CSV
# Parametros:
# Path      =   O caminho até o arquivo ('pasta/pasta/pasta/nome_do_arquivo.csv')
# Fields    =   Os campos que estarão presentes na tabela { name, email, group, role }      <--- linha 0
# Rows      =   A lista de arrays em que cada array representa uma linha na tabela {[linha1], [linha2], [linha3]}
def save_file(path:str, fields:array, rows:array):
    
    Path(path).mkdir(parents=True, exist_ok=True)

    # Acompanhamento de processo pelo terminal
    print("Iniciando processo de salvamento de um arquivo csv\n" + f"Caminho: {path}")

    # Abre o arquivo localizado em 'path' em modo de escrita ('w') e o armazena na memoria como 'file'
    with open(path + '.csv', 'w', newline='') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o nome de cada campo na primeira linha
        writer.writerow(fields)

        # Para cada linha subsequente, coloca os valores dos campos correspondentes 
        writer.writerows(rows)

        print("Arquivo .csv salvo com sucesso!")


# Carrega um arquivo csv e retorna os dados adquiridos pela leitura
def load_file(path:str):

    # Acompanhamento de processo pelo terminal
    print("Iniciando processo de carregamento de um arquivo csv\n" + f"Caminho: {path}")

    # Tenta executar o próximo código
    try:

        # Carrega o arquivo na variável 'reader'
        reader = csv.reader(path + '.csv')

    # Em caso de erro durante o processo de leitura do arquivo (Ex.: path inválido): 
    except:

        # Printa o Erro no console
        print("Erro ao carregar arquivo .csv!")
        return #i nterrompe a execução do método 'load'

    print(f"Arquivo carregado com sucesso!\n{reader}")

    # Retorna o texto carregado
    return reader


# Escreve a linha espeificada no arquivo .csv especificado
def add_line (path:str, row:str):

    # Acompanhamento de processo pelo terminal
    print("Iniciando processo de acrescentamento de um arquivo csv\n" + f"Caminho: {path}")

    # Abre o arquivo localizado em 'path' em modo de acrescentação ('a') e o armazena na memoria como 'file'
    with open(path + '.csv', 'a') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o nome de cada campo na primeira linha
        writer.writerow(row)

        print("Arquivo .csv acrescentado com sucesso!")

# Escreve uma linha de informação "Unica" com o id e valor especificado
def add_unique_data (path:str, id:int, row:str):
    pass

# Carrega o arquivo especificado e retorna o conteudo da linha de numero 'line' 
def read_line (path:str, line:int):

    # Tenta executar o proximo código 
    try:

        with open(path + '.csv', 'r') as file:

            # Converte os dados em uma lista de linhas e retorna o item 'line' da lista 
            return file.readlines()[line]

    # Em caso de erro (mais provavel: numero da linha maior ou igual o numero total de linhas do arquivo / OutOfBouds)
    except:
        print(f"Erro ao ler a linha {line} no arquivo de caminho {path}")


# Retorna o numero de linhas do arquivo especificado
def line_len (path:str):

    # Tenta executar o proximo codigo
    try:

        # Abre o arquivo genericamente
        with open(path + '.csv', 'r') as file:

            # Retorna o comprimento da lista retornada por file.readlines()
            return len(file.readlines())

    # falha
    except:
        print("CSVHandler.line_len: arquivo não encontrado")

    return 0
