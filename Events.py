

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


# Remove uma reação de evento
def unregister(event, reaction):
    if event not in listeners: return
    if reaction in listeners[event]: listeners[event].remove(reaction)

# Executa o evento, chamando as funções de reação cadastradas
def trigger(event):
    results = []
    if event in listeners:
        for reaction in listeners[event]:
            result = reaction()
            if result is not None: results.append(result)
    return results
