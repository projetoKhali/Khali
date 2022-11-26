

# Dicionário onde estarão as funções de reação a eventos
listeners = {}


# inicializa o sistema de eventos
def initialize():
    from Front.WindowManager import next_state
    register('login', next_state)

# Registra uma função a ser chamada ao executar o evento especificado
def register(event, reaction):
    # print(f'Events.register -- event: {event} | reaction: {reaction}')
    if type(event) is list:
        print(f'events.register -- event is list!! {event}')
        for e in event:
            register(e, reaction)
        return reaction
    if event in listeners:
        listeners[event].append(reaction)
    else:
        listeners.update({event:[reaction]})
    return reaction    

# Remove uma reação de evento
def unregister(event, reaction):
    if event not in listeners: return
    if reaction in listeners[event]: 
        listeners[event].remove(reaction)
        if len(listeners[event]) == 0: listeners.pop(event)
    return reaction

def unregister_all(event):
    if event not in listeners: return
    listeners.pop(event)

# Executa o evento, chamando as funções de reação cadastradas
def trigger(event):
    results = []
    if event in listeners:
        print(event)
        for reaction in listeners[event]:
            result = reaction() if hasattr(reaction, '__call__') else reaction
            print(result)
            # print(f'Events.trigger -- event: {event} | rection: {reaction}')
            # print(f'result: {result}')
            if result is not None: results.append(result)
    return results if len(results) > 1 else results[0] if len(results) == 1 else None


# Retorna true caso existam reações cadastradas para o evento
def has_event(event):
    return event in listeners
