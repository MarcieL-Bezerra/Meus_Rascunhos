import time
from datetime import date
from datetime import datetime, timedelta
#datas atuais
data_atual = date.today()
data_dmenos = date.today() + timedelta(days=-1)
primeiro_mes_atual=datetime(data_atual.year,data_atual.month,1)

	#datas passadas
primeiro_mes_passado=date(data_atual.year,data_atual.month-1,1)
ultimo_mes_passado = primeiro_mes_atual + timedelta(days=-1)
primeira_data=primeiro_mes_passado
dias=8
segunda_data = primeira_data + timedelta(days=dias)

while primeira_data <=data_atual:
	#print("Rodei - " + str(contado))
	#print(primeiro_mes_passado)
	print("data 1 " + str(primeira_data))
	print("data 2 " + str(segunda_data))

	primeira_data = primeira_data + timedelta(days=dias+1)
	segunda_data = primeira_data + timedelta(days=dias)

print("acabou")