from tkinter import * 
from tkinter import ttk
from Models.Role import get_role_name
from Users.Authentication import CURRENT_USER

from Settings import co0

# Informações do modulo
NAME = 'Avaliar'
REQUIRED_PERMISSIONS_REG  = [None]
REQUIRED_PERMISSIONS_RATE = [
    [3, 4, 5]
]
REQUIRED_PERMISSIONS_VIEW = [None]

# executa o modulo e retorna
def run(frame_parent, to_user_id):
    #Criar um frame para comportar o canvas
    frm_main=Frame(frame_parent, bg=co0)
    frm_main.grid(row=0, column=1, sticky='nsew')

    # O canvas aceita o scrollbar, mas ela só faz o papel da responsividade
    canvas=Canvas(frm_main, bg=co0)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Configurações do scrollbar
    scrollbar_ver = ttk.Scrollbar(frm_main, orient=VERTICAL, command=canvas.yview) # Comando xview para orientação HORIZONTAL
    scrollbar_ver.pack(side=RIGHT, fill=Y)

    # Configurações do canvas
    canvas.configure(yscrollcommand=scrollbar_ver.set) # xscrollcomand para barra horizontal
    module_frame=Frame(canvas, bg=co0, relief=FLAT, bd=3) # Não colocamos o frame com o .pack nesse caso
    module_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar

    # Integração do frame geral a uma janela do canvas
    canvas.create_window((0,0), window=module_frame, anchor='nw')

    # Comporta todos os outros frames. Deu erro quando coloquei diretamente no frm_geral
    frm_avaliacao=Frame(module_frame, bg=co0, relief=FLAT, bd=3)
    frm_avaliacao.grid(row=0, rowspan=30, column=0, columnspan=3, sticky='w')

    frm_criterias = []

    # TENTEI COLOCAR A CRIAÇÃO DOS FRAMES COMO FUNÇÃO, MAS DEU CONFLITO (não permite colocar .grid em algo .pack). Criando um por um não dá erro
    frame_header=Frame(frm_avaliacao, bg=co0, relief=FLAT, bd=3)
    frame_header.grid(row= 0, column=0, columnspan=4, sticky='nsew')
    frame_header.columnconfigure(0, weight=1)
    frame_header.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)

    # Textos gerais da tela
    title        = 'Autoavaliação' if to_user_id == CURRENT_USER.id else 'Avaliação'
    from CSV.CSVHandler import find_data_by_id_csv
    from Settings import USERS_PATH
    to_user_name = CURRENT_USER.name if to_user_id == CURRENT_USER.id else find_data_by_id_csv(USERS_PATH, str(to_user_id))['name']
    criar_label(frame_header, title, 30, 0, 0, 5, 5, 'w')
    criar_label(frame_header, to_user_name, 20, 0, 1, 5, 5, 'w')
    criar_label(frame_header, get_role_name(CURRENT_USER.role_id), 15, 0, 2, 5, 5, 'w')
    criar_label(frame_header, 'Prazo para realizar a autoavaliação da {nº da Sprint}', 15, 0, 3, 5, 5, 'w')  # PUXAR DADO VINCULADO COM TELA DE RETORNO ???
    criar_label(frame_header, 'Esta avaliação 360° utiliza a escala Likert para medir o desempenho dos usuários. Notas abaixo ou iguais a 3 necessitam obrigatoriamente de Feedback (resposta descritiva)', 11, 0, 4, 5, 5, 'w')  

    perguntas = [
        '1) Como você se avalia em trabalho em equipe, cooperação e descentralização de conhecimento?',
        '2) Como você se avalia em iniciativa e proatividade?',
        '3) Como você se avalia em autodidaxia e agregação de conhecimento ao grupo?',
        '4) Como você se avalia em entrega de resultados e participação efetiva no projeto?',
        '5) Como você se avalia em competência técnica?'
    ]

    escalas = []
    feedbacks = [None, None, None, None, None]

    for i in range(5):

        frm_criteria = Frame(frm_avaliacao, bg=co0, relief=GROOVE, bd=3)
        frm_criteria.grid(row= i+1, column=0, columnspan=2, sticky='nsew')
        frm_criteria.columnconfigure(0, weight=1)
        frm_criteria.rowconfigure([0, 1, 2, 3, 4], weight=1)

        frm_criteria_data = Frame(frm_criteria, bg=co0)
        frm_criteria_data.grid(row= 0, column=0, sticky='nsew')
        frm_criteria_data.columnconfigure(0, weight=1)
        frm_criteria_data.rowconfigure([0, 1, 2, 3, 4], weight=1)

        criar_label(frm_criteria_data, perguntas[i], 10, 0, 4, 5, 5, 'w')
        criar_label(frm_criteria_data, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 5, 5, 5, 'w')
        escalas.append(criar_escala(frm_criteria_data, 6, lambda _, index=i: computar_resposta(int(index))))

        frm_criterias.append(frm_criteria)
    

    def enviar_retorno():
        label=Label(master=module_frame, text='Avaliação enviada com sucesso!',
        bg=co0, fg='#1a1d1a', font=('Calibre', 10))
        label.place(relx=0.82, rely=0.09, relheight=0.03, relwidth=0.17)

    # def criar_label(master, text, tamanho, column, row, padx, pady, sticky):
    def computar_resposta(i):

        # print("computar_respostas")

        frm_criteria = frm_criterias[i]

        # print(f'[{i}]: {frm_criteria.winfo_children()}')

        try:
            frm_criteria_feedback = frm_criteria.winfo_children()[1]
            frm_criteria_feedback.destroy()
            feedbacks[i] = None
        except:
            pass

        if escalas[i].get() <= 3:

            frm_criteria_feedback = Frame(frm_criteria, bg=co0)
            frm_criteria_feedback.grid(row= 0, column=1, sticky='nsew')
            frm_criteria_feedback.columnconfigure(0, weight=1)
            frm_criteria_feedback.rowconfigure([0, 1, 2, 3, 4], weight=1)

            criar_label(frm_criteria_feedback, f'Feedback obrigatório para critério {i+1}: ', 10, 1, 3, 0, 0, 'w')
            feedbacks[i] = criar_entrada(frm_criteria_feedback, 3, 2, 0, 10, 'w')


    # Função para criação de caixas de entrada
    def criar_entrada(master, row, column, padx, pady, sticky):
        feedback=Entry(master=master, width=60, fg='#1a1d1a', font=('Calibre 10'))
        feedback.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return feedback

    def enviar_notas(_to_user_id):

        from Utils.back_avaliacao import dados_avaliacao

        notas = []
        comentarios = [None, None, None, None, None]

        for i in range(5):

            # print(f'escalas[i]: {escalas[i]} | escalas[i].get {escalas[i].get}')

            nota = escalas[i].get()

            # try:
            #     comentario = feedbacks[i].get()
            # except:
            #     comentario = ''
            print(f'feedbacks[i] is None: {feedbacks[i] is None}')

            comentario = feedbacks[i].get() if feedbacks[i] is not None else ''
            print(f'comentario: {comentario}')

            notas.append(nota)
            comentarios[i] = comentario

        dados_avaliacao(_to_user_id, notas, comentarios)

        enviar_retorno()


    # Botão para registrar notas e conferir a necessidade de feedback
    # button=Button(master=frm_main, text='Registrar Notas', fg='#1a1d1a', bg='#d9d9d9', 
    # font=('Calibre', 10), width=13, height=1, activebackground='#c5a8b0', command=computar_respostas)
    # button.place(relx=0.59, rely=0.09, relheight=0.04, relwidth=0.08)
    # resposta(p1, 0), resposta(p2, 5), resposta(p3, 10), resposta(p4, 15), resposta(p5, 20)

    # Botão para enviar notas para o banco de dados
    button1=Button(master=module_frame, text='Enviar Avaliação', fg='#1a1d1a', bg='#d9d9d9', 
        font='Calibre, 12', height=0, activebackground='#c5a8b0', command= lambda : enviar_notas(to_user_id)
    )
    button1.place(relx=0.69, rely=0.09)

    # window.mainloop()


# Função para criação de texto
def criar_label(master, text, tamanho, column, row, padx, pady, sticky):
    label=Label(master=master, text=text, fg='#1a1d1a'
    , bg=co0, font=('Calibre', tamanho))
    label.grid(column=column, row=row, padx=padx, pady=pady, sticky=sticky)

def criar_escala(master, row, command):
    _escala = Scale(master=master, from_=1, to=5, length=500, tickinterval=1, orient=HORIZONTAL, 
        bg=co0, font='Calibre, 10', highlightcolor='#c5a8b0', troughcolor='#c5a8b0', state='normal', variable=IntVar(),
        command=command
    )
    _escala.grid(column=0, row=row, padx=5, pady=5, sticky='w')
    _escala.set(1)
    return _escala
