import KMLFunctions

class Tag:
    def __init__(self, _type, _content):
        self.type = _type
        self.content = _content
    def run(self, parent):
        self.tk_obj = run_tag(self, parent)
        for child_tag in [i for i in self._content if type(i) is Tag]:
            child_tag.run(self)

FUNCTION_MAP = [
    {'frame': (KMLFunctions.create_label, ['parent', 'text', 'r', 'c'])},
]

def get_function(type):
    try:
        function = FUNCTION_MAP[type]
    except:
        print(f"KML | ERRO: função não encontrada para a tag de tipo'{type}'")
    return function



def run_tag(tag, parent):
    function_data = get_function(tag.type)
    return function_data[0](parent, get_params(function_data[1], tag))

def get_params(fields, tag):
    params = []
    for field in fields:
        try:
            params.append(tag.content[field])
        except:
            continue
    return params







things = [1, 2, 3, 'a', 'b', 'c']
other_things = [thing for thing in things if type(thing) is int]





print(other_things)


# tag = Tag("label", "", "c")
# print(tag.type)
# print(tag.name)
# print(tag.content)
