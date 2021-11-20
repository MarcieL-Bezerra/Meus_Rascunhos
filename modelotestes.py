import random
import tkinter as tk



def sortenado():
    cont=0
    numini= int(Txtini.get())
    numfim=int(Txtfim.get())
    qtd=int(Txtqtd.get())
    textganha=""
    while (cont<qtd):
        ganhador=random.randint(numini,numfim)
        textganha = str(textganha) +" "+ str(ganhador)
        print('Ganhador '+str(ganhador))
        cont=cont+1
    Lblqtdganhador.config(text='Houve '+str(cont)+' ganhadores')
    Lblganhador.config(text='Números da sorte = ' + textganha)
    

tinicial = tk.Tk()
tinicial.geometry("500x600")
#w,h = tinicial.winfo_screenwidth(),tinicial.winfo_screenheight()
#tinicial.geometry("%dx%d+0+0" % (w, h))
tinicial.title("Tela de Sorteios - ...")
tinicial.resizable(width=False, height=False)
Lblini = tk.Label(tinicial,text='Escolha o inicio')
Lblini.pack()
Txtini=tk.Entry(tinicial,justify='center')
Txtini.pack()
Lblfim = tk.Label(tinicial,text='Escolha o fim')
Lblfim.pack()
Txtfim=tk.Entry(tinicial,justify='center')
Txtfim.pack()
Lblqtd = tk.Label(tinicial,text='Escolha a quantidade de sorteios')
Lblqtd.pack()
Txtqtd=tk.Entry(tinicial,justify='center')
Txtqtd.pack()

botao = tk.Button(tinicial, text="Sortear", command=sortenado)
botao.pack()

Lblganhador = tk.Label(tinicial)
Lblganhador.pack()
Lblqtdganhador = tk.Label(tinicial)
Lblqtdganhador.pack()



tinicial.mainloop()
