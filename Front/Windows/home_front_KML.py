from tkinter import *
from Front.Modules import ModulesManager
from KML.KML import *
import Settings

# cores
co0 = "#FAE8E8"  # rosa
co1 = "#D9D9D9"  # cinza
co2 = "#1A1D1A"  # preta
co3 = "#26413C"  # verde

current_module = None
modules = []

frame_coluna_A = None
frame_coluna_B = None

# janela = None

def run(init_module = True):

    w = window(
        '@window',
        'Home (KML)',
        '1000x600',
        'white',

        # frame_coluna_A
        frame(
            '@frame_coluna_A',
            {'sticky':'nw'},

            # frame logo
            frame(
                '@frame_logo',
                {'sticky':'nw'},

                # logo
                img('Logo_small.png', {'sticky':'n'})
            ),

            # frame tabs | contém os botões seletores de modulo
            frame(
                '@frame_tabs',
                1, 0,
                '#FAE8E8',
                {'sticky':'nw'},

                # tag loop - executa o loop na lista fornecida
                loop(
                    ModulesManager.get_modules,         # função que será chamada para gerar a lista do loop
                    lambda tag,index,item: button({     # função que será chamada a cada iteração do loop
                        'text'     : item.NAME,
                        'fg'       : 'white'  ,
                        'bg'       : '#26413C',
                        'font-size': 14       ,
                        'padx'     : 5        ,
                        'pady'     : 5        ,
                        'r'        : index    ,
                        'c'        : 0        ,
                        'sticky'   : 'w'      ,
                        'command':lambda i=index, t=tag: print(f'{tag}|{index}')
                    })
                    
                )

            )
        ),

        # frame_coluna_B
        frame(
            '@frame_coluna_B',

        )
    )

    w.run()

    print(w.content)

    return w
