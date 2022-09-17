from tkinter import *
from KML import KML
# cores
co0 = "#FAE8E8" #rosa
co1 = "#D9D9D9" #cinza
co2 = "#1A1D1A" #preta

# função de criar frame
# row e column referem-se ao numero de linhas e colunas que o frame terá, já linha e coluna referem-se
# ao local onde o frame será colocado
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
        criar_button(frame_time_data, "Cadastrar", "Calibri, 10", row, 3, command = update_member_forms)


# Atualiza a tela para criar os formularios para cada membro de acordo com o numero de membros especificado em cada time
def update_member_forms():

    # acessa a lista global de frames de time
    global lista_frame_time

    # pra cada frame_time da lista
    for ft_index, frame_time in enumerate(lista_frame_time):


        num_alunos = get_entry_int(frame_time.winfo_children()[0].children['!entry'])


        members_parent = reset_or_create_frame(frame_time, 1, ft_index + 1)

        # se nenhum aluno for cadastrado nesse time,
        # significa que não há mais nenhum passo a ser executado para o frame_time atual, continue o loop 
        if num_alunos < 1:
            continue 

        # para cada aluno, cria um formulário de cadastro
        for i in range(num_alunos):
            criar_formulario_aluno(members_parent, i)


def reset_or_create_frame(parent:Frame, index:int, row:int):

    # tenta executar o proximo código
    try:

        # acessa o child de index 1 (frame) no parent
        frame = parent.winfo_children()[index]
        # print(f"frame já existe: {frame}")

        # deleta o frame
        frame.destroy()

    # caso não encontre o frame dentro do parent:
    # frame não existe
    except:
        """"""
        # print("frame doesn't exist")
    
    # pelo menos 1 aluno será cadastrado, crie o frame para armazenar o formulario
    frame = criar_frame(parent, row, 0)

    # Retorna o frame
    return frame


# Retorna o valor na entry especificada
def get_entry_int (entry):

    # tenta acessar o valor na entry especificada e retorná-lo como int
    try:
        return int(entry.get())

    # em caso de erro, retorne 0
    except:
        return 0


# Cria os campos para o cadastro de UM aluno
def criar_formulario_aluno (parent, row):
    criar_label(parent, "Nome",   "Calibri, 10", row, 0)
    criar_entry(parent,           "Calibri, 10", row, 1)
    criar_label(parent, "E-Mail", "Calibri, 10", row, 2)
    criar_entry(parent,           "Calibri, 10", row, 3)





# HIERARQUIA:
#
#            janela
#            |
#            |   janela_header                       # contém o titulo "Cadastro"
#            |
#            |   frame_section0                      # separa a primeira seção da janela
#            |   |
#            |   |   sprints_header                  # contem o cabeçalho do cadastro de sprints
#            |   |   frame_parent_sprints            # contem cada sprint
#            |   |   |   sprint_form                 # um sprint_form para cada sprint
#            |   |   |   ...
#            |   |
#            |
#            |   frame_section1                      # separa a segunda seção da janela
#            |   |
#            |   |   teams_header                    # contem o cabeçalho do cacdastro de times
#            |   |   frame_parent_times              # contem cada frame_time
#            |   |   |
#            |   |   |   frame_time                  # um frame_time para cada time
#            |   |   |   |   members_parent          # intermédio entre frame_time e cada membro
#            |   |   |   |   |   member_form         # contem o formulário de um membro
#            |   |   |   |   |   
#            |   |   |   |      
#            |   |   |   frame_time[...]
#            |   |   |   frame_time[...]
#            |   |   |
#            |   |
#            |



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

# janela_header
criar_label(janela, "Cadastro", "Calibri, 14", 0, 0)

# cria a seção de sprints
frame_section0 = criar_frame(janela, 1, 0)
frame_sprints = criar_frame(frame_section0, 0, 0)

# título
criar_label(frame_sprints, "Sprints", "Calibri, 12", 0, 0)

# input: label, entry, button
criar_label(frame_sprints, "Número de Sprints", "Calibri, 10", 1, 0)
en_numsprints = criar_entry(frame_sprints, "Calibri, 10", 1, 1)
criar_button(frame_sprints, "Cadastrar", "Calibri, 10", 1, 2, command = entry_sprint)

# data: list-wrapper
frame_parent_sprints = criar_frame(frame_section0, 2, 0)

# Cria uma 'section' de acordo com a seguinte hierarquia:
#           section
#           |   header
#           |   |   title
#           |   |   header_data     (ex.: [label, entry, button])
#           |   section_data        (ex.: [list-wrapper])
#
# Onde 'section' contém 'header' e 'section_data' e
#      'header' contém 'title' e 'header_data'
#
# '...._data' corresponde a uma lista de parametros a serem convertidos em widgets

def create_section (window, row, title, header_data, ):
    frame_section = criar_frame(window, row, 0)


# cria a seção de times
frame_section1 = criar_frame(janela, 2, 0)
times_header = criar_frame(frame_section1, 0, 0)

# título
criar_label(times_header, "Times", "Calibri, 12", 0, 0)

# input: label, entry, button
criar_label(times_header, "Quantidade de Times", "Calibri, 10", 1, 0)
en_numtimes = criar_entry(times_header, "Calibri, 10", 1, 1)
criar_button(times_header, "Cadastrar", "Calibri, 10", 1, 2, command = entry_times)

# data: list-wrapper
frame_parent_times = criar_frame(frame_section1, 2, 0)


janela.mainloop()






