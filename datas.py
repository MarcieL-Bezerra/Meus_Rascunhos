from datetime import date
from datetime import datetime, timedelta

import pyautogui,time

pyautogui.hotkey('alt', 'tab')
'''
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')


data_atual = date.today()
data_dmenos = date.today() + timedelta(days=-1)
data_Mmenos = data_atual.month-1
#novadata = str(data_dmenos) +"/"+ str(data_atual.month) +"/"+ str(data_atual.year)
#mes_passado = str(data_atual.day)+"/"+str(data_Mmenos)+"/"+str(data_atual.year)
#data_ontem = datetime.strptime(novadata,'%d/%m/%Y')

data_dmenos = data_dmenos.strftime('%d/%m/%Y')
primeiro_mes_passado=datetime(data_atual.year,data_atual.month-1,1)
#primeiro_mes_passado=primeiro_mes_passado.strftime('%d/%m/%Y')
primeiro_mes_passado = primeiro_mes_passado.strftime('%d/%m/%Y')
primeiro_mes_atual=datetime(data_atual.year,data_atual.month,1)
ultimo_mes_passado = primeiro_mes_atual + timedelta(days=-1)
ultimo_mes_passado=ultimo_mes_passado.strftime('%d/%m/%Y')

#data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_em_texto = data_atual.strftime('%d/%m/%Y')
#data_atual.year)
#print(data_dmenos)
print(primeiro_mes_passado)
print(primeiro_mes_atual)
print(ultimo_mes_passado)'''

#print(data_atual)