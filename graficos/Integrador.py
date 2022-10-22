import csv
import numpy

with open ('users.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=',')
    print("cabeçalho:" + str(arquivo_csv[0]))
    for i, linha in enumerate(arquivo_csv[1:]):
        print("resultado: " + str(linha))

def get_column_of_csv(filename, column):
    with open(filename) as stream:
        reader = csv.DictReader(stream)
        for row in reader:
            yield row[column]

cc = []

for i in range(5):
    lista = []
    for value in get_column_of_csv ('data/users.csv', f'c{i+1}'):
        lista.append(float(value))
    cc.append(lista)

    mediac1 = numpy.mean (lista)
    print (lista)
    print(mediac1)
