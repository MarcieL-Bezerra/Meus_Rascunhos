import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
janela = Tk()
janela.geometry("1440x900+0+0")
janela.title("MB - GERENCIADOR ")
janela['bg'] = 'DodgerBlue'

#figura
figura = plt.Figure(figsize=(8,4), dpi=60)
ax1 = figura.add_subplot(111)

canva = FigureCanvasTkAgg(figura, janela)
canva.get_tk_widget().place(relx=0.4, rely = 0.1)


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Fazenda', 'Cordeiro', 'União', 'Pessoal'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

#fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

janela.mainloop()