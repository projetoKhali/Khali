


def recursive(mlen:int, s:str, chars:list[str], lst:list[str] = []):
    newlst = []
    for c in chars:
        if c is not None and c not in s: 
            if s+c != '' and s+c not in lst: 
                newlst += [s+c] + recursive(mlen-1, s+c, chars if None in chars else [None] + chars, lst) if mlen > 1 else [s+c]
    return newlst


sticky_values:list[str] = recursive(4, '', ['n', 'e', 'w', 's'])


def value_is_color (value):
    from Settings import CORES
    return value in ['white','black','red','green','blue','cyan','yellow','magenta',].extend(CORES) or (type(value) is str and value[0] == '#')

def value_is_resolution (value):
    import re
    return re.match('\A[0-9]+x[0-9]+\Z', value)

def value_is_function (value):
    return hasattr(value, '__call__')