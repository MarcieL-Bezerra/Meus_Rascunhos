import pandas as pd
import os



path = r'C:\Users\Casa\Downloads\Relatorios'
files = os.listdir(path)
df = pd.DataFrame()

files_xlsx =[path + '\\' + f for f in files if f[-3:]== 'csv' ]

for f in files_xlsx:
	data=pd.read_csv(f, sep = '|')
	df = df.append(data)


df.to_excel(r'C:\Users\Casa\Downloads\Relatorios\final.xlsx')
