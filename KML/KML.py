from . import KMLFunctions
from Settings import COLS
from .KMLUtils import *

# Representa uma Tag que contem informações para a criação de um objeto tkinter
class Tag:
    def __init__(self, _type, *_content):
        self.type = _type
        self.content = _content
        self.id = [i for i in self.content if value_is_id(i)]
        # if self.id is not None:
        #     self.content.remove(self.id)
    def run(self, parent):
        print(COLS[7] + f'Tag.run() {self.type} {self.content} {type(self)}' + COLS[0])
        print(self.id)
        self.tk_obj = run_tag(self, parent)
        for child_tag in [i for i in self.content if type(i) is Tag or issubclass(type(i), Tag)]:
            child_tag.run(self.tk_obj)
        return self.tk_obj

class window (Tag):
    def __init__(self, *_content):
        super().__init__('window', *_content)
    def run(self):
        w = super().run(None)
        w.mainloop()
        return w

class module (Tag):
    def __init__(self, _name, _req_regi, _req_rate, _req_view, *_content):
        self.NAME = _name,
        self.REQUIRED_PERMISSIONS_REG = _req_regi
        self.REQUIRED_PERMISSIONS_RATE = _req_rate
        self.REQUIRED_PERMISSIONS_VIEW = _req_view
        super().__init__('module', *_content)

class frame (Tag):
    def __init__(self, *_content):
        super().__init__('frame', *_content)

class label (Tag):
    def __init__(self, *_content):
        super().__init__('label', *_content)

class entry (Tag):
    def __init__(self, *_content):
        super().__init__('entry', *_content)

class button (Tag):
    def __init__(self, *_content):
        super().__init__('button', *_content)

class img (Tag):
    def __init__(self, *_content):
        super().__init__('img', *_content)


class loop (Tag):
    list_function = None
    iter_function = None
    def __init__(self, list_function, iter_function, *_content):
        self.list_function = list_function
        self.iter_function = iter_function
        super().__init__('loop', *_content)


tags:list[type] = [Tag, window, module, frame, label, entry, button, img, loop]


# Mapeia os parametros das funções do tkinter aos seus tipos de variavel aceitados
PARAM_MAP = {
    # param     :  [types] , [priority values], default value
    'title'     : [[str], [], 'unnamed window'],
    'res'       : [[], value_is_resolution, '400x300'],

    'bg'        : [[], value_is_color, 'white'],
    'fg'        : [[], value_is_color, 'white'],

    'file'      : [[], value_is_file, 'None.png'],

    'r'         : [[int], [], 0],
    'c'         : [[int], [], 0],
    'sticky'    : [[], sticky_values, None],

    'padx'      : [[], [], 0],
    'pady'      : [[], [], 0],
    'justify'   : [[], [], None],

    'command'   : [[], value_is_function, None],

    'text'      : [[str], [], ''],
    'font'      : [[str], [], 'Calibri'],
    'font-size' : [[], [10, 12, 14, 16, 20, 22, 24], 10],

}

def check_param_type (field, value):        
    result = type(value) in PARAM_MAP[field][0]
    if not result:
        result = PARAM_MAP[field][1](value) if value_is_function(PARAM_MAP[field][1]) else value in PARAM_MAP[field][1]
    print(f'KML.check_param_type -- field: "{field}" | value: "{value}" | result: "{result}"')
    return result


# Mapeia as funções do tkinter aos diferentes tipos de Tag
FUNCTION_MAP = {
#    tipo       : (          função          , [                                            parametros                                           ]),
    'window'    : (KMLFunctions.create_window, ['title', 'res', 'bg',                                                                            ]),
    'module'    : (KMLFunctions.create_frame,  ['bg',                                    'padx', 'pady',                       'r', 'c', 'sticky']),
    'frame'     : (KMLFunctions.create_frame,  ['bg',                                    'padx', 'pady',                       'r', 'c', 'sticky']),
    'label'     : (KMLFunctions.create_label,  ['bg',       'text', 'font', 'font-size', 'padx', 'pady', 'justify',            'r', 'c', 'sticky']),
    'entry'     : (KMLFunctions.create_entry,  ['bg',               'font', 'font-size', 'padx', 'pady', 'justify',            'r', 'c', 'sticky']),
    'button'    : (KMLFunctions.create_button, ['bg', 'fg', 'text', 'font', 'font-size', 'padx', 'pady', 'justify', 'command', 'r', 'c', 'sticky']),
    'img'       : (KMLFunctions.create_img,    ['file',                                                                        'r', 'c', 'sticky']),
    'loop'      : (KMLFunctions.create_loop,   [                                                                                                 ]),
}

# Acessa a função no mapa de funções para o tipo de Tag fornecido
def get_function_data(_type):
    try:
        function_data = FUNCTION_MAP[_type]
        print(COLS[3] + f'KML.get_function -- type {_type} returns function {function_data}' + COLS[0])
    except:
        print(COLS[2] + f"KML.get_function -- ERRO: função não encontrada para a tag de tipo '{_type}'" + COLS[0])
    return function_data

# Executa a Tag fornecida requisitando a função correspondente ao seu tipo no mapa de funções 
# e conectando parametros automaticamente 
def run_tag(tag, parent):
    print(f'KML.run_tag -- tag "{tag}" | parent: "{parent}"')
    print(f'content: {tag.content}')
    function_data = get_function_data(tag.type)
    return run_function(function_data[0], tag, parent, get_params(function_data[1], tag))

def run_function (function, tag, parent, params):
    print(COLS[6] + f'KML.run_function -- function: "{function}" | parent: "{parent}" | params: "{params}"' + COLS[0])
    if parent is None:
        return function(tag, params)
    return function(tag, parent, params)

# Retorna uma lista com as informações na tag que correspondem aos campos 'fields' fornecidos
def get_params(fields, tag):

    # Inicializa uma lista para os parametros
    params = dict()

    # Inicializa uma lista que armazenará os dados da Tag que já foram associados a um campo da função
    tag_taken_content = []
    current_index = 1 if (False if len(tag.content) < 1 else value_is_id(tag.content[0])) else 0

    # Define uma função local que associa um valor da tag a um campo através do indice
    def assign_from_index(field, content):
        nonlocal current_index
        if current_index >= len(content):
            return None
        value = content[current_index]
        if not check_param_type(field, value):
            return None
        value = check_taken(value, f"from index {current_index}")
        if value is None:
            return None
        current_index += 1
        return value

    # Define uma função local que associa um valor da tag a um campo através de dicionário
    def assign_from_dict(field, content):
        for con in content:
            if type(con) is not dict:
                continue
            try:
                value = con[field]
            except:
                return None
            return check_taken(value, f"from dict {con}")
        return None

    # Retorna None caso o valor fornecido esteja na lista tag_taken_content
    # Caso contrario, adiciona o valor fornecido na lista tag_taken_content e o retorna
    def check_taken(value, debug = None):
        if value in tag_taken_content:
            return None
        tag_taken_content.append(value)
        if debug is not None:
            print(COLS[7] + f'value "{value}" {debug}' + COLS[0])
        return value

    # Para cada campo na lista fields
    for field in fields:

        # Inicializa uma variável valor para o campo da iteração atual do loop de campos
        value = assign_from_index(field, tag.content)
        if value is None:
            value = assign_from_dict(field, tag.content)
        if value is None:
            value = PARAM_MAP[field][2]

        if value is None:
            print(COLS[4] + f'KML.get_params -- field "{field}" ignored' + COLS[0])
        else:
            print(COLS[3] + f'KML.get_params -- field: "{field}" value: "{value}"' + COLS[0])

        params.update({field: value})

    print(f'params: {params}')

    # Retorne a lista de parametros gerada
    return params
