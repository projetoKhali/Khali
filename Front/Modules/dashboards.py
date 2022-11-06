from tkinter import *
from graficos import Dashboards
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# cores
co0 = "#FAE8E8" #rosa
co1 = "#D9D9D9" #cinza
co2 = "#1A1D1A" #preta


master_frame = None

def run(frame_parent):
   
    global master_frame
     # função de criar frame
    def criar_frame(quadro, row, column):
        frame = Frame(quadro, background = co0, relief=FLAT, bd=1)
        frame.rowconfigure(row, minsize = 10)  # Quantas linhas o frame terá
        frame.columnconfigure(column, minsize = 100)  # Quantas colunas o frame terá
        frame.grid(row=row, column=column, padx=10, pady=10, sticky='w') # Local onde o frame será colocado
        return frame

    # criar widgets ###quadro é se seá colocado na janela ou em frame
    def criar_label(quadro, text, font, r, c, name=None):
        label = Label(quadro, text=text, font=font, background=co0, fg=co2)
        label.grid(row=r, column=c, padx=5, pady=3, sticky = "w")
        return label

    frame_title = criar_frame(frame_parent, 0, 0)
    criar_label(frame_title, "Dashboards", "Calibri, 20", 0, 0)
    
    frame_dashboards = criar_frame(frame_parent, 1, 0)
    # figure = Dashboards.teste()
    figure1 = Dashboards.user_media_sprints(6)
    canvas = FigureCanvasTkAgg(figure1, master = frame_dashboards)
    # canvas.show()
    canvas.get_tk_widget().grid(row=0, column=0, sticky='wens')
    figure2 = Dashboards.user_media_x_team(6)
    canvas = FigureCanvasTkAgg(figure2, master = frame_dashboards)
    # canvas.show()
    canvas.get_tk_widget().grid(row=0, column=1, sticky='wens')
    
    # figure = Figure(figsize = (5,4), dpi = 100)
    # figure.get_figure()
    # canvas =  FigureCanvasTkAgg(figure, master = frame_parent)
    # canvas.draw
    # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

