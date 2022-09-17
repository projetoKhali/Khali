# Importar bibliotecas
import tkinter as tk
from tkinter import ttk
from tkinter import END
from tkinter.messagebox import NO
from turtle import heading
import win32com.client as win32  # Biblioteca que possibilita a interagração com o e-mail

grupo = 0

window=tk.Tk()  # Criar uma janela e instanciar a classe

# Criação da função que recolhe informações cadastradas e gera código do grupo
def criar_grupo():
    nome_lider = ent_lider.get()
    email_lider = ent_lemail.get()
    nome_client = ent_client.get()
    email_client = ent_cemail.get()
    global grupo
    grupo += 1
    codigo_str = 'GRUPO-{}'.format(grupo)
    tree.insert('', END, values=[codigo_str, nome_lider, email_lider, nome_client, email_client])
    tree.grid(row=0, column=0)
    # Chamar função com os parâmetros "nome" e "email1"
    enviaremail(ent_lider.get(), ent_lemail.get())
    enviaremail(ent_client.get(), ent_cemail.get())

window.configure(bg='#fae8e8')  # Cor do plano de fundo da tela
window.title('Sistema de Cadastro - Administrador')  # Título da janela

def textojanela(tipo, texto, tamanho, linha, coluna, espaço):
    tipo=tk.Label(master=window,
    text=texto,
    fg='#1a1d1a', bg='#fae8e8', font=('Calibre', tamanho))
    tipo.grid(row=linha, column=coluna, padx=30, pady=espaço)

textojanela('lbl_titulo', 'Cadastro de Grupos', 30, 0, 0, 20)
textojanela('lbl_desc', 
    'Após inserir os dados do Líder do Grupo e Fake Client, clique no botão "Cadastrar" para salvar as informações e criar outro grupo.', 
    15, 1, 0, 0)  
textojanela('lbl_senha', 
    'Uma senha gerada automaticamente será enviada para o e-mail de cada um dos integrantes ao final do cadastro.', 
    13, 2, 0, 0)

# Frame do cadastro de grupos
frm_grupo=tk.Frame(master=window, relief=tk.GROOVE, bd=3,
    width=1000, height=100, bg='#fae8e8')
frm_grupo.rowconfigure([0, 1], weight=1, minsize=50) 
frm_grupo.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
frm_grupo.grid(row=3, column=0, padx=30, pady=30)

# Frame da tabela de valores cadastrados
frm_tabela=tk.Frame(master=window, relief=tk.FLAT, bd=1,
    width=100, height=100, bg='#fae8e8')
frm_tabela.rowconfigure(0, weight=1, minsize=100) 
frm_tabela.columnconfigure(0, weight=1, minsize=100)
frm_tabela.grid(row=4, column=0, padx=5, pady=5)

# Widgets de entrada
ent_lider=tk.Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # Nome Líder
ent_lider.grid(row=0, column=1, padx=10)

ent_lemail=tk.Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # E-mail Líder
ent_lemail.grid(row=0, column=3, padx=10)

ent_client=tk.Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # Nome Client
ent_client.grid(row=1, column=1, padx=10)

ent_cemail=tk.Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # E-mail Client
ent_cemail.grid(row=1, column=3, padx=10)

# Função para widget de texto
def widgetlabel(usuario, linha, coluna):
    usuario=tk.Label(master=frm_grupo, text='Nome do Líder do Grupo:',
        fg='#1a1d1a', bg='#fae8e8', font=('Calibre', 15))
    usuario.grid(row=linha, column=coluna, sticky='e')

widgetlabel('lbl_lider', 0, 0)  # Widget de texto nome Líder do Grupo
widgetlabel('lbl_lemail', 0, 2)  # Widget de texto e-mail Líder do Grupo
widgetlabel('lbl_client', 1, 0)  # Widget de texto nome Fake Client
widgetlabel('lbl_cemail', 1, 2)  # Widget de texto e-mail Fake Client

def criarbotao(nome, texto, comando, linha):
    nome=tk.Button(master=frm_grupo, text=texto, 
    fg='#1a1d1a', bg='#d9d9d9', font=('Calibre', 15),
    width=10, height=1, activebackground='#c5a8b0',
    command=comando)
    nome.grid(row=linha, column=4, padx=20)
criarbotao('button_grupo', 'Cadastrar', criar_grupo, 0)
criarbotao('button_home', 'Home', 0, 1)

# Tabela gerada com dados cadastrados pelo Administrador
tree=ttk.Treeview(master=frm_tabela, selectmode='browse',
    column=('codigogrupo', 'nomelider', 'emaillider', 'nomeclient', 'emailclient'),
    show="headings")

def criartabela(coluna, número, texto): 
    tree.column(coluna, width=200, minwidth=50, stretch=NO)
    tree.heading(número, text=texto)

criartabela('codigogrupo', '#1', 'Código do grupo')
criartabela('nomelider', '#2', 'Nome do Líder do Grupo')
criartabela('emaillider', '#3', 'E-mail do Líder do Grupo')
criartabela('nomeclient', '#4', 'Nome do Fake Client')
criartabela('emailclient', '#5', 'E-mail do Fake Client')

# Função envio de  e-mail Líder do Grupo e Fake Client
def enviaremail(nome, email1):
    outlook = win32.Dispatch('outlook.application')  # Criar interação com outlook
    email = outlook.CreateItem(0)  # Criar um e-mail

    # Configurar as informações do e-mail
    email.To = email1
    email.Subject = 'E-mail automático - Senha cadastrada para Avaliação 360°'
    email.HTMLBody = f"""
    <p>Olá, {nome}!</p>

    <p>Aqui está sua senha gerada automaticamente, para acesso à plataforma de Avaliação 360°:</p>
    <p>SENHA:</p>
    <p>E-MAIL CADASTRADO: {email1}</p>

    <p><b>Sua senha é intrasferível, não compartilhe com ninguém.</b></p>

    <p>Não responda a este e-mail.</p>
    """

    if str(object='@') in email1:
        email.Send()
        print(f'E-mail enviado para {nome}')
    else:
        print(f'Não existe e-mail cadastrado para {nome}')

window.mainloop()  # Método que executa eventos como cliques de botão e mantém a janela aberta