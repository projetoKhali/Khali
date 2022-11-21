
co0 = "#fae8e8"  # rosa
co1 = "#d9d9d9"  # cinzinha
co2 = "#1a1d1a"  # preta
co3 = "#26413C"  # verde



# funções genéricas de widgets do tkinter
def criar_frame(quadro, r, c, sticky='news', bg=co0, hlbg=co0, hlt=0, px=5, py=5):
    from tkinter import Frame
    frame = Frame(quadro, background=bg, highlightbackground=hlbg, highlightthickness=hlt)
    frame.grid(row=r, column=c, sticky=sticky, padx=px, pady=py)
    return frame

def criar_label(quadro, text, font, r, c, bg=co0, sticky='n', justify='left'):
    from tkinter import Label
    widget = Label(quadro, text=text, font=font, background=bg , justify=justify)
    widget.grid(row=r, column=c, sticky=sticky)
    return widget

def criar_button(quadro, text, font, r, c, command, sticky='ne', width=12):
    from tkinter import Button
    widget = Button(quadro, text=text, font=font, background=co0, justify='right', fg=co2, command=command,
        width=width, height=0, activebackground='#c5a8b0')
    widget.grid(row=r, column=c, sticky= sticky)
    return widget

def criar_entry(quadro, font, r, c, sticky='w', px=0, py=0, justify='left'):
    from tkinter import Entry
    widget = Entry(quadro, font=font, fg=co2, justify=justify)
    widget.grid(row=r, column=c, padx=px, pady=py, sticky=sticky)
    return widget
