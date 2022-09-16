from tkinter import *

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
    frame_sprint = criar_frame(frame_section0, valor, 0)
    for i in range(valor):
        criar_label(frame_sprint, f"Sprint {i+1}", "Calibri, 10", i, 0)
        criar_label(frame_sprint, "Início", "Calibri, 10", i, 1)
        criar_entry(frame_sprint, "Calibri, 10", i, 2)
        criar_label(frame_sprint, "Fim", "Calibri, 10", i, 3)
        criar_entry(frame_sprint, "Calibri, 10", i, 4)
        criar_label(frame_sprint, "Dias para avaliação", "Calibri, 10", i, 5)
        criar_entry(frame_sprint, "Calibri, 10", i, 6)

def entry_times():
    valor = int(en_numtimes.get())
    for i in range(valor):
        row = i
        frame_time = criar_frame(frame_parent_times, row, 0)
        lista_frame_time.append(frame_time)

        frame_time_data = criar_frame(frame_time, 0, 0)
        criar_label(frame_time_data, f"Time {i+1}", "Calibri, 10", row, 0)
        criar_label(frame_time_data, "Quantidade de alunos", "Calibri, 10", row, 1)
        criar_entry(frame_time_data, "Calibri, 10", row, 2)
        # lista.append(criar_button(frame_time_data, "Cadastrar", "Calibri, 10", i, 3, command = entry_alunos(en_numalunos)))
        criar_button(frame_time_data, "Cadastrar", "Calibri, 10", row, 3, command = entry_alunos)

def entry_alunos():

    # acessa a lista global de frames de time
    global lista_frame_time

    # pra cada frame_time da lista
    for ft_index, frame_time in enumerate(lista_frame_time):

        # 1) criar ou acessar o frame_parent_aluno caso já exista.
        # caso exista: deleta o frame_parent_aluno
        # caso não exista: continua com a execução do código

        # tenta executar o proximo código
        try:

            # acessa o child de index 1 (frame_parent_aluno) no frame_time
            frame_parent_aluno = frame_time.winfo_children()[1]
            print(f"frame_parent_aluno já existe: {frame_parent_aluno}")

            # deleta o frame
            frame_parent_aluno.destroy()

        # caso não encontre o frame_parent_aluno dentro do frame_time:
        # frame_parent_aluno não existe
        except:
            print("frame_parent_aluno doesn't exist")

        # 2) após assegurar que não exista um frame_parent_aluno nesse frame_time,
        # define o numero de alunos a serem registrados no time 
        # e cria um formulario de cadastro para cada

        # inicializa a variavel que armazena o numero de alunos desejado
        num_alunos = 0

        # tenta acessar a entry que contem o numero de alunos fornecido
        try:
            en_numalunos = frame_time.winfo_children()[0].children['!entry']
        except:
            print("entry not found")

        # tenta passar o valor na entry en_numalunos para a variavel num_alunos
        try:
            num_alunos = int(en_numalunos.get())
            print(f'en_numalunos:  OK  | {num_alunos}')

        # em caso de erro, mantenha num_alunos em 0 (previamente inicializado)
        except:
            print(f'en_numalunos: NULO | {num_alunos}')

        # se nenhum aluno for cadastrado nesse time,
        # significa que não há mais nenhum passo a ser executado para o frame_time atual, continue o loop 
        if num_alunos < 1:
            continue 

        # pelo menos 1 aluno será cadastrado, crie o frame_parent_aluno para armazenar o formulario
        frame_parent_aluno = criar_frame(frame_time, ft_index + 1, 0)

        # para cada aluno, cria um formulário de cadastro
        for i in range(num_alunos):
            criar_formulario_aluno(frame_parent_aluno, i)

def criar_formulario_aluno (frame_parent_aluno, index):
    criar_label(frame_parent_aluno, "Nome", "Calibri, 10", index, 0)
    criar_entry(frame_parent_aluno, "Calibri, 10", index, 1)
    criar_label(frame_parent_aluno, "E-Mail", "Calibri, 10", index, 2)
    criar_entry(frame_parent_aluno, "Calibri, 10", index, 3)


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

# HIERARQUIA:
#
# janela
#   label                               # contém o titulo "Cadastro"
#   frame_section0                      # separa a primeira seção da janela
#       frame_sprints                   # contem o cabeçalho do cadastro de sprints
#       frame_parent_sprints            # contem cada frame_sprint
#           frame_sprint                # um frame_sprint para cada
#           ...
#   frame_section1                      # separa a segunda seção da janela
#       frame_times                     # contem o cabeçalho do cacdastro de times
#       frame_parent_times              # contem cada frame_time
#           frame_time                  # um frame_time para cada time
#           ...




# cria a seção de sprints
frame_section0 = criar_frame(janela, 1, 0)
frame_sprints = criar_frame(frame_section0, 0, 0)
criar_label(frame_sprints, "Sprints", "Calibri, 12", 0, 0)
criar_label(frame_sprints, "Número de Sprints", "Calibri, 10", 1, 0)
en_numsprints = criar_entry(frame_sprints, "Calibri, 10", 1, 1)
criar_button(frame_sprints, "Cadastrar", "Calibri, 10", 1, 2, command = entry_sprint)
frame_parent_sprints = criar_frame(frame_section0, 2, 0)


# cria a seção de times
frame_section1 = criar_frame(janela, 2, 0)
frame_times = criar_frame(frame_section1, 0, 0)
criar_label(frame_times, "Times", "Calibri, 12", 0, 0)
criar_label(frame_times, "Quantidade de Times", "Calibri, 10", 1, 0)
en_numtimes = criar_entry(frame_times, "Calibri, 10", 1, 1)
criar_button(frame_times, "Cadastrar", "Calibri, 10", 1, 2, command = entry_times)
frame_parent_times = criar_frame(frame_section1, 2, 0)







janela.mainloop()






