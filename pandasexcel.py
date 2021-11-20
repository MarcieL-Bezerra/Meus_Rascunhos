import pandas as pd
from datetime import datetime, date
import os

caminhodownload =r'C:\Users\Marciel\Downloads' 
caminhosalvar = r'C:\Users\Marciel\Downloads\juntados'
files = os.listdir(caminhodownload)

files_csv =[caminhodownload + '\\' + f for f in files if f[-3:]== 'csv']



os.rename(files_csv[len(files_csv)-1], files_csv[len(files_csv)-1].replace('.csv',' ') + '(' + str(len(files_csv)-len(files_csv)) + ')' + '.csv')
files = os.listdir(caminhodownload)

files_csv =[caminhodownload + '\\' + f for f in files if f[-3:]== 'csv']
files_csv.sort(reverse = True)
print(files_csv)
df2 = pd.DataFrame()
novovcto = []
data_atual = date.today()
for f in files_csv:
	#print('aqui'+f)
	data=pd.read_csv(f,sep = '|') #sep = '|'
	df2 = df2.append(data)
'''for linha in df2['Data da Última Modificação do Status']:
	linha = datetime.strptime(linha, '%d/%m/%Y %H:%M').date()
	#linha = linha.strftime('%d/%m/%Y')
	novovcto.append(linha)

del df2['Data da Última Modificação do Status']
df2.insert(21, "Data da Última Modificação do Status",novovcto, allow_duplicates=True)

	#linha = linha.strftime('%m/%d/%Y')
	
#df2['Data da Última Modificação do Status'] = df2['Data da Última Modificação do Status'].dt.strftime('%m/%d/%Y')
#print(type(df2['Data da Última Modificação do Status']))

df2.sort_values(by=['Data da Última Modificação do Status'], ascending=False)'''
df2.to_excel(caminhosalvar +'/Relatorio-Thalles-' + str(data_atual.strftime('%d-%m-%Y')) + '.xlsx', index=False)
'''for f in files_csv:
	os.remove(f)'''