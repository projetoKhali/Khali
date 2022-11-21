from tkinter import Frame, Label, Button, Text, Scale, IntVar, messagebox
from Models.Role import get_role_name
from Authentication import CURRENT_USER
from CSV.CSVHandler import *
from Front.Core import *

# Informações do modulo
NAME = 'Avaliar'
REQUIRED_PERMISSIONS_REG  = [None]
REQUIRED_PERMISSIONS_RATE = [
    [3, 4, 5]
]
REQUIRED_PERMISSIONS_VIEW = [None]

# executa o modulo e retorna
def run(frame_parent, to_user_id):
    from Front.Scrollbar import add_scrollbar

    module_frame = Frame(frame_parent, bg=co0, bd=3)
    module_frame.rowconfigure(1, weight=1)
    module_frame.columnconfigure(0, weight=1)
    module_frame.grid(row=0, column=0, sticky='news')

    frame_header = Frame(module_frame, bg=co3, bd=3)
    frame_header.grid(row= 0, column=0, sticky='ew')
    frame_header.columnconfigure(0, weight=1)

    # Textos gerais da tela
    criar_label(frame_header, 'Autoavaliação' if to_user_id == CURRENT_USER.id else 'Avaliação', 'Calibri, 30', 0, 0, co3, 'w').config(fg=co0)

    #rating_send_success
    from Events import trigger, register, unregister_all

    frame_send_btn = Frame(frame_header, bg=co3)
    frame_send_btn.grid(row= 0, column=2, sticky='ew')
    frame_send_btn.columnconfigure(0, weight=1)

    def update_send_btn (fsb, state):
        fsb_children = fsb.winfo_children()
        if fsb_children and len(fsb_children) > 0 and fsb_children[0] is not None:
            fsb_children[0].destroy()

        frame_button_wrapper = Frame(fsb, bg=co3, bd=0)
        frame_button_wrapper.grid(row= 0, column=0, sticky='ew')
        frame_button_wrapper.columnconfigure(0, weight=1)

        confirm_btn = Button(master=frame_button_wrapper, fg='#1a1d1a', bg='#d9d9d9', 
            font='Calibri, 14', height=0, activebackground='#c5a8b0', 
            text='Fechar' if state == 1 else 'Enviar Avaliação', 
            # state='disabled' if state == 2 else 'active',
            command=(lambda m=module_frame: fechar_avaliação(m)) if state == 1 else (lambda: enviar_notas(to_user_id))
        )
        confirm_btn.grid(row=0, column=0, sticky='e')
        if state == 1: criar_label(frame_button_wrapper, 'Avaliação enviada com sucesso!', 'Calibri, 10 bold', 1, 0).config(fg='green')
        elif state == 2: 
            for error_message in trigger('get_error_messages'):
                criar_label(frame_button_wrapper, error_message*(2-i), 'Calibri, 10 bold', i+1, 0).config(fg='red')

    update_send_btn(frame_send_btn, 0)

    register('rating_send_success', lambda fsb=frame_send_btn: update_send_btn(fsb, 1))
    register('rating_send_error', lambda fsb=frame_send_btn: update_send_btn(fsb, 2))

    frame_body = Frame(module_frame, bg=co0, bd=0)
    frame_body.columnconfigure(0, weight=1)
    frame_body.rowconfigure(0, weight=1)
    frame_body.grid(row= 1, column=0, sticky='news')
    frame_body = add_scrollbar(frame_body, bd=0)
    frame_body.rowconfigure(0, weight=2)
    frame_body.rowconfigure(1, weight=2)
    
    from CSV.CSVHandler import find_data_by_id_csv
    from Settings import USERS_PATH
    to_user_name = CURRENT_USER.name if to_user_id == CURRENT_USER.id else find_data_by_id_csv(USERS_PATH, str(to_user_id))['name']

    frame_summary = Frame(frame_body, bg=co1, padx=8, pady=8)
    frame_summary.grid(row= 0, column=0, sticky='ew')
    frame_summary.columnconfigure(0, weight=1)

    frame_user_data = Frame(frame_summary, bg=co1, padx=8, pady=8)
    frame_user_data.grid(row=0, column=0, sticky='ew')

    criar_label(frame_user_data, f'{to_user_name}\t', 'Calibri, 20', 0, 0, co1, 'w')
    criar_label(frame_user_data, get_role_name(CURRENT_USER.role_id), 'Calibri, 12', 1, 0, co1, 'w')
    criar_label(frame_summary, 'Esta avaliação 360° utiliza a escala Likert para medir o desempenho dos usuários. Notas abaixo ou iguais a 3 necessitam obrigatoriamente de Feedback (resposta descritiva)',
        'Calibri, 11', 0, 1, co1, 'w').config(wraplength=600) 

    # from Models.Sprint import sprint_index, current_rating_period
    # criar_label(frame_user_data, f'Prazo para realizar a autoavaliação da Sprint {sprint_index(CURRENT_USER.group_id, current_rating_period(CURRENT_USER.group_id).id)}', 'Calibri, 15', 2, 0, None, 'w')  # PUXAR DADO VINCULADO COM TELA DE RETORNO ???

    perguntas = [
        '1) Como você se avalia em trabalho em equipe, cooperação e descentralização de conhecimento?',
        '2) Como você se avalia em iniciativa e proatividade?',
        '3) Como você se avalia em autodidaxia e agregação de conhecimento ao grupo?',
        '4) Como você se avalia em entrega de resultados e participação efetiva no projeto?',
        '5) Como você se avalia em competência técnica?'
    ] if to_user_id == CURRENT_USER.id else [
        '1) Como você avalia o integrante em trabalho em equipe, cooperação e descentralização de conhecimento?',
        '2) Como você avalia o integrante em iniciativa e proatividade?',
        '3) Como você avalia o integrante em autodidaxia e agregação de conhecimento ao grupo?',
        '4) Como você avalia o integrante em entrega de resultados e participação efetiva no projeto?',
        '5) Como você avalia o integrante em competência técnica?'
    ]

    frame_criterias = Frame(frame_body, bg=co0, bd=3, padx=12, pady=4)
    frame_criterias.columnconfigure(0, weight=1)
    frame_criterias.rowconfigure([i for i in range(5)], weight=1)
    frame_criterias.grid(row=1, column=0, sticky='ew')
    
    from Models.id_criteria import criteria

    for i, c in enumerate(criteria):

        frame_criteria = Frame(frame_criterias, bg=co0, relief='groove', bd=3, pady=4)
        frame_criteria.grid(row= i, column=0, columnspan=2, sticky='nsew')
        frame_criteria.columnconfigure(0, weight=1)

        criar_label(frame_criteria, perguntas[i], 'Calibri, 10', 0, 0, co0, 'w')

        frame_slider_wrapper = Frame(frame_criteria, bg=co0, padx=64, pady=16)
        frame_slider_wrapper.grid(row=1, column=0, sticky='nsew')
        frame_slider_wrapper.columnconfigure(0, weight=1)

        frame_criteria_data = Frame(frame_slider_wrapper, bg=co0)
        frame_criteria_data.grid(row=0, column=0, sticky='nsew')
        frame_criteria_data.columnconfigure([i for i in range(4)], weight=1)

        for g_index, grade in enumerate(['Péssimo (1)', 'Ruim (2)', 'Regular (3)', 'Bom (4)', 'Ótimo (5)']):
            criar_label(frame_criteria_data, grade, 'Calibri, 10', 0, g_index, co0, 'w').config(width=0)
        
        frame_slider = Frame(frame_slider_wrapper, bg=co0)
        frame_slider.grid(row=1, column=0, sticky='nsew')
        frame_slider.columnconfigure(0, weight=1)

        frame_feedback = Frame(frame_criteria, bg=co0)
        frame_feedback.grid(row=3, column=0, sticky='nsew')
        frame_feedback.columnconfigure(0, weight=1)

        var = IntVar(value=5)
        
        unregister_all(f'get_value_criterio_{c}')
        register(f'get_value_criterio_{c}', lambda v=var: v.get())

        _escala = Scale(frame_slider, from_=1, to=5, tickinterval=0, orient='horizontal', showvalue=0,
            bg=co0, font='Calibri, 10 bold', highlightcolor='#c5a8b0', troughcolor='#c5a8b0', variable=var,
            command=lambda v, ff=frame_feedback, c=c: slider_change_position(ff, int(v), c)
        )
        _escala.grid(column=0, row=0, sticky='ews')

    f = Frame(frame_body, pady=100, bg=co0)
    Label(f, text='', bg=co0).grid(row=0, column=0, sticky="s")
    f.grid(row=100, column=0, sticky="s")


# def criar_label(master, text, tamanho, column, row, padx, pady,None,  sticky):
def slider_change_position(frame_feedback, new_value, criterio):
    ff_children = frame_feedback.winfo_children()
    if ff_children and len(ff_children) > 0 and ff_children[0] is not None:
        ff_children[0].destroy()

    from Events import register, unregister_all
    unregister_all(f'get_feedback_criterio_{criterio}')

    if new_value > 3: return

    frame_text_input = Frame(frame_feedback, bg=co0, padx=4)
    frame_text_input.grid(row= 0, column=0, sticky='nsew')
    frame_text_input.columnconfigure(0, weight=1)
    frame_text_input.rowconfigure(0, weight=1)

    criar_label(frame_text_input, f'Deixe um feedback para o critério {criterio}:* ', 'Calibri, 10', 0, 0, co0, 'we')
    
    text_input = Text(master=frame_text_input, height=5, font = 'Calibri, 10', bd=4)
    text_input.grid(row=1, column=0, sticky = 'news')

    register(f'get_feedback_criterio_{criterio}', lambda t=text_input: t.get('1.0', 'end')[:-2])


def enviar_notas(_to_user_id):
    from Utils.back_avaliacao import dados_avaliacao
    from Models.id_criteria import criteria, criteria_full

    notas = [0 for _ in criteria_full]
    comentarios = [0 for _ in criteria_full]

    print(notas)
    print(comentarios)

    from Events import trigger, register, unregister_all

    for i, c in enumerate(criteria):
        notas[i] = trigger(f'get_value_criterio_{c}')
        comentarios[i] = trigger(f'get_feedback_criterio_{c}')

    print(notas)
    print(comentarios)

    FEEDBACK_LEN_MINMAX = [0, 400]
    
    error_messages = []
    error_message_templates = lambda i, c: [
        f'Insira um feedback obrigatório para o critério {c}',
        f'Feedback do critério {c} é muito curto! Escreva pelo menos {FEEDBACK_LEN_MINMAX[0]} caracteres',
        f'Feedback do critério {c} é muito longo! Escreva no máximo {FEEDBACK_LEN_MINMAX[0]} caracteres'
    ][i]

    for i, criterio in enumerate(criteria_full):
        if notas[i] <= 3:
            if comentarios[i] is None or comentarios[i] == '': error_messages.append(error_message_templates(0, criterio))
            elif len(comentarios[i]) < FEEDBACK_LEN_MINMAX[0]: error_messages.append(error_message_templates(1, criterio))
            elif len(comentarios[i]) > FEEDBACK_LEN_MINMAX[1]: error_messages.append(error_message_templates(2, criterio))


    if len(error_messages) > 0: 
        for i in error_messages:
            print(i)

        unregister_all('get_error_messages')
        register('get_error_messages', lambda: error_messages)
        trigger('rating_send_error')
        return error_messages

    dados_avaliacao(_to_user_id, notas, comentarios)

    trigger('rating_send_success')
    return True

def fechar_avaliação(m):
    from Events import trigger
    m.destroy()
    trigger('sub_module_close')