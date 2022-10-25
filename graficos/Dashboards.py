import  matplotlib.pyplot as  plt 


# Define a expessura da barra
barWidth = .2 

# Gera um grafico multi barra
def multi_bar (title, names, y_label, values, x_label, x_ticks, colors):

    plt.rcParams['toolbar'] = 'None'

    # Define a ampliação do grafico
    # plt.figure(figsize = (10, 5))

    for i, value in enumerate(values):

        # Aqui eu construo a barra
        bar = [j + (i * barWidth) for j in range(len(x_ticks))]
        plt.bar(bar, value, color=colors[i], width=barWidth, label=names[i])

    plt.title(title)

    plt.xlabel(x_label)
    plt.xticks([r + barWidth for r in range(len(x_ticks))], x_ticks)

    plt.ylabel(y_label)

    plt.legend()

    plt.show()











def PO():
    multi_bar(
        'desempenho individual',
        ['Rodrigo', 'rogerio', 'marta', 'Cleitinho'],
        'Notas',
        [
            [4, 3, 5, 4, 2],
            [5, 4, 3, 4, 6],
            [4, 2, 4, 5, 4],
            [2, 3, 4, 5, 3]
        ],
        'Críterio avaliativo',
        ['TG', 'PO', 'KE', 'PT', 'QU'],
        ['orange', 'green', 'blue', 'pink']
    )







def LT ():
    multi_bar(
        'Seu desempenho em comparativo ao seu time',
        ['Valeria', 'Simone', 'Vitor', 'lula'],
        'Notas',
        [
            [2, 3, 4, 4, 5],
            [2, 5, 3, 4, 2],
            [5, 3, 4, 5, 2],
            [5, 3, 4, 5, 3]
        ],
        'Críterio avaliativo',
        ['TG', 'PO', 'KE', 'PT', 'QU'],
        ['orange', 'yellow', 'red', 'green']
    )




def estudantes ():
    multi_bar(
        'Seu desempenho em comparativo ao seu time',
        ['Sua média', 'Média dos seu time'],
        'Criterios',
        [
            [2, 3, 2, 4, 5],
            [3, 4, 2, 5, 4]
        ],
        None,
        ['TG', 'PO', 'KE', 'PT', 'QU'],
        ['orange', 'green']
    )





def Estudante_2 ():
    multi_bar(
        'Desempenho ao decorrer das Sprints',
        ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4'],
        'Criterios',
        [
            [2, 3, 2, 4, 5],
            [3, 4, 2, 5, 4],
            [4, 4, 3, 4, 3],
            [4, 5, 4, 5, 4]
        ],
        None,
        ['TG', 'PO', 'KE', 'PT', 'QU'],
        ['orange', 'green', 'blue', 'red']
    )


