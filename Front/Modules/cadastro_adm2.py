from Authentication import register
from Front.Core import *

# Informações do modulo
NAME = 'Cadastrar'
REQUIRED_PERMISSIONS_REG = [0, 1, 2]
REQUIRED_PERMISSIONS_RATE = [None]
REQUIRED_PERMISSIONS_VIEW = [None]

# executa o modulo e retorna
def run (frame_parent):

    # frame_parent.rowconfigure(0, weight = 1)
    # frame_parent.columnconfigure(0, weight = 1)

    module_frame = criar_frame(frame_parent, 0, 0)
    module_frame.columnconfigure(0, weight=1)
    module_frame.rowconfigure(1, weight=1)

    # cabeçalho
    frame_header = criar_frame(module_frame, 0, 0, 'ew', co3, co3, 0, 0, 0)
    frame_header.columnconfigure(0, weight=1)

    # titulo
    criar_label(frame_header, 'Cadastro de Grupos', 'Calibri, 24', 0, 0, co3, 'ew', 'center').config(fg=co0)

    from Front.Scrollbar import add_scrollbar

    frame_body = criar_frame(module_frame, 1, 0, 'news', co0, co0, 0, 0, 0)
    frame_body.columnconfigure(0, weight=1)
    frame_body.rowconfigure(0, weight=1)
    frame_body = add_scrollbar(frame_body, bd=0)
    frame_body.columnconfigure(0, weight=1)
    frame_body.rowconfigure(1, weight=1)

    frame_summary = criar_frame(frame_body, 0, 0, 'ew', co0, co0, 0, 0, 0)
    frame_summary.columnconfigure(0, weight=1)

    texts = [
        'Após inserir os dados do Líder do Grupo e Fake Client, clique no botão "Cadastrar" para salvar as informações e criar outro grupo.',
        'Uma senha gerada automaticamente será enviada para o e-mail de cada um dos integrantes ao final do cadastro.'
    ]

    for i, text in enumerate(texts):
        criar_label(frame_summary, text, 'Calibri, 12', i, 0, co1, 'ew', 'center').config(wraplength=750, padx=16, pady=2)

    frame_group_form = criar_frame(frame_body, 1, 0, 'news', co0, co0, 0, 0, 0)
    frame_group_form.columnconfigure(0, weight=1)

    frame_group_form_header = criar_frame(frame_group_form, 0, 0, 'ew', co0, co0, 0, 0, 0)

    frame_group_form_title = criar_frame(frame_group_form_header, 1, 0, 'ew', co0, co0, 0, 0, 0)
    criar_label(frame_group_form_title, 'Nome do Grupo: ', 'Calibri, 12', 0, 0, sticky='w').config(width=20)
    criar_entry(frame_group_form_title, 'Calibri, 12', 0, 1, 'ew')

    frame_users_form = criar_frame(frame_group_form, 1, 0, 'ew', co1, co1, 0, 2, 2)

    for i, role in enumerate(['Líder do Grupo', 'Fake Client']):
        criar_label(frame_users_form, f'Nome do {role}: ', 'Calibri, 12', i, 0, co1, sticky='w').config(width=22)
        entry_name = criar_entry(frame_users_form, 'Calibri, 12', i, 1)
        criar_label(frame_users_form, f'Email do {role}: ', 'Calibri, 12', i, 2, co1, sticky='w').config(width=26)
        entry_email = criar_entry(frame_users_form, 'Calibri, 12', i, 3)

    return module_frame

    # Frame do cadastro de grupos
    frm_grupo=Frame(master=module_frame, relief=GROOVE, bd=3, bg=co0)
    frm_grupo.rowconfigure([0, 1], weight=1, minsize=30) 
    frm_grupo.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
    frm_grupo.place(relx=0.02, rely=0.22, relwidth=0.96, relheight=0.2)

    #   Frame da tabela de valores cadastrados
    frm_tabela=Frame(master=module_frame, relief=GROOVE, bd=1, bg=co0)
    frm_tabela.rowconfigure(0, weight=1, minsize=100) 
    frm_tabela.columnconfigure(0, weight=1, minsize=100)
    frm_tabela.place(relx=0.02, rely=0.45, relwidth=0.96, relheight=0.5)

    # Widgets de entrada
    ent_lider=Entry(master=frm_grupo, width=30, fg=co2, font='Calibri 13')  # Nome Líder
    ent_lider.grid(row=0, column=1, padx=5)

    ent_lemail=Entry(master=frm_grupo, width=30, fg=co2, font='Calibri 13')  # E-mail Líder
    ent_lemail.grid(row=0, column=3, padx=5)

    ent_client=Entry(master=frm_grupo, width=30, fg=co2, font='Calibri 13')  # Nome Client
    ent_client.grid(row=1, column=1, padx=5)

    ent_cemail=Entry(master=frm_grupo, width=30, fg=co2, font='Calibri 13')  # E-mail Client
    ent_cemail.grid(row=1, column=3, padx=5)

    widgetlabel('lbl_lider', 0, 0, 'Nome do Líder do Grupo:')  # Widget de texto nome Líder do Grupo
    widgetlabel('lbl_lemail', 0, 2, 'E-mail do Líder do Grupo:')  # Widget de texto e-mail Líder do Grupo
    widgetlabel('lbl_client', 1, 0, 'Nome do Fake Client:') # Widget de texto nome Fake Client
    widgetlabel('lbl_cemail', 1, 2, 'E-mail do Fake Client:')  # Widget de texto e-mail Fake Client

    criarbotao('button_grupo', 'Cadastrar', criar_grupo, 0)
    criarbotao('button_home', 'Home', 0, 1)

    # Tabela gerada com dados cadastrados pelo Administrador
    tree=ttk.Treeview(master=frm_tabela, selectmode='browse',
        column=('codigogrupo', 'nomelider', 'emaillider', 'nomeclient', 'emailclient'),
        show="headings")

    scroll_tree = ttk.Scrollbar(frm_tabela, orient='vertical', command=tree.yview) # Comando xview para orientação HORIZONTAL
    scroll_tree.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scroll_tree.set) # xscrollcomand para barra horizontal
    tree.bind('<Configure>', lambda e: tree.configure(scrollregion=tree.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar
    
    criartabela('codigogrupo', '#1', 'Código do grupo')
    criartabela('nomelider', '#2', 'Nome do Líder do Grupo')
    criartabela('emaillider', '#3', 'E-mail do Líder do Grupo')
    criartabela('nomeclient', '#4', 'Nome do Fake Client')
    criartabela('emailclient', '#5', 'E-mail do Fake Client')

    return module_frame


# Criação da função que recolhe informações cadastradas e gera código do grupo
def criar_grupo():

    # acessa as informações do lider
    nome_lider = ent_lider.get()
    email_lider = ent_lemail.get()

    # acessa as informações do cliente
    nome_client = ent_client.get()
    email_client = ent_cemail.get()

    # criando uma condição que lê o input do usuário impedindo o programa de criar um registro vazio
    if len(nome_lider) == 0 or len(email_lider) == 0 or len(nome_client) == 0 or len(email_client) == 0:
        import tkinter
        tkinter.messagebox.showinfo("Khali Group",  "Valores nulos. Por favor, preencher corretamente")
        return
        
    # para a aplicação sempre que o email do lider e do cliente forem iguais
    if email_lider == email_client:
        tkinter.messagebox.showinfo("Khali Group", "Emails são iguais!! Por favor, insira emails diferentes")
        return
    
    from Models.Group import create_group


    group_id = create_group(
        group_name,
        register(nome_lider, email_lider, None, None, 1),
        register(nome_client, email_client, None, None, 2)
    )

    tree.insert('', 'end', values=[codigo_str, nome_lider, email_lider, nome_client, email_client])
    tree.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)


