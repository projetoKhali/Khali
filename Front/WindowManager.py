from .Windows import home_front, login_front

# O estado atual do WindowManager corresponde a qual janela dentro da lista STATES deve estar aberta
CURRENT_STATE = 0

# Armazena uma função de janela 
STATES = [

    # Default:      # Ao iniciar o programa, a janela de index 0 será iniciada
    login_front,    # 0

    # Redirects:    # Ao alterar o estado do WindowManager, a janela correspondente ao index será chamada
    home_front,     # 1

]

# Referencia para a janela aberta atualmente
CURRENT_WINDOW_INSTANCE = None

# Inicia o WindowManager
def initialize():

    # Inicia a janela correspondente ao estado 0
    set_state(0)

def set_state(new_state:int):
    global CURRENT_STATE
    
    # Se CURRENT_STATE é inválido, corrija mantendo CURRENT_STATE positivo menor que a quantidade de estados cadastrados
    CURRENT_STATE = 0 if new_state < 0 else ((new_state % len(STATES)) if new_state >= len(STATES) else new_state)

    launch()

# Seta CURRENT_STATE pra 0 para chamar a tela de login e deslogar usuário
def reset():
    CURRENT_STATE = 0
    set_state(0)

def next_state():
    set_state(CURRENT_STATE + 1)

# Inicia a janela correspondente ao estado atual (CURRENT_STATE) do WindowManager
def launch():
    global CURRENT_WINDOW_INSTANCE, STATES, CURRENT_STATE

    # Se a atual janela aberta não é nula, destrua
    if CURRENT_WINDOW_INSTANCE is not None:
        # print(f'CURRENT_WINDOW_INSTANCE \'{CURRENT_WINDOW_INSTANCE}\'')
        CURRENT_WINDOW_INSTANCE.destroy()

    CURRENT_WINDOW_INSTANCE = STATES[CURRENT_STATE].run()


def update():
    CURRENT_WINDOW_INSTANCE.mainloop()

