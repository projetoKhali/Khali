from tkinter import * 
from tkinter import ttk

# Configurações da janela
window = Tk() 
window.configure(bg='#fae8e8')  # Cor do plano de fundo da tela
window.geometry("1200x600")
window.title('Autoavaliação')  # Título da janela

# Criar um frame para comportar o canvas
frm_main=Frame(window, bg='#fae8e8')
frm_main.pack(fill=BOTH, expand=1) 

# O canvas aceita o scrollbar, mas ela só faz o papel da responsividade
canvas=Canvas(frm_main, bg='#fae8e8')
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Configurações do scrollbar
scrollbar_ver = ttk.Scrollbar(frm_main, orient=VERTICAL, command=canvas.yview) # Comando xview para orientação HORIZONTAL
scrollbar_ver.pack(side=RIGHT, fill=Y)

# Configurações do canvas
canvas.configure(yscrollcommand=scrollbar_ver.set) # xscrollcomand para barra horizontal
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar

frm_geral=Frame(canvas, bg='#fae8e8', relief=FLAT, bd=3) # Não colocamos o frame com o .pack nesse caso
# Integração do frame geral a uma janela do canvas
canvas.create_window((0,0), window=frm_geral, anchor='nw')

# Comporta todos os outros frames. Deu erro quando coloquei diretamente no frm_geral
frm_avaliacao=Frame(frm_geral, bg='#fae8e8', relief=FLAT, bd=3)
frm_avaliacao.grid(row=0, rowspan=30, column=0, columnspan=3, sticky='w')

frames = []

# TENTEI COLOCAR A CRIAÇÃO DOS FRAMES COMO FUNÇÃO, MAS DEU CONFLITO (não permite colocar .grid em algo .pack). Criando um por um não dá erro
frame_header=Frame(frm_avaliacao, bg='#fae8e8', relief=FLAT, bd=3)
frame_header.grid(row= 0, column=0, columnspan=4, sticky='nsew')
frame_header.columnconfigure(0, weight=1)
frame_header.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)

for frm in range(5):
    frm_criteria=Frame(frm_avaliacao, bg='#fae8e8', relief=GROOVE, bd=3)
    frm_criteria.grid(row= frm+1, column=0, columnspan=4, sticky='nsew')
    frm_criteria.columnconfigure(0, weight=1)
    frm_criteria.rowconfigure([0, 1, 2, 3, 4], weight=1)
    frames.append(frm_criteria)

# frm_3=Frame(frm_avaliacao, bg='#fae8e8', relief=GROOVE, bd=3)
# frm_3.grid(row= 2, column=0, columnspan=4, sticky='nsew')
# frm_3.columnconfigure(0, weight=1)
# frm_3.rowconfigure([0, 1, 2, 3, 4], weight=1)
# frames.append(frm_3)

# frm_4=Frame(frm_avaliacao, bg='#fae8e8', relief=GROOVE, bd=3)
# frm_4.grid(row= 3, column=0, columnspan=4, sticky='nsew')
# frm_4.columnconfigure(0, weight=1)
# frm_4.rowconfigure([0, 1, 2, 3, 4], weight=1)
# frames.append(frm_4)

# frm_5=Frame(frm_avaliacao, bg='#fae8e8', relief=GROOVE, bd=3)
# frm_5.grid(row= 4, column=0, columnspan=4, sticky='nsew')
# frm_5.columnconfigure(0, weight=1)
# frm_5.rowconfigure([0, 1, 2, 3, 4], weight=1)
# frames.append(frm_5)

# frm_6=Frame(frm_avaliacao, bg='#fae8e8', relief=GROOVE, bd=3)
# frm_6.grid(row= 5, column=0, columnspan=4, sticky='nsew')
# frm_6.columnconfigure(0, weight=1)
# frm_6.rowconfigure([0, 1, 2, 3, 4], weight=1)
# frames.append(frm_6)

# Função para criação de texto
def criar_label(master, text, tamanho, column, row, padx, pady, sticky):
    label=Label(master=master, text=text
    , bg='#fae8e8', font=('Calibre', tamanho))
    label.grid(column=column, row=row, padx=padx, pady=pady, sticky=sticky)
 

# Textos gerais da tela
criar_label(frame_header, 'Autoavaliação', 30, 0, 0, 30, 30, 'w')
criar_label(frame_header, 'Nome do usuário', 20, 0, 1, 30, 0, 'w')  # PUXAR DADO VINCULADO COM TELA DE RETORNO - NOME E FUNÇÃO ???
criar_label(frame_header, 'Prazo para realizar a autoavaliação da {nº da Sprint}', 15, 0, 2, 30, 20, 'w')  # PUXAR DADO VINCULADO COM TELA DE RETORNO ???
criar_label(frame_header, 'Esta avaliação 360° utiliza a escala Likert para medir o desempenho dos usuários. Notas abaixo ou iguais a 3 necessitam obrigatoriamente de Feedback (resposta descritiva)',
13, 0, 3, 30, 10, 'w')  

criar_label(frames[0], '1) Como você se avalia em trabalho em equipe, cooperação e descentralização de conhecimento?', 11, 0, 4, 30, 10, 'w')
criar_label(frames[1], '2) Como você se avalia em iniciativa e proatividade?', 11, 0, 4, 30, 10, 'w')
criar_label(frames[2], '3) Como você se avalia em autodidaxia e agregação de conhecimento ao grupo?', 11, 0, 4, 30, 10, 'w')
criar_label(frames[3], '4) Como você se avalia em entrega de resultados e participação efetiva no projeto?', 11, 0, 4, 30, 10, 'w') 
criar_label(frames[4], '5) Como você se avalia em competência técnica?', 11, 0, 4, 30, 10, 'w')

escalas = []
notas = []

p = ''

def criar_escala(master, row):
    p = Scale(master=master, from_=1, to=5, length=500, tickinterval=1, orient=HORIZONTAL, 
    bg='#fae8e8', font='Calibre, 10', highlightcolor='#c5a8b0', troughcolor='#c5a8b0', state='normal', variable=IntVar())
    p.grid(column=0, row=row, padx=30, pady=0, sticky='w')
    p.set(1)
    escalas.append(p)
    return p

def enviar_notas():
    for i in escalas:
        print = print(p.get())
        notas.append(print)

print(notas)

for i, frm in enumerate(frames):
    criar_label(frm, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 5, 30, 0, 'w')
    # criar_label(frm_3, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 8, 30, 0, 'w')
    # criar_label(frm_4, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 11, 30, 0, 'w')
    # criar_label(frm_5, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 14, 30, 0, 'w') 
    # criar_label(frm_6, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 17, 30, 0, 'w')
    criar_escala(frm, 6)


# Escalas de cada um dos critérios separadas por Frame
# criar_escala(frm_3, 9)
# criar_escala(frm_4, 12)
# criar_escala(frm_5, 15)
# criar_escala(frm_6, 18)

# Função para criação de caixas de entrada
def criar_entrada(master, row, column, padx, pady, sticky):
    feedback=Entry(master=master, width=75, fg='#1a1d1a', font=('Calibre 10'))
    feedback.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)

# def criar_label(master, text, tamanho, column, row, padx, pady, sticky):
def resposta():
    for i, escala in enumerate(escalas):
        if escala.get() <= 3:
            #frm_feedback=Frame(frm_avaliacao, bg='#fae8e8', relief=FLAT, bd=3)  # Frame individual para cada feedback obrigatório
            #frm_feedback.grid(row=row, column=1, sticky='w')
            criar_label(frames[i], f'Feedback obrigatório para critério {i+1}: ', 10, 1, 6, 0, 24, 'w')
            criar_entrada(frames[i], 6, 2, 0, 0, 'w')
        # print(f'Print P1 {str(p[i].get())}')
    

def enviar_retorno():
    label=Label(master=frm_main, text='Avaliação enviada com sucesso!',
    bg='#fae8e8', font=('Calibre', 10))
    label.place(relx=0.78, rely=0.09, relheight=0.03, relwidth=0.17)


# Botão para registrar notas e conferir a necessidade de feedback
button=Button(master=frm_main, text='Registrar Notas', fg='#1a1d1a', bg='#d9d9d9', 
font=('Calibre', 10), width=13, height=1, activebackground='#c5a8b0', command=resposta)
button.place(relx=0.59, rely=0.09, relheight=0.04, relwidth=0.08)
# resposta(p1, 0), resposta(p2, 5), resposta(p3, 10), resposta(p4, 15), resposta(p5, 20)

# Botão para enviar notas para o banco de dados
button1=Button(master=frm_main, text='Enviar Avaliação', fg='#1a1d1a', bg='#d9d9d9', 
font=('Calibre', 10), width=13, height=1, activebackground='#c5a8b0', command=(enviar_notas, enviar_retorno))
button1.place(relx=0.69, rely=0.09, relheight=0.04, relwidth=0.08)

window.mainloop()