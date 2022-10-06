# Importar bibliotecas
from asyncio.windows_events import NULL
import email
import tkinter as tk
from tkinter import Frame, ttk
from tkinter import END
from tkinter.messagebox import NO, YES
from CSV.CSVHandler import find_data_list_by_field_value_csv
from Users.Authentication import find_data_csv, register
import Settings as settings

# Informações do modulo
NAME = 'Cadastrar'
REQUIRED_PERMISSIONS_REG = [0, 1, 2]        
REQUIRED_PERMISSIONS_RATE = [None]
REQUIRED_PERMISSIONS_VIEW = [None]

# armazena o numero do grupo durante o cadastro
grupo_num = 0

# executa o modulo e retorna
def run (frame_parent):

    frame_parent.grid_rowconfigure(0, weight = 1)
    frame_parent.grid_columnconfigure(0, weight = 1)

    window=Frame(frame_parent)  # Criar uma janela e instanciar a classe
    # window.configure(background="green")
    window.grid(row=0, column=0, sticky="nsew")
    window.configure(bg='#fae8e8')  # Cor do plano de fundo da tela

    # Criação da função que recolhe informações cadastradas e gera código do grupo
    def criar_grupo():

        # acessa as informações do lider
        nome_lider = ent_lider.get()
        email_lider = ent_lemail.get()

        # acessa as informações do cliente
        nome_client = ent_client.get()
        email_client = ent_cemail.get()

        # criando uma condição que lê o input do usuário impedindo o programa de criar um registro vazio
        if len(nome_lider) == 0  or len(email_lider) == 0  or len(nome_client) == 0  or len(email_client) == 0:
            print("valores nulos, por favor inserir dados válidos.")
            return
        # para a aplicação sempre que o email do lider e do cliente forem iguais
        if email_lider == email_client:
            print("emails são iguais!!! por favor, insira emails diferentes")
            return
        
        from Models.Groups import create_group

        # TODO: codigo_str -> group_name
        # criar label e entry para definir o nome do grupo a ser criado
        global grupo_num
        grupo_num += 1
        codigo_str = f'GRUPO-{grupo_num}'

        group_id = create_group(codigo_str)

        register(nome_lider, email_lider, group_id, None, 1)
        register(nome_client, email_client, group_id, None, 2)

        tree.insert('', END, values=[codigo_str, nome_lider, email_lider, nome_client, email_client])
        tree.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    # window.configure(bg='#fae8e8')  # Cor do plano de fundo da tela
    # window.geometry("1200x600")
    # window.title('Sistema de Cadastro - Administrador')  # Título da janela

    def textojanela(tipo, texto, tamanho, x, y, largura, altura):
        tipo=tk.Label(master=window,
        text=texto, fg='#1a1d1a', bg='#fae8e8', font=('Calibre', tamanho))
        tipo.place(relx=x, rely=y, relwidth=largura, relheight=altura)

    textojanela('lbl_titulo', 'Cadastro de Grupos', 30, 0.02, 0.01, 0.96, 0.09)
    textojanela('lbl_desc', 
        'Após inserir os dados do Líder do Grupo e Fake Client, clique no botão "Cadastrar" para salvar as informações e criar outro grupo.', 
        13, 0.02, 0.1, 0.96, 0.06)  
    textojanela('lbl_senha', 
        'Uma senha gerada automaticamente será enviada para o e-mail de cada um dos integrantes ao final do cadastro.', 
        13, 0.02, 0.17, 0.96, 0.04)

    # Frame do cadastro de grupos
    frm_grupo=tk.Frame(master=window, relief=tk.GROOVE, bd=3, bg='#fae8e8')
    frm_grupo.rowconfigure([0, 1], weight=1, minsize=30) 
    frm_grupo.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
    frm_grupo.place(relx=0.02, rely=0.22, relwidth=0.96, relheight=0.2)

    #   Frame da tabela de valores cadastrados
    frm_tabela=tk.Frame(master=window, relief=tk.GROOVE, bd=1, bg='#fae8e8')
    frm_tabela.rowconfigure(0, weight=1, minsize=100) 
    frm_tabela.columnconfigure(0, weight=1, minsize=100)
    frm_tabela.place(relx=0.02, rely=0.45, relwidth=0.96, relheight=0.5)

    # Widgets de entrada
    ent_lider=tk.Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # Nome Líder
    ent_lider.grid(row=0, column=1, padx=5)

    ent_lemail=tk.Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # E-mail Líder
    ent_lemail.grid(row=0, column=3, padx=5)

    ent_client=tk.Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # Nome Client
    ent_client.grid(row=1, column=1, padx=5)

    ent_cemail=tk.Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # E-mail Client
    ent_cemail.grid(row=1, column=3, padx=5)

    # Função para widget de texto
    def widgetlabel(usuario, linha, coluna, texto):
        usuario=tk.Label(master=frm_grupo, text=texto,
            fg='#1a1d1a', bg='#fae8e8', font=('Calibre', 13))
        usuario.grid(row=linha, column=coluna, sticky='e')

    widgetlabel('lbl_lider', 0, 0, 'Nome do Líder do Grupo:')  # Widget de texto nome Líder do Grupo
    widgetlabel('lbl_lemail', 0, 2, 'E-mail do Líder do Grupo:')  # Widget de texto e-mail Líder do Grupo
    widgetlabel('lbl_client', 1, 0, 'Nome do Fake Client:') # Widget de texto nome Fake Client
    widgetlabel('lbl_cemail', 1, 2, 'E-mail do Fake Client:')  # Widget de texto e-mail Fake Client

    def criarbotao(nome, texto, comando, linha):
        nome=tk.Button(master=frm_grupo, text=texto, 
        fg='#1a1d1a', bg='#d9d9d9', font=('Calibre', 13),
        width=10, height=1, activebackground='#c5a8b0',
        command=comando)
        nome.grid(row=linha, column=4, padx=20)
    criarbotao('button_grupo', 'Cadastrar', criar_grupo, 0)
    criarbotao('button_home', 'Home', 0, 1)

    # Tabela gerada com dados cadastrados pelo Administrador
    tree=ttk.Treeview(master=frm_tabela, selectmode='browse',
        column=('codigogrupo', 'nomelider', 'emaillider', 'nomeclient', 'emailclient'),
        show="headings")

    scroll_tree = ttk.Scrollbar(frm_tabela, orient=tk.VERTICAL, command=tree.yview) # Comando xview para orientação HORIZONTAL
    scroll_tree.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scroll_tree.set) # xscrollcomand para barra horizontal
    tree.bind('<Configure>', lambda e: tree.configure(scrollregion=tree.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar

    def criartabela(coluna, número, texto): 
        tree.column(coluna, width=200, minwidth=50, stretch=YES)
        tree.heading(número, text=texto)
    
    criartabela('codigogrupo', '#1', 'Código do grupo')
    criartabela('nomelider', '#2', 'Nome do Líder do Grupo')
    criartabela('emaillider', '#3', 'E-mail do Líder do Grupo')
    criartabela('nomeclient', '#4', 'Nome do Fake Client')
    criartabela('emailclient', '#5', 'E-mail do Fake Client')

    return window


