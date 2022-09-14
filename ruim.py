from tkinter import *

#cores
co0 = "#FAE8E8" #rosa
co1 = "#D9D9D9" #cinza
co2 = "#1A1D1A" #preta


#criando a janela
janela = Tk()
janela.title('')
janela.geometry('1300x670')  # aqui coloco o tamanho da tela, largura x altura
#tentativa de dar numero de linhas e colunas para a tabela. Se deixo ativado, os labels ficam espalhados pela tela.
# janela.rowconfigure([0,1,2,3], weight = 1, minsize=30)
# janela.columnconfigure([0,1,2], weight = 1, minsize=30)
janela.configure(background=co0)

#função de criar frame
#row e column referem-se ao numero de linhas e colunas que o frame terá, já linha e coluna referem-se
# ao local onde o frame será colocado
def criar_frame(quadro, row, column, linha, coluna):
    frame = Frame(quadro, background = co0)
    frame.rowconfigure(row, minsize = 0)
    frame.columnconfigure(column, minsize = 0)
    frame.grid(row = linha, column = coluna)
    return frame

###criar widgets ###quadro é se seá colocado na janela ou em frame
def criar_label(quadro, text, font, r, c):
    Label(quadro, text = text, font = font, background = co1).grid(row=r, column=c, sticky = "w")

def criar_entry(quadro, font, r, c):
    entrada = Entry(quadro, font = font, justify = "left")
    entrada.grid(row=r, column=c, sticky = "w")
    return entrada

def criar_button(quadro, text, font, r, c, command):
    Button(quadro, text = text, font = font, height = 0, command = command ).grid(row=r, column=c, sticky = "w")

#função que pegar o valor da caixa de entrada do "n° de sprints, ao apertar o button.
# essa função também "abre um frame" para que as linhas referentes ao cadastro da sprint sejam encaixadas
def entry_sprint():
    valor = int(en_numsprints.get())
    frame_sprint = criar_frame(janela, valor, 4, 3, 2)
    for i in range(valor):
        criar_label(frame_sprint, f"Sprint {i+1}", "Calibri, 10", i, 0)
        criar_label(frame_sprint, "Data de início", "Calibri, 10", i, 1)
        criar_entry(frame_sprint, "Calibri, 10", i, 2)
        criar_label(frame_sprint, "Data final", "Calibri, 10", i, 3)
        criar_entry(frame_sprint, "Calibri, 10", i, 4)
        criar_label(frame_sprint, "Dias para avaliação", "Calibri, 10", i, 5)
        criar_entry(frame_sprint, "Calibri, 10", i, 6)


#coloca os widgets no frame de sprintsuh
criar_label(janela, "Cadastro", "Calibri, 14", 0, 0)
criar_label(janela, "Sprints", "Calibri, 12", 1, 0)
criar_label(janela, "Número de Sprints", "Calibri, 10", 2, 0)
en_numsprints = criar_entry(janela, "Calibri, 10", 2, 1)
criar_button(janela, "Cadastrar", "Calibri, 10", 2, 2, command = entry_sprint)



def entry_times():
    valor = int(en_numtimes.get())
    frame_time = criar_frame(janela, valor, 2, 6, 2)
    lista = []
    for i in range(valor):
        criar_label(frame_time, f"Time {i+1}", "Calibri, 10", i, 0)
        criar_label(frame_time, "Quantidade de alunos", "Calibri, 10", i, 1)
        en_numalunos = criar_entry(frame_time, "Calibri, 10", i, 2)
        lista.append(criar_button(frame_time, "Cadastrar", "Calibri, 10", i, 3, command = entry_alunos))

def alunos():
    num_alunos = int(en_numalunos.get())
    valor = int(en_numalunos.get())
    criar_label(frame_alunos, "teste", "Calibri, 10", valor, 0)
    frame_alunos = criar_frame(frame_time, valor, 4, 7, 2)


#coloca os widgets no frame de times
criar_label(janela, "Times", "Calibri, 12", 4, 0)
criar_label(janela, "Quantidade de Times", "Calibri, 10", 5, 0)
en_numtimes = criar_entry(janela, "Calibri, 10", 5, 1)
criar_button(janela, "Cadastrar", "Calibri, 10", 5, 2, command = entry_times)







janela.mainloop()






