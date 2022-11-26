# inicializa o sistema de eventos
import Events

Events.initialize()

# Cria dados de teste para popular os bancos de dados com usuários, grupos, times e avaliações
from _test import create_test_data

# create_test_data()

from Time import set_today
# set_today(29, 8)    # começo da sprint 1 
# set_today(19, 9)    # fim da sprint 1 | começo do periodo avaliativo da sprint 1 
# set_today(26, 9)    # fim do periodo avaliativo da sprint 1 

# # teste retorno de valores do sistema de eventos
# def teste():
#     from tkinter import Tk, IntVar
#     Tk()
#     for i in range(4):
#         var = IntVar(value=i)
#         Events.register(f'test_{i}', lambda v=var: v.get())
# teste()
# for i in range(5):
#     print(Events.trigger(f'test_{i}'))
# exit()


# from tkinter import *
# window = Tk()
# window.configure(background = co0)
# window.columnconfigure([0], minsize = 0, weight = 1)
# window.rowconfigure([0], minsize = 0, weight = 1)

# from Front.Modules import dashboards
# dashboards.run(window)
# def on_closing():
#     from matplotlib import pyplot as plt
#     plt.close("all")
#     window.destroy()
# window.protocol("WM_DELETE_WINDOW", on_closing)
# window.mainloop()

# exit()


# from Authentication import register
# for i in range(10):
#     register("fulano",  "f@u.lano", 0, 0, 5, custom_password='123')



from Front import WindowManager

WindowManager.initialize()

# teste - login automatico
from Authentication import login
# login(email='a@d.m', senha='123')
login(email='l@d.g', senha='123')
# login(email='c@c.c', senha='123')
# login(email='lt1@o.com', senha='123')
# login(email='fulano-dev@dev.com', senha ='123')
# login(email='d@e.v', senha='123')

WindowManager.update()
