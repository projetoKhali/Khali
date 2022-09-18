from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk

#cores
co0 = "#FAE8E8" #rosa
co1 = "#D9D9D9" #cinza
co2 = "#1A1D1A" #preta

#FUNÇÃO SPRINT = PEGA O VALOR QUE FOI DIGITADO NA QUANTIDADE DE SPRINTS
def sprints():
    global frame_sprint
    global en_nSprint
    global janela

    #FUNÇÃO QUE PEGA O NUMERO DE TIMES
    def times():
        nonlocal en_Times
        num_times = int(en_Times.get())
        lista2 = list(range(num_times))
        frame_xTimes = tk.Frame(janela, background=co0)
        frame_xTimes.rowconfigure(num_times, minsize=0)
        frame_xTimes.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=0)
        frame_xTimes.grid(sticky="ew")


        def alunos():
            nonlocal en_quantAlunos
            global janela
            print('oi')
            num_alunos = int(en_quantAlunos.get())
            lista3 = list(range(num_alunos))
            frame_xalunos = tk.Frame(janela, background=co0)
            frame_xalunos.rowconfigure([0,1,2,3,4,5,6,7,8,9], minsize=0)
            frame_xalunos.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=0)
            frame_xalunos.grid(sticky="ew")

        #estou me referindo, fora da função, a variavel q está dentro da função. O for está fora


        for i in range(0, num_times):
            lb_timex = tk. Label(frame_xTimes, text = (f'Time{i+1}: '), font=("Calibri, 10"), background=co0)
            lb_timex.grid(row=i, column=0, sticky="w")
            lb_quantAlunos = tk.Label(frame_xTimes, text="Quantidade de alunos no time", font=("Calibri, 10"), background=co0)
            lb_quantAlunos.grid(row=i, column=1, sticky="w")
            en_quantAlunos = tk.Entry(frame_xTimes, font = "Calibri, 10", justify = "left")
            en_quantAlunos.grid(row=i, column=2, sticky="w")
            lb_cadastrar6 = tk.Button(frame_xTimes, text='Cadastrar', font=("Calibri, 10"), background=co0, height=1, command=alunos)
            lb_cadastrar6.grid(row=i, column=3, sticky="w")
            def teste():
                nonlocal en_quantAlunos

                numm_alunos = int(en_quantAlunos.get())
                for j in range(numm_alunos):
                    lb_teste = tk.Label(frame_xalunos, text=(f"aluno{numm_alunos}"), font=("Calibri, 10"), background=co0)
                    lb_teste.grid(row=j, column=0, sticky="w")
            teste()



    num_sprints = int(en_nSprint.get())
    frame_xSprint = tk.Frame(janela, background=co0)
    lista = list(range(num_sprints))
    frame_xSprint.rowconfigure(num_sprints, minsize=0)
    frame_xSprint.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=0)
    frame_xSprint.grid(sticky="ew")
    #***aqui terei que colocar get() para cada looping, para armazenar todas variáveis, (fazer lista)
    for i in range(0,num_sprints):
        lb_xSprint = tk.Label(frame_xSprint, text=(f'Sprint{i+1}: '), font=("Calibri, 10"), background=co0)
        lb_xSprint.grid(row=i, column=0, sticky="w")
        lb_dataInicio = tk.Label(frame_xSprint, text=(f'Data de início'), font=("Calibri, 10"), background=co0)
        lb_dataInicio.grid(row=i, column=1, sticky="w")
        en_dataInicio = tk.Entry(frame_xSprint, font = "Calibri, 10", justify = "left")
        en_dataInicio.grid(row=i, column=2, sticky="w")
        lb_dataFim = tk.Label(frame_xSprint, text=(f'Data Final'), font=("Calibri, 10"), background=co0)
        lb_dataFim.grid(row=i, column=3, sticky="w")
        en_dataFim = tk.Entry(frame_xSprint, font="Calibri, 10", justify="left")
        en_dataFim.grid(row=i, column=4, sticky="w")
        lb_periodo = tk.Label(frame_xSprint, text=(f'Período para Avaliação (dias)'), font=("Calibri, 10"), background=co0)
        lb_periodo.grid(row=i, column=5, sticky="w")
        en_periodo = tk.Entry(frame_xSprint, font="Calibri, 10", justify="left")
        en_periodo.grid(row=i, column=6, sticky="w")
        lb_cadastrar2 = tk.Button(frame_xSprint, text='Cadastrar', font=("Calibri, 10"), background=co0, height=0)
        lb_cadastrar2.grid(row=i, column=7, sticky="w") #se eu falar que tenho 4 sprints, esse label ficará na quinta linha
    #Frame do Fake Client
    frame_FakeClient = tk.Frame(janela, background=co0)
    frame_FakeClient.rowconfigure([1,2,3,4], minsize=0)
    frame_FakeClient.columnconfigure([1,2,3,4,5,6,7], minsize=0)
    frame_FakeClient.grid(sticky="ew")
    #Widgets do Fake Client
    titulo_FakeClient = tk.Label(frame_FakeClient, text = "Fake Client", font = ("Calibri, 12"), background=co0)
    titulo_FakeClient.grid(row=0, column=0)
    lb_nomeFakeClient = tk.Label(frame_FakeClient, text="Nome", font=("Calibri, 10"), background=co0)
    lb_nomeFakeClient.grid(row=1, column=0, sticky = "w")
    en_nomeFakeClient = tk.Entry(frame_FakeClient, font = "Calibri, 10", justify = "left", width = 50)
    en_nomeFakeClient.grid(row=1, column=1, sticky = "w")
    lb_emailFakeClient = tk.Label(frame_FakeClient, text="E-mail", font=("Calibri, 10"), background=co0)
    lb_emailFakeClient.grid(row=2, column=0, sticky="w")
    en_emailFakeClient = tk.Entry(frame_FakeClient, font="Calibri, 10", justify="left", width=50)
    en_emailFakeClient.grid(row=2, column=1, sticky="w")
    lb_cadastrar3 = tk.Button(frame_FakeClient, text='Cadastrar', font=("Calibri, 10"), background=co0, height=0)
    lb_cadastrar3.grid(row=1, column=2, sticky="w")
    lb_cadastrar3 = tk.Button(frame_FakeClient, text='Cadastrar', font=("Calibri, 10"), background=co0, height=0)
    lb_cadastrar3.grid(row=2, column=2, sticky="w")

    #FrameTimes
    frame_Times = tk.Frame(janela, background=co0)
    frame_Times.rowconfigure([1, 2, 3, 4], minsize=0)
    frame_Times.columnconfigure([1, 2, 3, 4, 5, 6, 7], minsize=0)
    frame_Times.grid(sticky="ew")
    #WidgetsTimes
    titulo_Times = tk.Label(frame_Times, text='Times', font=("Calibri, 12"), background=co0)
    titulo_Times.grid(row=0, column=0, sticky="w")
    lb_Times = tk.Label(frame_Times, text='Quantidade de Times', font=("Calibri, 10"), background=co0)
    lb_Times.grid(row=1, column=0, sticky="w")
    en_Times = tk.Entry(frame_Times, font="Calibri, 10", justify="left", width=50)
    en_Times.grid(row=1, column=1, sticky="w")
    lb_cadastrar4 = tk.Button(frame_Times, text='Cadastrar', font=("Calibri, 10"), background=co0, height=0, command = times)
    lb_cadastrar4.grid(row=1, column=2, sticky="w")






#criando janela
janela = tk.Tk()
janela.title('')
janela.geometry('1300x670') #aqui coloco o tamanho da tela, largura x altura
janela.configure(background=co0)
janela.resizable(width=FALSE, height=FALSE)


#criando as frames das sprints
frame_sprint = tk.Frame(janela, background = co0)
frame_sprint.rowconfigure([0,1,2,3], minsize = 0)
frame_sprint.columnconfigure([0,1,2,3,4,5,6,7], minsize = 0)
frame_fakeclient = tk.Frame(janela, background = co0)
frame_times = tk.Frame(janela, background = co0)

#criando os widgets - 1°Frame
titulo_Cadastro = tk.Label(frame_sprint, text = 'Cadastro', font = ("Calibri, 14"), background = co0)
titulo_Sprint = tk.Label(frame_sprint, text = 'Sprints', font = ("Calibri, 12"), background = co0)
titulo_Cadastro.grid(row=0, column = 0, sticky = "w")
titulo_Sprint.grid(row=1, column = 0, sticky = "w")
lb_nSprint = tk.Label(frame_sprint, text = 'Número de Sprints', font = ("Calibri, 10"), background = co0)
lb_nSprint.grid(row=2, column = 0, sticky = "w")
en_nSprint = tk.Entry(frame_sprint, font = "Calibri, 10", justify = "left")
en_nSprint.grid (row=2, column = 1, sticky = "w")
lb_cadastrar1 = tk.Button(frame_sprint, text = 'Cadastrar', font = ("Calibri, 10"), background = co0, height = 0, command = sprints)
lb_cadastrar1.grid(row=2, column = 2, sticky = "w")


#colocando a frame do sprint no lugar
frame_sprint.grid(sticky = "ew")





janela.mainloop()