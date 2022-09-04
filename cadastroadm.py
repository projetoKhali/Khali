from tkinter import *  # Importar biblioteca
master = Tk()  # Instanciar a classe, para utilizar as funções da classe
master.title("Sistema de Cadastro - Administrador")  # Título da tela
master.iconbitmap(default="icokhali.ico")  # Definir ícone da tela
master.geometry("1300x670+300+200")  # Redimensionar a janela/
# Dados referentes á Largura x Altura + Distância esquerda + Distância topo
master.wm_resizable(width=False, height=False)  # Travar redimensionamento

# Importar Imagens
telacadastro = PhotoImage(file="Cadastrarturmas.png")  # Variável da imagem

# Label
labelTela = Label(master, image=telacadastro)
labelTela.place(x=0, y=0)  # A função "place" usa como parâmetro as funções x e y, coordenadas da tela

# Funções
# def clique_esq_mouse(retorno):
# print(f'X: {retorno.x} | Y: {retorno.y} Geo: {master.geometry()}') Mapear as coordenadas do cursor do mouse/
# Para reposicionar a janela, copiar as coordenadas apresentadas após o clique e colar em "master.geometry"

flag = x1 = y1 = x = 0  # Variável para funções de mesmo valor


def clique_esq_mouse(arg):  # Identificar coordenadas para criação de botões e caixas de entrada

    global flag, x1, y1
    flag = not flag
    if flag:
        x1 = arg.x
        y1 = arg.y
    else:
        print(f'width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1}')


# Criação dos botões
bt1 = Button(master, text="Cadastrar", font="Calibre 15")  # Criação parâmetro botão
bt2 = Button(master, text="Cadastrar", font="Calibre 15")
bt3 = Button(master, text="Cadastrar", font="Calibre 15")
# Posicionar botões
bt1.place(width=160, height=34, x=753, y=136)
bt2.place(width=154, height=37, x=1100, y=238)


# Criação de caixas de entrada
caixa1 = Entry(master, font="Calibre 15", justify=LEFT)
caixa2 = Entry(master, font="Calibre 15", justify=LEFT)
caixa3 = Entry(master, font="Calibre 15", justify=LEFT)
# Posicionar caixas de entrada
caixa1.place(width=185, height=41, x=523, y=133)
caixa2.place(width=233, height=43, x=524, y=236)
caixa3.place(width=184, height=40, x=858, y=237)
# Valores iniciais de entrada
caixa1.insert(END, "Insira a quatidade")
caixa2.insert(END, "Insira o nome")
caixa3.insert(END, "Insira o e-mail")

# Eventos
master.bind("<Button-1>", clique_esq_mouse)
master.mainloop()  # Criar uma janela em local aleatório que ficará em looping até que seja fechada pelo "X"
