def value_is_resolution (value):
    try:
        import re
        return re.match('\A[0-9]+x[0-9]+\Z', value)
    except:
        return False

def value_is_file (value):
    import re
    return re.match('.*?\.[\w]+\Z', value)

def value_is_function (value):
    return hasattr(value, '__call__')