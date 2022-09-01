
# importa a biblioteca que permite manipular arquivos .csv
import csv

# definição do namespace, ao usar 'import ...', importará todos os metodos dentro do namespace

# salva um banco de dados CSV
# parametros:
# path      =   o caminho até o arquivo ('pasta/pasta/pasta/nome_do_arquivo.csv')
# fields    =   os campos que estarão presentes na tabela { name, email, group, role }      <--- linha 0
# rows      =   a lista de arrays em que cada array representa uma linha na tabela {[linha1], [linha2], [linha3]}
def csvsave(path, fields, rows):
    
    print("asuhjasbnckjabsjchakjscbk")

    # abre o arquivo localizado em 'path' em modo de escrita ('w') e o armazena na memoria como 'file'
    with open(str(path) + '.csv', 'w') as file:

        print(path)
        print(file)
        
        # inicializa a classe writer da biblioteca padrão 'csv' utilizando 'file' como parametro
        writer = csv.writer(file)

        # insere o nome de cada campo na primeira linha
        writer.writerow(fields)

        # para cada linha subsequente, coloca os valores dos campos correspondentes 
        writer.writerows(rows)

# carrega um arquivo csv e retorna os dados adquiridos pela leitura
def csvload(path):

    # tenta executar o próximo código
    try:

        # carrega o arquivo na variável 'reader'
        reader = csv.reader(path + '.csv')

    # em caso de erro durante o processo de leitura do arquivo (Ex.: path inválido), printa 
    except:
        print("Erro ao carregar arquivo .csv!")
        return #i nterrompe a execução do método 'load'

    # retorna o texto carregado
    print(reader)
    return reader