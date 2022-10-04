from tkinter import * 
from tkinter import ttk

# Configurações da janela
window = Tk() 
window.configure(bg='#fae8e8')  # Cor do plano de fundo da tela
window.geometry("1200x600")
window.title('Sistema de Cadastro - Administrador')  # Título da janela

# Criar um frame para comportar o canvas
frm_main=Frame(window, bg='#fae8e8')
frm_main.pack(fill=BOTH, expand=1) 

# O canvas aceita o scrollbar, mas ela só faz o papel da responsividade
canvas=Canvas(frm_main, bg='#fae8e8')
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Configurações do scrollbar
scrollbar_ver = ttk.Scrollbar(frm_main, orient=VERTICAL, command=canvas.yview) # Comando xview para orientação HORIZONTAL
scrollbar_ver.pack(side=RIGHT, fill=Y)
scrollbar_hor = ttk.Scrollbar(frm_main, orient=HORIZONTAL, command=canvas.xview) # Comando xview para orientação HORIZONTAL
scrollbar_hor.pack(side=BOTTOM, fill=X)

# Configurações do canvas
canvas.configure(yscrollcommand=scrollbar_ver.set, xscrollcommand=scrollbar_hor.set) # xscrollcomand para barra horizontal
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar

frm_geral=Frame(canvas, bg='#fae8e8', relief=FLAT, bd=3) # Não colocamos o frame com o .pack nesse caso

# Integração do frame geral a uma janela do canvas
canvas.create_window((0,0), window=frm_geral, anchor='nw')

# Criação de um frame para as questões da avaliação
frm_avaliacao=Frame(frm_geral, bg='#fae8e8', relief=FLAT, bd=3)
frm_avaliacao.grid(row=4, column=0, columnspan=3, sticky='w') # O label do prazo está muito afastado, aumentei o columnspan para aproximar

# Função para criação de texto
def criar_label(master, text, tamanho, column, row, padx, pady, sticky):
    label=Label(master=master, text=text
    , bg='#fae8e8', font=('Calibre', tamanho))
    label.grid(column=column, row=row, padx=padx, pady=pady, sticky=sticky)

def criar_entrada(master, row, column, padx, pady, sticky):
    feedback=Entry(master=master, width=80, fg='#1a1d1a', font=('Calibre 13'))  # Nome Líder
    feedback.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)

# Função para criação de escalas
def criar_escala(master, row, padx, pady):
    escala = Scale(master=master, from_=1, to=5, length=500, tickinterval=1, orient=HORIZONTAL, 
    bg='#fae8e8', font='Calibre, 10', highlightcolor='#c5a8b0', troughcolor='#c5a8b0', state='normal')
    escala.grid(column=0, row=row, padx=padx, pady=pady, sticky='w')
    def resposta():
        if escala.get() <= 3:
            criar_label(frm_avaliacao, 'Feedback obrigatório: ', 13, 1, row, 2, 0, 'e')
            criar_entrada(frm_avaliacao, row, 2, 1, 0, 'w')
    nome=Button(master=frm_avaliacao, text='Enviar', fg='#1a1d1a', bg='#d9d9d9', 
    font=('Calibre', 15), width=10, height=1, activebackground='#c5a8b0', command=resposta)
    nome.grid(row=28, column=1, padx=5, pady=5, sticky='w')

p1 = criar_escala(frm_avaliacao, 6, 30, 2)
p2 = criar_escala(frm_avaliacao, 9, 30, 2)
p3 = criar_escala(frm_avaliacao, 12, 30, 2)
p4 = criar_escala(frm_avaliacao, 15, 30, 2)
p5 = criar_escala(frm_avaliacao, 18, 30, 2)
p6 = criar_escala(frm_avaliacao, 21, 30, 2)
p7 = criar_escala(frm_avaliacao, 24, 30, 2)
p8 = criar_escala(frm_avaliacao, 27, 30, 2)

# variable with integer values only
var = IntVar()

# Textos gerais da tela
criar_label(frm_geral, 'Autoavaliação', 30, 0, 0, 30, 30, 'w')
criar_label(frm_geral, 'Nome do usuário', 20, 0, 1, 30, 0, 'w')  
criar_label(frm_geral, 'Prazo para realizar a autoavaliação da {nº da Sprint}', 15, 0, 2, 30, 20, 'w')
criar_label(frm_geral, 'Breve explicação sobre a avaliação: Falar sobre a escala Likert e dos feedbacks obrigatórios para notas abaixo ou iguais a 3',
10, 0, 3, 30, 30, 'w')  

# Textos das questões da avaliação
criar_label(frm_avaliacao, 'Primeira questão', 15, 0, 4, 30, 5, 'w')
criar_label(frm_avaliacao, 'Segunda questão', 15, 0, 7, 30, 5, 'w')
criar_label(frm_avaliacao, 'Terceira questão', 15, 0, 10, 30, 5, 'w')
criar_label(frm_avaliacao, 'Quarta questão', 15, 0, 13, 30, 5, 'w') 
criar_label(frm_avaliacao, 'Quinta questão', 15, 0, 16, 30, 5, 'w')
criar_label(frm_avaliacao, 'Sexta questão', 15, 0, 19, 30, 5, 'w')
criar_label(frm_avaliacao, 'Sétima questão', 15, 0, 22, 30, 5, 'w')  
criar_label(frm_avaliacao, 'Oitava questão', 15, 0, 25, 30, 5, 'w')

# Descrição da tabela
criar_label(frm_avaliacao, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 5, 30, 0, 'w')
criar_label(frm_avaliacao, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 8, 30, 0, 'w')
criar_label(frm_avaliacao, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 11, 30, 0, 'w')
criar_label(frm_avaliacao, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 14, 30, 0, 'w') 
criar_label(frm_avaliacao, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 17, 30, 0, 'w')
criar_label(frm_avaliacao, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 20, 30, 0, 'w')
criar_label(frm_avaliacao, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 23, 30, 0, 'w')  
criar_label(frm_avaliacao, 'Péssimo (1)           Ruim (2)              Regular (3)                Bom (4)               Ótimo (5)', 10, 0, 26, 30, 0, 'w')


window.mainloop()