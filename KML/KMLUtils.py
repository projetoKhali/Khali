def value_is_resolution (value):
    import re
    return re.match('\A[0-9]+x[0-9]+\Z', value)

def value_is_function (value):
    return hasattr(value, '__call__')