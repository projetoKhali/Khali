import  matplotlib.pyplot as  plt 

# Gera um grafico multi barra
def multi_bar (title, names, y_label, matrix, x_label, x_ticks, colors):

    # Esconde a barra de comandos do matplotlib
    plt.rcParams['toolbar'] = 'None'

    # Define a ampliação do grafico
    # plt.figure(figsize = (10, 5))
    
    # Define a largura de cada barra individual sendo 1 dividido pela quantidade de listas da matriz
    # somado por um valor constante de espaçamento entre cada x_tick
    bar_width = 1. / (len(matrix) + 1.75)

    # Para cada lista na matriz
    for i, lst in enumerate(matrix):

        # Define a posição da barra. Indice da barra * espaçamento definido pela quantidade de barras por x_tick
        offset = (i * bar_width) 

        # move todas as barras para esquerda em (tamanho total da soma das barras / 2)
        offset -= bar_width * int(len(matrix) / 2)

        # caso o numero de barras seja par, move o metade do tamanho de UMA barra para a direita
        if len(matrix) % 2 == 0: offset += bar_width / 2

        # define a posição de cada barra da lista de indice 'i'
        positions = [j + offset for j in range(len(x_ticks))]
        
        # Cria um grafico de barras para cada item da lista 'lst'  
        plt.bar(positions, lst, color=colors[i], width=bar_width, label=names[i])

    # Adiciona o título
    plt.title(title)

    # Adiciona a label e os marcadores x
    plt.xlabel(x_label)
    plt.xticks([r for r in range(len(x_ticks))], x_ticks)

    # Adiciona a label y
    plt.ylabel(y_label)

    # Adiciona a legenda representando cada lista da matriz
    plt.legend()

    # Renderiza o grafico
    plt.show()


# Gera um grafico de linha
def line (title, names, y_label, values, x_label, x_ticks, colors):
    plt.rcParams['toolbar'] = 'None'

    # Define a ampliação do grafico
    # plt.figure(figsize = (10, 5))
    barWidth = .2 

    for i, value in enumerate(values):

        # Aqui eu construo a barra
        positions = [j + barWidth for j in range(len(x_ticks))]
        plt.plot(positions, value, color=colors[i], label=names[i])

    plt.title(title)

    plt.xlabel(x_label)
    plt.xticks([r + barWidth for r in range(len(x_ticks))], x_ticks)

    plt.ylabel(y_label)

    plt.legend()

    plt.show()


def teste():
    names = []
    values = []

    for i in range(10):

        names.append(f'teste{i}')
        values.append([3, 3, 3, 3, 3])

    multi_bar(
        'desempenho individual',
        names,
        'Notas',
        values,
        'Críterio avaliativo',
        ['TG', 'PO', 'KE', 'PT', 'QU'],
        ['orange', 'green', 'blue', 'pink', 'red', 'green', 'blue', 'magenta', 'black', 'gray']
    )
teste()






def PO():
    multi_bar(
        'desempenho individual',
        ['Rodrigo', 'rogerio', 'marta', 'Cleitinho'],
        'Notas',
        [
            [4, 3, 5, 4, 2],
            [5, 4, 3, 4, 6],
            [4, 2, 4, 5, 4],
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


