from tkinter import *
from KML.KML import *

def run():
    janela = window(                                    # Tag janela
        'window test title',                            # titulo
        '1000x600',                                     # resolução
        frame(                                              # Tag frame
            0, 0,                                           # row, column
            frame(                                              # Tag frame
                'red',                                          # bg
                0, 0,                                           # row, column
                {'padx':20},                                    # padx
                {'pady':20},                                    # pady
                label('#FAE8E8', "titulo", 20, 0, 0, 'ew'),         # Tag label(bg, text, font-size, row, column, sticky)
            ),                                                  
        ),                                                  
        frame(                                              # Tag frame
            1, 0,                                               # row, column
            frame(                                                  # Tag frame
                'green',                                            # bg
                1, 0,                                               # row, column
                {'padx':20},                                        # padx
                {'pady':20},                                        # pady
                label('cyan', "coluna A label 1", 0, 0, 'ew'),          # Tag label(bg, text, font-size, row, column, sticky)
                label('magenta', "coluna A label 2", 0, 1, 'ew'),       # Tag label(bg, text, font-size, row, column, sticky)
            ),
            frame(                                                  # Tag frame
                'blue',                                             # bg 
                1, 3,                                               # row, column 
                {'padx':20},                                        # padx 
                {'pady':20},                                        # pady 
                label('yellow', "coluna B label 1", 0, 0, 'ew'),        # Tag label(bg, text, font-size, row, column, sticky)
                label('white', "coluna B label 2", 0, 1, 'ew'),         # Tag label(bg, text, font-size, row, column, sticky)
            ),
        ),
    )
    janela.run()
