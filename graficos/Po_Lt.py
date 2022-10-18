import numpy as np
import  matplotlib.pyplot as  plt 

ti1id1 = [4,3,5,4,2]
ti1id2 = [5,4,3,4,6]
ti1id3 = [4,2,4,5,4]
ti1id4 = [2,3,4,5,3]
ti2id5 = [2,3,4,4,5]
ti2id6 = [2,5,3,4,2]
ti2id7 = [5,3,4,5,2]
ti2id8 = [5,3,4,5,3]


#Define a expessura da barra
barWidth = 0.2
#Defini a ampliação do grafico
plt.figure(figsize=(10,5))

#Aqui eu estou definindo a posição de cada barra no grafico
r1 = np.arange(len(ti1id1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

#Aqui eu contruo a barra
plt.bar(r1, ti1id1, color='orange', width=barWidth, label="Rodrigo")
plt.bar(r2, ti1id2, color='green', width=barWidth, label="rogerio")
plt.bar(r3, ti1id3, color='blue', width=barWidth, label="marta")
plt.bar(r4, ti1id4, color='pink', width=barWidth, label="Cleitinho")
plt.xlabel('Críterio avaliativo')
plt.xticks( [r + barWidth for r in range(len(ti1id1))],['TG','PO','KE', 'PT', 'QU'])
plt.ylabel("Notas")
plt.title('desempenho individual')
plt.legend()
plt.show()

r1 = np.arange(len(ti2id5))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

plt.bar(r1, ti2id5, color='orange', width=barWidth, label="Valeria")
plt.bar(r2, ti2id6, color='yellow', width=barWidth, label="Simone")
plt.bar(r3, ti2id7, color='red', width=barWidth, label="Vitor")
plt.bar(r4, ti2id8, color='green', width=barWidth, label="lula")

plt.xlabel('Críterio avaliativo')
plt.xticks( [r + barWidth for r in range(len(ti2id5))],['TG','PO','KE', 'PT', 'QU'])
plt.ylabel("Notas")
plt.title('Seu desempenho em comparativo ao seu time')

plt.legend()
plt.show()