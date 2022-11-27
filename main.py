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
set_today(29, 11)


# area de testes 
# exit()

from Front import WindowManager

WindowManager.initialize()

# teste - login automatico
from Authentication import login
login(email='a@d.m', senha='123')
# login(email='l@d.g', senha='123')
# login(email='c@c.c', senha='123')
# login(email='lt2@o.com', senha='123')
# login(email='fulano-dev@dev.com', senha ='123')
login(email='d@e.v', senha='123')

WindowManager.update()
