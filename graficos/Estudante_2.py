# Importando as libs
import numpy as np
import  matplotlib.pyplot as  plt 
# Aqui eu inlcui as listas com as médias das notas em casa críterio avaliativo
sprint1 = [2,3,2,4,5]
sprint2 = [3,4,2,5,4]
sprint3 = [4,4,3,4,3]
sprint4 = [4,5,4,5,4]

#Define a expessura da barra
barWidth = 0.2
#Defini a ampliação do grafico quando você roda
plt.figure(figsize=(10,5))

#Aqui eu estou definindo a posição de cada barra no grafico
r1 = np.arange(len(sprint1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

#Aqui eu contruo a barra
plt.bar(r1, sprint1, color='orange', width=barWidth, label="Sprint 1")
plt.bar(r2, sprint2, color='green', width=barWidth, label="Sprint 2")
plt.bar(r3, sprint3, color='blue', width=barWidth, label="Sprint 3")
plt.bar(r4, sprint4, color='red', width=barWidth, label="Sprint 4")

#contrução das legndas
plt.xlabel('notas')
plt.xticks( [r + barWidth for r in range(len(sprint1))],['TG','PO','KE', 'PT', 'QU'])
plt.ylabel("Criterios")
plt.title('Desempenho ao decorrer das Sprints')
plt.legend()

plt.show()