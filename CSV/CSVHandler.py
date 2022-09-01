
# Importa a biblioteca que permite manipular arquivos .csv
from array import array
import csv

# Definição do namespace, ao usar 'import ...', importará todos os metodos dentro do namespace

# Salva um banco de dados CSV
# Parametros:
# Path      =   O caminho até o arquivo ('pasta/pasta/pasta/nome_do_arquivo.csv')
# Fields    =   Os campos que estarão presentes na tabela { name, email, group, role }      <--- linha 0
# Rows      =   A lista de arrays em que cada array representa uma linha na tabela {[linha1], [linha2], [linha3]}
def save_csv(path:str, fields:array, rows:array):
    
    # Acompanhamento de processo pelo terminal
    print("Iniciando processo de salvamento de um arquivo csv\n" + f"Caminho: {path}")

    # Abre o arquivo localizado em 'path' em modo de escrita ('w') e o armazena na memoria como 'file'
    with open(path + '.csv', 'w') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o nome de cada campo na primeira linha
        writer.writerow(fields)

        # Para cada linha subsequente, coloca os valores dos campos correspondentes 
        writer.writerows(rows)

        print("Arquivo .csv salvo com sucesso!")


# Carrega um arquivo csv e retorna os dados adquiridos pela leitura
def load_csv(path:str):

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
def add_line_csv (path:str, row:str):

    # Acompanhamento de processo pelo terminal
    print("Iniciando processo de acrescentamento de um arquivo csv\n" + f"Caminho: {path}")

    # Abre o arquivo localizado em 'path' em modo de acrescentação ('a') e o armazena na memoria como 'file'
    with open(path + '.csv', 'a') as file:
        
        # Inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # Insere o nome de cada campo na primeira linha
        writer.writerow(row)

        print("Arquivo .csv acrescentado com sucesso!")


# Carrega o arquivo especificado e retorna o conteudo da linha de numero 'line' 
def read_line_csv (path:str, line:int):

    # Carrega o arquivo no caminho 'path'
    reader = csv.reader(path + '.csv')

    # Tenta executar o proximo código 
    try:

        # Converte os dados em uma lista de linhas e retorna o item 'line' da lista 
        return list(reader)[line]

    # Em caso de erro (mais provavel: numero da linha maior ou igual o numero total de linhas do arquivo / OutOfBouds)
    except:
        print(f"Erro ao ler a linha {line} no arquivo de caminho {path}")

