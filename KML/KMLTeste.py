from tkinter import *
from KML.KML import *

def run():

    module = frame(
        'red',
        label(
            'green',
            "this is a test",
            0, 0,
        ),
        label(
            'blue',
            "This is another test",
            0, 1,
        ),
    )

    w = window('window test title', '800x600', module)
    
    w.run()
