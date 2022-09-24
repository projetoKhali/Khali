from tkinter import *

def grid (obj, r, c, s):
    if s:
        obj.grid(row=r, column=c, sticky=s)
    else:
        obj.grid(row=r, column=c)
    return obj

def create_window(a):
    window = Tk()
    window.title(a['title'])
    window.geometry(a['res']) 
    # window.rowconfigure(0, minsize = 800, weight = 1)
    # window.columnconfigure(1, minsize = 800, weight = 1)
    window.configure(background=a['bg'])
    return window

def create_frame(parent, a):
    return grid(
        Frame(
            parent,
            bg=a['bg'],
            padx=a['padx'],
            pady=a['pady']
        ),
        a['r'],
        a['c'],
        a['sticky']
    )

def create_label(parent, a):
    return grid(
        Label(
            parent,
            bg=a['bg'],
            text=a['text'],
            font=f"{a['font']}, {a['font-size']}",
            justify=a['justify']
        ),
        a['r'],
        a['c'],
        a['sticky']
    )

def create_entry(parent, a):
    return grid(
        Entry(
            parent,
            bg=a['bg'],
            font=f"{a['font']}, {a['font-size']}",
            justify=a['justify']
        ),
        a['r'],
        a['c'],
        a['sticky']
    )

def create_button(parent, a):
    return grid(
        Button(
            parent,
            bg=a['bg'],
            text=a['text'],
            font=f"{a['font']}, {a['font-size']}",
            justify=a['justify'],
            command=a['command']
        ),
        a['r'],
        a['c'],
        a['sticky']
    )
