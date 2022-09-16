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
    codigo_str = "GRUPO-{}".format(grupo)
    tree.insert("", END, values=[codigo_str, nome_lider, email_lider, nome_client, email_client])
    tree.grid(row=0, column=0)
    confemaill()
    confemailc()

window.configure(bg="#fae8e8")  # Cor do plano de fundo da tela
window.title("Sistema de Cadastro - Administrador")  # Título da janela

# Título da página
lbl_titulo=tk.Label(master=window,
    text="Cadastro de Grupos",
    fg="#000000", bg="#fae8e8", font=('Calibre', 30))
lbl_titulo.grid(row=0, column=0, padx=30, pady=20)

# Widget de texto - descrição do cadastro
lbl_desc=tk.Label(
    master=window,
    text='Após inserir os dados do Líder do Grupo e Fake Client, clique no botão "Cadastrar" para salvar as informações e criar outro grupo.',
    fg="#000000", bg="#fae8e8", font=('Calibre', 15))
lbl_desc.grid(row=1, column=0, padx=30)

# Widget de texto - descrição do envio de senha
lbl_senha=tk.Label(
    master=window,
    text='Uma senha gerada automaticamente será enviada para o e-mail de cada um dos integrantes ao final do cadastro.',
    fg="#000000", bg="#fae8e8", font=('Calibre', 13))
lbl_senha.grid(row=2, column=0, padx=30)

# Frame do cadastro de grupos
frm_grupo=tk.Frame(master=window, relief=tk.GROOVE, bd=3,
    width=1000, height=100, bg="#fae8e8")
frm_grupo.rowconfigure([0, 1], weight=1, minsize=50) 
frm_grupo.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
frm_grupo.grid(row=3, column=0, padx=30, pady=30)

# Frame da tabela de valores cadastrados
frm_tabela=tk.Frame(master=window, relief=tk.FLAT, bd=1,
    width=100, height=100, bg="#fae8e8")
frm_tabela.rowconfigure(0, weight=1, minsize=100) 
frm_tabela.columnconfigure(0, weight=1, minsize=100)
frm_tabela.grid(row=4, column=0, padx=5, pady=5)

# Widget de texto - nome Líder do Grupo
lbl_lider=tk.Label(master=frm_grupo, text="Nome do Líder do Grupo:",
    fg="#000000", bg="#fae8e8", font=('Calibre', 15))
lbl_lider.grid(row=0, column=0, sticky="e")

# Widget de entrada - nome Líder do Grupo
ent_lider=tk.Entry(master=frm_grupo, width=30, fg="#000000", font=('Calibre 13'))
ent_lider.grid(row=0, column=1, padx=10)

# Widget de texto - e-mail Líder do Grupo
lbl_lemail=tk.Label(master=frm_grupo, text="E-mail do Líder do Grupo:",
    fg="#000000", bg="#fae8e8", font=('Calibre', 15))
lbl_lemail.grid(row=0, column=2, sticky="e")

# Widget de entrada - e-mail Líder do Grupo
ent_lemail=tk.Entry(master=frm_grupo, width=30, fg="#000000", font=('Calibre 13'))
ent_lemail.grid(row=0, column=3, padx=10)

# Widget de texto - nome Fake Client
lbl_client=tk.Label(master=frm_grupo, text="Nome do Fake Client:",
    fg="#000000", bg="#fae8e8", font=('Calibre', 15))
lbl_client.grid(row=1, column=0, sticky="e")

# Widget de entrada - nome Fake Client
ent_client=tk.Entry(master=frm_grupo, width=30, fg="#000000", font=('Calibre 13'))
ent_client.grid(row=1, column=1, padx=10)

# Widget de texto - e-mail Fake Client
lbl_cemail=tk.Label(master=frm_grupo, text="E-mail do Fake Client:",
    fg="#000000", bg="#fae8e8", font=('Calibre', 15))
lbl_cemail.grid(row=1, column=2, sticky="e")

# Widget de entrada - e-mail Fake Client
ent_cemail=tk.Entry(master=frm_grupo, width=30, fg="#000000", font=('Calibre 13'))
ent_cemail.grid(row=1, column=3, padx=10)

# Botão de cadastro
button_grupo=tk.Button(master=frm_grupo, text="Cadastrar", 
    fg="#000000", bg="#a6a6a6", font=('Calibre', 15),
    width=10, height=1, activebackground="#c5a8b0",
    command=criar_grupo)
button_grupo.grid(row=0, column=4, padx=20)

# Botão tela Home
button_home=tk.Button(master=frm_grupo, text="Home", 
    fg="#000000", bg="#a6a6a6", font=('Calibre', 15),
    width=10, height=1,
    activebackground="#c5a8b0")
button_home.grid(row=1, column=4, padx=20)

# Tabela gerada com dados cadastrados pelo Administrador
tree=ttk.Treeview(
    master=frm_tabela,
    selectmode="browse",
    column=("codigogrupo", "nomelider",
    "emaillider", "nomeclient", "emailclient"),
    show="headings")

tree.column("codigogrupo", width=100, minwidth=50, stretch=NO)
tree.heading("#1", text="Código do grupo")

tree.column("nomelider", width=200, minwidth=50, stretch=NO)
tree.heading("#2", text="Nome do Líder do Grupo")

tree.column("emaillider", width=200, minwidth=50, stretch=NO)
tree.heading("#3", text="E-mail do Líder do Grupo")

tree.column("nomeclient", width=200, minwidth=50, stretch=NO)
tree.heading("#4", text="Nome do Fake Client")

tree.column("emailclient", width=200, minwidth=50, stretch=NO)
tree.heading("#5", text="E-mail do Fake Client")

# Função envio de  e-mail Líder do Grupo
def confemaill():
    outlook = win32.Dispatch('outlook.application')  # Criar interação com outlook
    email = outlook.CreateItem(0)  # Criar um e-mail

    # Configurar as informações do e-mail
    nome_lider = ent_lider.get()
    email_lider = ent_lemail.get()
    email.To = email_lider
    email.Subject = 'E-mail automático - Senha cadastrada para Avaliação 360°'
    email.HTMLBody = f"""
    <p>Olá, {nome_lider}!</p>

    <p>Aqui está sua senha gerada automaticamente, para acesso à plataforma de Avaliação 360°:</p>
    <p>SENHA:</p>
    <p>E-MAIL CADASTRADO: {email_lider}</p>

    <p><b>Sua senha é intrasferível, não compartilhe com ninguém.</b></p>

    <p>Não responda a este e-mail.</p>
    """

    if str(object='@') in email_lider:
        email.Send()
        print("E-mail Enviado")
    else:
        print('não existe e-mail cadastrado')

# Função envio de e-mail Fake Client
def confemailc():
    outlook = win32.Dispatch('outlook.application')  # Criar interação com outlook
    email = outlook.CreateItem(0)  # Criar um e-mail

    # Configurar as informações do e-mail
    nome_client = ent_client.get()
    email_client = ent_cemail.get()
    email.To = email_client
    email.Subject = 'E-mail automático - Senha cadastrada para Avaliação 360°'
    email.HTMLBody = f"""
    <p>Olá, {nome_client}!</p>

    <p>Aqui está sua senha gerada automaticamente, para acesso à plataforma de Avaliação 360°:</p>
    <p>SENHA:</p>
    <p>E-MAIL CADASTRADO: {email_client}</p>

    <p><b>Sua senha é intrasferível, não compartilhe com ninguém.</b></p>

    <p>Não responda a este e-mail.</p>
    """

    if str(object='@') in email_client:
        email.Send()
        print("E-mail Enviado")
    else:
        print('não existe e-mail cadastrado')

window.mainloop()  # Método que executa eventos como cliques de botão e mantém a janela aberta