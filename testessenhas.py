import pandas as pd
import os
from datetime import date
import time

data_atual = date.today()
data_atual = data_atual.strftime('%d-%m-%Y')


path = '.\\arquivos'
df = pd.DataFrame()
filesarquivo =[path + '\\' + 'acessos.xlsx']
for f in filesarquivo:
    dados=pd.read_excel(f) 
    df = df.append(dados)
#filesarquivo.close()    
loginDTS = df[['loginDTS']]
loginDTS = str(loginDTS.loc[0, 'loginDTS'])

senhaDTS = df[['senhaDTS']]
senhaDTS = str(senhaDTS.loc[0, 'senhaDTS'])

grupoDTS = df[['grupoDTS']]
grupoDTS = str(grupoDTS.loc[0, 'grupoDTS'])

loginVTX = df[['loginVTX']]
loginVTX = str(loginVTX.loc[0, 'loginVTX'])

senhaVTX = df[['senhaVTX']]
senhaVTX = str(senhaVTX.loc[0, 'senhaVTX'])

loginTHS = df[['loginTHS']]
loginTHS = str(loginTHS.loc[0, 'loginTHS'])

senhaTHS = df[['senhaTHS']]
senhaTHS = str(senhaTHS.loc[0, 'senhaTHS'])

global caminhodownload
caminhodownload = df[['caminhodownload']]
caminhodownload = os.path.abspath(caminhodownload.loc[0, 'caminhodownload'])
files = os.listdir(caminhodownload)

files_csv =[caminhodownload + '\\' + f for f in files if f[-3:]== 'xls']
contandoini = len(files_csv)
contadofim=0
while contadofim <= contandoini:
	files = os.listdir(caminhodownload)
	files_csv =[caminhodownload + '\\' + f for f in files if f[-3:]== 'xls']
	contadofim = len(files_csv)
	time.sleep(10)
	print("não mudou")
'''df2 = pd.DataFrame()
for f in files_csv:
	#print('aqui'+f)
	data=pd.read_csv(f,sep = '|') #sep = '|'
	df2 = df2.append(data)
#sisteminha = os.path.abspath(os.path.dirname(__file__))
#arquivo = os.startfile(r'.\\arquivos\\acessos.xlsx')
global caminhosalvar
caminhosalvar = df[['caminhosalvar']]
caminhosalvar = os.path.abspath(caminhosalvar.loc[0, 'caminhosalvar'])
df2.to_excel(caminhosalvar +'/Relatorio-Thalles-' + data_atual + '.xlsx', index=False)'''


print("Mudou")
print(contandoini)
print(contadofim)

#print(df2)