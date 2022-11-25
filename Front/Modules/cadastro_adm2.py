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
    criar_label(frame_header, 'Gerenciamento de Grupos', 'Calibri, 24', 0, 0, co3, 'ew', 'center').config(fg=co0)

    from Front.Scrollbar import add_scrollbar

    frame_body = criar_frame(module_frame, 1, 0, 'news', co0, co0, 0, 0, 0)
    frame_body.columnconfigure(0, weight=1)
    frame_body.rowconfigure(0, weight=1)
    frame_body = add_scrollbar(frame_body, bd=0)
    frame_body.columnconfigure(0, weight=1)
    frame_body.rowconfigure(2, weight=1)

    frame_summary = criar_frame(frame_body, 0, 0, 'ew', co0, co0, 0, 0, 0)
    frame_summary.columnconfigure(0, weight=1)

    texts = [
        'Após inserir os dados do Líder do Grupo e Fake Client, clique no botão "Cadastrar" para salvar as informações e criar outro grupo.',
        'Uma senha gerada automaticamente será enviada para o e-mail de cada um dos integrantes ao final do cadastro.'
    ]

    for i, text in enumerate(texts):
        criar_label(frame_summary, text, 'Calibri, 12', i, 0, co1, 'ew', 'center').config(wraplength=750, padx=16, pady=2)

    frame_group_form = criar_frame(frame_body, 1, 0, 'news', co3, co3, 1, 8, 8)
    frame_group_form.columnconfigure(0, weight=1)

    frame_group_form_header = criar_frame(frame_group_form, 0, 0, 'ew', co3, co3, 0, 0, 0)
    frame_group_form_header.columnconfigure(0, weight=1)

    frame_group_form_title = criar_frame(frame_group_form_header, 0, 0, 'ew', co3, co3, 0, 4, 0)
    frame_group_form_title.columnconfigure(0, weight=1)
    criar_label(frame_group_form_title, 'Novo Grupo', 'Calibri, 12 bold', 0, 0, co3, 'w').config(fg=co0)
    criar_button(frame_group_form_title, 'Cadastrar', 'Calibri, 12 bold', 0, 1, cadastrar, 'e').config(takefocus = 0)

    frame_group_form_name = criar_frame(frame_group_form_header, 1, 0, 'ew', co0, co0, 0, 0, 0)
    frame_group_form_name.columnconfigure(2, weight=1)
    criar_label(frame_group_form_name, 'Nome do Grupo: ', 'Calibri, 12', 0, 0, sticky='w').config(width=22)

    from Events import trigger, register, unregister_all

    unregister_all('get_group_name')
    register('get_group_name', lambda e=criar_entry(frame_group_form_name, 'Calibri, 12', 0, 1, 'ew'): e.get())

    frame_users_form = criar_frame(frame_group_form, 1, 0, 'ew', co1, co1, 0, 0, 0)
    for role_index, role in enumerate(['Líder do Grupo', 'Fake Client']):

        criar_label(frame_users_form, f'Nome do {role}: ', 'Calibri, 12', role_index, 0, co1, sticky='w').config(width=22)
        unregister_all(f'get_{["LdG", "FC"][role_index]}_name')
        register(f'get_{["LdG", "FC"][role_index]}_name', lambda e=criar_entry(frame_users_form, 'Calibri, 12', role_index, 1): e.get())

        criar_label(frame_users_form, f'Email do {role}: ', 'Calibri, 12', role_index, 2, co1, sticky='w').config(width=26)
        unregister_all(f'get_{["LdG", "FC"][role_index]}_email')
        register(f'get_{["LdG", "FC"][role_index]}_email', lambda e=criar_entry(frame_users_form, 'Calibri, 12', role_index, 3): e.get())

    frame_table = criar_frame(frame_body, 2, 0, 'news', co3, co3, 1, 8, 8)
    frame_table.columnconfigure(0, weight=1)
    frame_table.rowconfigure(1, weight=1)

    frame_table_header = criar_frame(frame_table, 0, 0, 'ew', co3, None, 0, 4, 0)
    criar_label(frame_table_header, 'Grupos', 'Calibri, 12 bold', 0, 0, co3, 'w').config(fg=co1)

    frame_table_list = criar_frame(frame_table, 2, 0, 'news', co1, co1, 0, 0, 0)
    frame_table_list.columnconfigure(0, weight=1)
    frame_table_list.rowconfigure(0, weight=1)

    register('update_table', lambda ftl=frame_table_list: update_table(ftl))
    trigger('update_table')

    return module_frame


# atualiza a tabela
def update_table(frame_table):

    ft_children = frame_table.winfo_children()
    if ft_children is not None and len(ft_children) > 0 and ft_children[0] is not None:
        ft_children[0].destroy()

    from Models.Group import get_groups
    groups = get_groups()

    from Events import trigger, register, unregister_all
    from tkinter import StringVar

    frame_groups_parent = criar_frame(frame_table, 0, 0, 'news', co1, None, 0, 2, 2)
    for group_index, group in enumerate(groups):

        frame_group = criar_frame(frame_groups_parent, group_index, 0, 'ew', co1, co2, 1, 2, 2)
        frame_group.columnconfigure([i for i in range(3)], weight=1)
        var = StringVar()
        var.set(group.name)
        label_group_name = criar_label(frame_group, group.name, 'Calibri, 10', 0, 0, co1, 'w', width=40)
        label_group_name.bind("<Button-1>", 
            lambda _, lbl=label_group_name, fg=frame_group: 
            (lambda e: [
                e.config(highlightthickness=0, bd=0, background=co1, textvariable=var),
                e.bind(i, lambda: save(lbl, e), e.destroy()) for i in ['<Return>', '<FocusOut>', '<Escape>']
            ])(criar_entry(fg, 'Calibri, 10', 0, 0, 'ew', 4, 2, 'center'))
        )
        def save (label, entry):
            label.config(text=entry.get())

        """
        label - click -> create_entry
        entry - return, focusout, escape - save, update_label, delete_entry
        """

        # unregister_all(f'edit_group_{group.id}')
        # label_group_name.bind("<Button-1>", lambda _, group_id=group.id: trigger(f'edit_group_{group_id}'))

        from Models.Team import get_teams_of_group
        from Models.User import get_users_of_group

        criar_label(frame_group, f'Nº de Times: {len(get_teams_of_group(group.id))}', 'Calibri, 10', 0, 1, co1, 'w', width=20)
        criar_label(frame_group, f'Nº de Membros: {len(get_users_of_group(group.id))}', 'Calibri, 10', 0, 2, co1, 'w', width=20)

        criar_button(frame_group, 'Excluir', 'Calibri, 10', 0, 3, lambda group_id=group.id: excluir(group_id)).config(takefocus = 0)


# Criação da função que recolhe informações cadastradas e gera código do grupo
def cadastrar():
    from tkinter import messagebox
    from Events import trigger

    group_name = trigger('get_group_name')
    instructor_data = [[trigger(f'get_{["LdG", "FC"][i]}_name'), trigger(f'get_{["LdG", "FC"][i]}_email')] for i in range(2)]

    for role in instructor_data:
        for field in role:
            if len(field) == 0:
                messagebox.showinfo("Khali Group",  "Valores nulos. Por favor, preencher corretamente")
                return

    if instructor_data[0][1] == instructor_data[1][1]:
        messagebox.showinfo("Khali Group", "Emails são iguais!! Por favor, insira emails diferentes")
        return
    
    from Models.Group import create_group

    create_group(
        group_name,
        register(instructor_data[0][0], instructor_data[0][1], None, None, 1),
        register(instructor_data[1][0], instructor_data[1][1], None, None, 2)
    )

    trigger('update_table')


# exclui um grupo
def excluir(group_index):
    return

