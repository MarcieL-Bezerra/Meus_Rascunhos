import tkinter.filedialog as fdlg
import os
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter import *
import pandas as pd

tinicial = tk.Tk()
tinicial.geometry("800x500+200+100")
tinicial.title("JUNTA ARQUIVOS - SIS")
tinicial.resizable(width=False, height=False)
tinicial['bg'] = '#49A'
tinicial.iconphoto(True, PhotoImage(file='./arquivos/junta.png'))
image=PhotoImage(file='./arquivos/junta.png')

colunaum='Código da Loja'
colunadois='CPF'

#path = fdlg.askopenfilenames()

#aqui seleciona a pasta a ser colocada o novo arquivo
opcoes = {}                # as opções são definidas em um dicionário
opcoes['initialdir'] = ''    # será o diretório atual
opcoes['parent'] = tinicial
opcoes['title'] = 'Diálogo que retorna o nome do diretório selecionado'
caminhoinicial = fdlg.askdirectory(**opcoes)

files = os.listdir(caminhoinicial)
#df = pd.DataFrame()

files_mp3 =[caminhoinicial + '\\' + f for f in files if f[-3:]== 'mp3']


print(files_mp3)

for f in files_mp3:
	os.remove(f)

'''
#df = df.style.hide_index()
ORDENADO = df[[colunaum,colunadois]]
#ORDENADO = ORDENADO.style.hide_index()

#opcoes = {}                # as opções são definidas em um dicionário
#opcoes['initialdir'] = ''    # será o diretório atual
#opcoes['parent'] = tinicial
#opcoes['title'] = 'Diálogo que retorna o nome do diretório selecionado'
#caminhoinicial = fdlg.askdirectory(**opcoes)

#ORDENADO.to_excel(caminhoinicial +'/Resultado-final.xlsx')


#print(df)
print(ORDENADO)
'''