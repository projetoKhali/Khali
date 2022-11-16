
# Informações do modulo
NAME = 'Lista'
REQUIRED_PERMISSIONS_REG  = [None]
REQUIRED_PERMISSIONS_RATE = [
    [3, 4, 5]  # pelo menos uma das 3
]
REQUIRED_PERMISSIONS_VIEW = [None]

def run(frame_parent):
    from KML.KML import frame, label

    # from Front.Scrollbar import add_scrollbar
    # module_frame = add_scrollbar(frame_parent)
    return frame(
        'red',
        'nsew',

        # ratings | left section
        frame(
            'green',
            0,0,
            'ns',
            label('asiyugdiauhs'),
        ),
        frame(
            'green',
            1,0,
            'ns',
            label('asiyugdiauhs'),

        ),


    ).run(frame_parent)
