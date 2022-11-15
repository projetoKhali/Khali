

# Dicionário onde estarão as funções de reação a eventos
listeners = {}


# inicializa o sistema de eventos
def initialize():
    from Front.WindowManager import next_state
    register('login', next_state)


# Registra uma função a ser chamada ao executar o evento especificado
def register(event, reaction):
    if event in listeners:
        listeners[event].append(reaction)
    else:
        listeners.update({event:[reaction]})


# Executa o evento, chamando as funções de reação cadastradas
def trigger(event):
    if event in listeners:
        for r in listeners[event]:
            r()

