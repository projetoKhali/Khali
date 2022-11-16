from tkinter import *

def grid (obj, r, c, s):
    if s != None:
        obj.grid(row=r, column=c, sticky=s)
    else:
        obj.grid(row=r, column=c)
    return obj

def create_window(tag, a):
    window = Tk()
    window.title(a['title'])
    window.geometry(a['res']) 
    # window.rowconfigure(0, minsize = 800, weight = 1)
    # window.columnconfigure(1, minsize = 800, weight = 1)
    window.configure(background=a['bg'])
    return window

def create_frame(tag, parent, a):
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

def create_label(tag, parent, a):
    return grid(
        Label(
            parent,
            bg=a['bg'],
            padx=a['padx'],
            pady=a['pady'],
            text=a['text'],
            font=f"{a['font']}, {a['font-size']}",
            justify=a['justify']
        ),
        a['r'],
        a['c'],
        a['sticky']
    )

def create_entry(tag, parent, a):
    return grid(
        Entry(
            parent,
            bg=a['bg'],
            # padx=a['padx'],
            # pady=a['pady'],
            font=f"{a['font']}, {a['font-size']}",
            justify=a['justify']
        ),
        a['r'],
        a['c'],
        a['sticky']
    )

def create_button(tag, parent, a):
    return grid(
        Button(
            parent,
            fg=a['fg'],
            bg=a['bg'],
            padx=a['padx'],
            pady=a['pady'],
            text=a['text'],
            font=f"{a['font']}, {a['font-size']}",
            justify=a['justify'],
            command=a['command'],
        ),
        a['r'],
        a['c'],
        a['sticky']
    )

def create_img(tag, parent, a):
    from Settings import RESOURCES_PATH
    # try:
    kml_img = PhotoImage(file=f"{RESOURCES_PATH}\\{a['file']}")
    # except:
    #     pass
        # kml_img = PhotoImage(file=f"{RESOURCES_PATH}\\None.png")
    kml_lbl = Label(parent, image=kml_img)
    kml_lbl.photo = kml_img
    return grid(
        kml_lbl,
        a['r'],
        a['c'],
        a['sticky']
    )

def create_loop (tag, parent, a):
    results = []
    from KML.KMLUtils import value_is_function
    items = tag.list_function() if value_is_function(tag.list_function) else tag.list_function
    for index, item in enumerate(items):
        iteration_tag = tag.iter_function(tag, index, item)
        results.append(iteration_tag.run(parent))

    return results
