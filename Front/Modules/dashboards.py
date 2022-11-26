from tkinter import *
from graficos import Dashboards
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Authentication import CURRENT_USER
from Models import Role 
from CSV import CSVHandler as handler
import Settings
from Front.Core import *

# Informações do modulo
NAME = 'Dashboards'
REQUIRED_PERMISSIONS_REG = [None]        
REQUIRED_PERMISSIONS_RATE = [None]
REQUIRED_PERMISSIONS_VIEW = [11]

master_frame = None
# esses parâmetros são dados de quem está logando
#  user_id, user_role, user_group
def run(frame_parent):
    
    global master_frame
    # from Front.Scrollbar import add_scrollbar
    # master_frame = add_scrollbar(frame_parent)
    frame_parent.configure(background = co0)
    master_frame = Frame(frame_parent, background = co0)
    master_frame.grid(sticky = 'nwe')
    master_frame.columnconfigure(0, minsize = 0, weight = 1)
    master_frame.rowconfigure(0, minsize = 0, weight = 1)
     # função de criar frame
    # def criar_frame(quadro, row, column, background = co0):
    #     frame = Frame(quadro, background = background, relief=FLAT, bd=1)
    #     frame.rowconfigure(row, minsize = 10)  # Quantas linhas o frame terá
    #     frame.columnconfigure(column, minsize = 100)  # Quantas colunas o frame terá
    #     frame.grid(row=row, column=column, padx=10, pady=10, sticky='nw') # Local onde o frame será colocado
    #     return frame
    

    # criar widgets ###quadro é se seá colocado na janela ou em frame
    def criar_label(quadro, text, font, r, c, name=None, background=co0, fg=co2):
        label = Label(quadro, text=text, font=font, background=background, fg=fg)
        label.grid(row=r, column=c, padx=5, pady=3, sticky = "w")
        return label

    frame_title = criar_frame(master_frame, 0, 0, "ew",co3, px= 0, py=0)
    frame_title.columnconfigure(0,weight=1)
    criar_label(frame_title, "Dashboards", "Calibri, 24 bold", 0, 0, None, co3, co0)
    
    from Models.Group import get_groups_of_leader, get_groups_of_client
    from Authentication import CURRENT_USER
    create_dropdown(criar_frame(frame_title, 0, 1, "ew", co3, px=12, py=0),0,0, [i.name for i in get_groups_of_leader(CURRENT_USER.id)] + [i.name for i in get_groups_of_client(CURRENT_USER.id)])


    
    from Authentication import CURRENT_USER
    if CURRENT_USER.role_id in [3, 4, 5]:
        frame_dashboards = criar_frame(master_frame, 1, 0)
        # figure = Dashboards.teste()
        figure1 = Dashboards.user_media_sprints(CURRENT_USER.id)
        canvas = FigureCanvasTkAgg(figure1, master = frame_dashboards)
        # canvas.show()
        canvas.get_tk_widget().grid(row=0, column=0, sticky='wens')
        figure2 = Dashboards.user_media_x_team(CURRENT_USER.id)
        canvas = FigureCanvasTkAgg(figure2, master = frame_dashboards)
        # canvas.show()
        canvas.get_tk_widget().grid(row=0, column=1, sticky='wens')

    if CURRENT_USER.role_id in [1, 2]:
        from Models.Group import get_group
        group = get_group(CURRENT_USER.group_id)
        frame_dashboards = criar_frame(master_frame, 1, 0)
        # figure = Dashboards.teste()
        figure1 = Dashboards.teams_media(group.id)
        canvas = FigureCanvasTkAgg(figure1, master = frame_dashboards)
        # canvas.show()
        canvas.get_tk_widget().grid(row=0, column=0, sticky='wens')
        if group.leader_id == CURRENT_USER.id:
            figure2 = Dashboards.role_media(3, group.id)
            canvas = FigureCanvasTkAgg(figure2, master = frame_dashboards)
            # canvas.show()
            canvas.get_tk_widget().grid(row=0, column=1, sticky='wens')
        if group.client_id == CURRENT_USER.id:
            figure2 = Dashboards.role_media(4, group.id)
            canvas = FigureCanvasTkAgg(figure2, master = frame_dashboards)
            # canvas.show()
            canvas.get_tk_widget().grid(row=0, column=1, sticky='wens')
    