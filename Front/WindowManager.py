from .Windows import home_front, login_front

# O estado atual do WindowManager corresponde a qual janela dentro da lista STATES deve estar aberta
CURRENT_STATE = None

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
    global CURRENT_STATE
    CURRENT_STATE = 0
    set_state(0)

def next_state():
    if CURRENT_STATE is None: return
    set_state(CURRENT_STATE + 1)

# Inicia a janela correspondente ao estado atual (CURRENT_STATE) do WindowManager
def launch():
    global CURRENT_WINDOW_INSTANCE, STATES, CURRENT_STATE
    if CURRENT_STATE is None: return

    # Se a atual janela aberta não é nula, destrua
    if CURRENT_WINDOW_INSTANCE is not None:
        CURRENT_WINDOW_INSTANCE[0] = None
        CURRENT_WINDOW_INSTANCE[1].destroy()

    CURRENT_WINDOW_INSTANCE = [STATES[CURRENT_STATE], None]
    CURRENT_WINDOW_INSTANCE[1] = CURRENT_WINDOW_INSTANCE[0].run()


def update():
    if CURRENT_STATE is None: return
    def on_closing():
        from matplotlib import pyplot
        pyplot.close("all")
        CURRENT_WINDOW_INSTANCE[1].destroy()
    CURRENT_WINDOW_INSTANCE[1].protocol("WM_DELETE_WINDOW", on_closing)
    CURRENT_WINDOW_INSTANCE[1].mainloop()

def create_window (background):
    from tkinter import Tk

    # cria a janela
    window = Tk()
    window.title('')

    # tamanho padrão de janela
    window.minsize(1300, 670)  # tamanho da tela, largura x altura
    window.resizable(width=True, height=True)
    
    # janela maximizada
    window.state('zoomed')
    # janela.geometry("%dx%d+0+0" % (janela.winfo_screenwidth(), janela.winfo_screenheight()))

    # tentativa de dar numero de linhas e colunas para a tabela. Se deixo ativado, os labels ficam espalhados pela tela.
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)
    window.configure(background=background)

    return window

