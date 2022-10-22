import csv
import pandas
from os import name
from matplotlib.pyplot import get
import numpy

with open ('users.csv','r') as arquivo:
    arquivo_csv = csv.reader(arquivo,delimiter=',')
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("cabeçalho:" + str(linha))
        else:
            print("resultado: " + str(linha))
def get_column_of_csv(filename, column):
    with open(filename) as stream:
     reader = csv.DictReader(stream)
     for row in reader:
      yield row[column]
cc1 = []
cc2 = []
cc3 = []
cc4 = []
cc5 = []

for name1 in get_column_of_csv ('users.csv','c1'):
    cc1.append(float(name1))
for name2 in get_column_of_csv('users.csv', 'c2'):
    cc2.append(float(name2))
for name3 in get_column_of_csv('users.csv', 'c3'):
    cc3.append(float(name3))
for name4 in get_column_of_csv('users.csv', 'c4'):
    cc4.append(float(name4))
for name5 in get_column_of_csv('users.csv', 'c5'):
    cc5.append(float(name5))


 
mediac1 = numpy.mean (cc1)
mediac2 = numpy.mean (cc2)  
mediac3 = numpy.mean (cc3)
mediac4 = numpy.mean (cc4)
mediac5 = numpy.mean (cc5)

print (cc1)
print (cc2)
print (cc3)
print (cc4)
print (cc5)

print(mediac1)
print(mediac2)
print(mediac3)
print(mediac4)
print(mediac5)