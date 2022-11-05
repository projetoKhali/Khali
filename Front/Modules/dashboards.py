from tkinter import *
from graficos import Dashboards
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# cores
co0 = "#FAE8E8" #rosa
co1 = "#D9D9D9" #cinza
co2 = "#1A1D1A" #preta




def run(frame_parent):
   
    
     # função de criar frame
    def criar_frame(quadro, row, column):
        frame = Frame(quadro, background = co0, relief=FLAT, bd=1)
        frame.rowconfigure(row, minsize = 10)  # Quantas linhas o frame terá
        frame.columnconfigure(column, minsize = 100)  # Quantas colunas o frame terá
        frame.grid(row=row, column=column, padx=10, sticky='w') # Local onde o frame será colocado
        return frame

    # criar widgets ###quadro é se seá colocado na janela ou em frame
    def criar_label(quadro, text, font, r, c, name=None):
        label = Label(quadro, text=text, font=font, background=co0, fg=co2)
        label.grid(row=r, column=c, padx=5, pady=3, sticky = "w")
        return label
    # criar_label(frame_parent, "oi com boi", "Calibri, 10", 0, 0)
    
    # figure = Dashboards.teste()
    # figure = Dashboards.user_media_sprints_fig(6)
    figure = Dashboards.user_media_x_team_fig(6)
    canvas = FigureCanvasTkAgg(figure, master = frame_parent)
    # canvas.show()
    canvas.get_tk_widget().grid(row=0, column=0, sticky='wens')
    
    # figure = Figure(figsize = (5,4), dpi = 100)
    # figure.get_figure()
    # canvas =  FigureCanvasTkAgg(figure, master = frame_parent)
    # canvas.draw
    # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

