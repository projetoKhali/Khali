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
                1, 1,                                               # row, column 
                {'padx':20},                                        # padx 
                {'pady':20},                                        # pady 
                label('yellow', "coluna B label 1", 0, 0, 'ew'),        # Tag label(bg, text, font-size, row, column, sticky)
                label('white', "coluna B label 2", 0, 1, 'ew'),         # Tag label(bg, text, font-size, row, column, sticky)
            ),
        ),
    )
    janela.run()

def run_tkinter():
    janela = Tk()
    janela.title('window test title')
    janela.geometry('1000x600')  # tamanho da tela, largura x altura

    janela.configure(background='#FAE8E8')

    frame1 = Frame(janela)
    frame1.grid(row=0, column=0)

    frame_titulo = Frame(frame1, bg='red', padx=20)
    frame_titulo.grid(row=0, column=0)
    
    Label(frame_titulo, bg='#FAE8E8', text="titulo", font="Calibri, 20").grid(row=0, column=0, sticky='ew')

    frame2 = Frame(janela)
    frame2.grid(row=1, column=0)

    frame_colunaA = Frame(frame2, bg='green', padx=20)
    frame_colunaA.grid(row=1, column=0)

    Label(frame_colunaA, bg='cyan', text="coluna A label 1", font="Calibri, 10").grid(row=0, column=0, sticky='ew')
    Label(frame_colunaA, bg='magenta', text="coluna A label 2", font="Calibri, 10").grid(row=0, column=1, sticky='ew')

    frame_colunaB = Frame(frame2, bg='blue', padx=20)
    frame_colunaB.grid(row=1, column=3)

    Label(frame_colunaB, bg='yellow', text="coluna B label 1", font="Calibri, 10").grid(row=0, column=0, sticky='ew')
    Label(frame_colunaB, bg='white', text="coluna B label 2", font="Calibri, 10").grid(row=0, column=1, sticky='ew')

    janela.mainloop()

