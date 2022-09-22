from tkinter import *
def create_label(parent, text, r, c):
    Label(parent, text=text, font="Calibri").grid(row=r, column=c, sticky = "w")
