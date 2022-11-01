# Importando as libs
import numpy as np
import  matplotlib.pyplot as  plt 

from Dashboards import estudantes_1
estudantes_1()
exit()

# Aqui eu inlcui as listas com as médias das notas em casa críterio avaliativo

criterios = [
    [2,3,4,4], 
    [3,4,4,5], 
    [2,2,3,4], 
    [4,5,4,5], 
    [5,4,3,4]
]

gc = [ 
    [2,4,5,4,5,3,4,3,2,1,4,5,3,2,1,4,5,4,3,5,2,4,5,4],
    [2,1,4,5,3,3,4,3,2,1,3,2,1,4,2,1,4,5,3,2,1,4,5,4],
    [5,3,4,3,2,1,4,5,3,2,1,4,5,4,1,3,2,1,4,2,1,4,5,3],
    [4,5,4,5,3,4,3,2,1,4,5,3,2,1,4,4,2,1,4,2,1,4,5,3],
    [3,4,3,2,1,3,2,1,4,2,1,4,5,3,2,3,4,2,1,4,5,3,2,3]
]

minha_media = []
media_time = []

# Lista com a média em cada críterio avaliativo
for i in range(5):
    minha_media.append(np.mean(criterios[i]))
    media_time.append(np.mean(gc[i]))

#Define a expessura da barra
barWidth = 0.2
#Defini a ampliação do grafico quando você roda
plt.figure(figsize=(10,5))

#Aqui eu estou definindo a posição de cada barra no grafico
r1 = np.arange(5)
r2 = [x + barWidth for x in r1]

#Aqui eu contruo a barra
plt.bar(r1, minha_media, color='orange', width=barWidth, label=" ")
plt.bar(r2, media_time, color='green', width=barWidth, label="")

plt.xlabel('Críterio avaliativo')
plt.xticks( [r + barWidth for r in range(len(minha_media))],['TG','PO','KE', 'PT', 'QU'])
plt.ylabel("Notas")
plt.title('Seu desempenho em comparativo ao seu time')

plt.legend()
plt.show()

exit()
#_____________________________________________________

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