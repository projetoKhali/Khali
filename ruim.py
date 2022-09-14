from ast import Pass
from tkinter import *
from warnings import catch_warnings

# cores
co0 = "#FAE8E8" #rosa
co1 = "#D9D9D9" #cinza
co2 = "#1A1D1A" #preta

# função de criar frame
# row e column referem-se ao numero de linhas e colunas que o frame terá, já linha e coluna referem-se
# ao local onde o frame será colocado
# def criar_frame(quadro, row, column, linha, coluna):
#     frame = Frame(quadro, background = co0)
#     frame.rowconfigure(row, minsize = 0)
#     frame.columnconfigure(column, minsize = 0)
#     frame.grid(row = linha, column = coluna)
#     return frame
def criar_frame(quadro, row, column):
    frame = Frame(quadro, background = co0)
    frame.rowconfigure(row, minsize = 0)
    frame.columnconfigure(column, minsize = 0)
    frame.grid(row=row, column=column, sticky='w')
    return frame

# criar widgets ###quadro é se seá colocado na janela ou em frame
def criar_label(quadro, text, font, r, c):
    Label(quadro, text=text, font=font, background=co1).grid(row=r, column=c, sticky = "w")

def criar_entry(quadro, font, r, c):
    entrada = Entry(quadro, font = font, justify = "left")
    entrada.grid(row=r, column=c, sticky = "w")
    return entrada

def criar_button(quadro, text, font, r, c, command):
    Button(quadro, text = text, font = font, height = 0, command = command ).grid(row=r, column=c, sticky = "w")

# função que pegar o valor da caixa de entrada do "n° de sprints, ao apertar o button.
# essa função também "abre um frame" para que as linhas referentes ao cadastro da sprint sejam encaixadas
def entry_sprint():
    try:
        valor = int(en_numsprints.get())
    except:
        return
    # frame_sprint = criar_frame(janela, valor, 4, 3, 2)
    frame_sprint = criar_frame(janela, valor, 3)
    for i in range(valor):
        criar_label(frame_sprint, f"Sprint {i+1}", "Calibri, 10", i, 0)
        criar_label(frame_sprint, "Data de início", "Calibri, 10", i, 1)
        criar_entry(frame_sprint, "Calibri, 10", i, 2)
        criar_label(frame_sprint, "Data final", "Calibri, 10", i, 3)
        criar_entry(frame_sprint, "Calibri, 10", i, 4)
        criar_label(frame_sprint, "Dias para avaliação", "Calibri, 10", i, 5)
        criar_entry(frame_sprint, "Calibri, 10", i, 6)

def entry_times():
    valor = int(en_numtimes.get())
    frame_parent_times = criar_frame(frame_times, 2, 0)
    for i in range(valor):
        row = i
        frame_time = criar_frame(frame_parent_times, row, 0)
        criar_label(frame_time, f"Time {i+1}", "Calibri, 10", row, 0)
        criar_label(frame_time, "Quantidade de alunos", "Calibri, 10", row, 1)
        criar_entry(frame_time, "Calibri, 10", row, 2)
        # lista.append(criar_button(frame_time, "Cadastrar", "Calibri, 10", i, 3, command = entry_alunos(en_numalunos)))
        lista_frame_time.append(frame_time)
        criar_button(frame_time, "Cadastrar", "Calibri, 10", row, 3, command = entry_alunos)

def entry_alunos():
    print("chegamos na função entry_alunos")
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    global lista_frame_time
    for ft_index, frame_time in enumerate(lista_frame_time):
        en_numalunos = frame_time.children['!entry']
        num_alunos = 0
        try:
            num_alunos = int(en_numalunos.get())
            print(num_alunos)
        except:
            print(f'en_numalunos nulo: {num_alunos}')

        try:
            frame_parent_aluno = frame_time.children['!frame']
            print(f"frame_parent_aluno já existe: {frame_parent_aluno}")
            frame_parent_aluno.configure(background='#ffff00')

            lista_label_aluno = frame_parent_aluno.winfo_children()

            print(f'children: {lista_label_aluno}')

            for label_aluno in lista_label_aluno:
                label_aluno.configure(background='#ff0000', height=0)            
                label_aluno.destroy()
                label_aluno.grid_forget()
                print(f'children: {lista_label_aluno}')
                # del label_aluno
            frame_parent_aluno.forget()
        except:
            Pass

        if num_alunos > 0:
            frame_parent_aluno = criar_frame(frame_time, ft_index + 1, 0)
            for i in range(num_alunos):
                criar_label(frame_parent_aluno, "teste", "Calibri, 10", i, 0)
        # else:
        #     frame_parent_aluno.destroy()
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print("fim da função entry_alunos")


# criando a janela
janela = Tk()
janela.title('')
res = '800x400'
# res = '1300x670'
janela.geometry(res)  # aqui coloco o tamanho da tela, largura x altura
# tentativa de dar numero de linhas e colunas para a tabela. Se deixo ativado, os labels ficam espalhados pela tela.
# janela.rowconfigure([0,1,2,3], weight = 1, minsize=30)
# janela.columnconfigure([0,1,2], weight = 1, minsize=30)
janela.configure(background=co0)

lista_frame_time = []

criar_label(janela, "Cadastro", "Calibri, 14", 0, 0)

# coloca os widgets no frame de sprints
frame_sprints = criar_frame(janela, 1, 0)
criar_label(frame_sprints, "Sprints", "Calibri, 12", 0, 0)
criar_label(frame_sprints, "Número de Sprints", "Calibri, 10", 1, 0)
en_numsprints = criar_entry(frame_sprints, "Calibri, 10", 1, 1)
criar_button(frame_sprints, "Cadastrar", "Calibri, 10", 1, 2, command = entry_sprint)


# coloca os widgets no frame de times
frame_times = criar_frame(janela, 2, 0)
criar_label(frame_times, "Times", "Calibri, 12", 0, 0)
criar_label(frame_times, "Quantidade de Times", "Calibri, 10", 1, 0)
en_numtimes = criar_entry(frame_times, "Calibri, 10", 1, 1)
criar_button(frame_times, "Cadastrar", "Calibri, 10", 1, 2, command = entry_times)







janela.mainloop()






