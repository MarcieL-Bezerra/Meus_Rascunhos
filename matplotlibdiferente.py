import sys, time, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import ticker

class wS1(QWidget):
 
    def __init__(self):
        super().__init__()

        self.setWindowTitle('graficos')      
        self.setFixedSize(1440,880)

        self.initUI()
        
    def initUI(self):

        def set_GraphWidget_1 (ys=[0,1,0,2,26,22,14,12,4,2],remark=3):



            self.figure = Figure(figsize=(3,1.8))
            self.Graph_1 = FigureCanvas(self.figure)
            ax = self.figure.add_subplot(111)
            self.figure.tight_layout()
            ax.clear()
            ax.grid(True,axis='both',linestyle=':')

            ax.set_yticklabels(ax.get_yticks(), {'family':'Cambria','size':'9','color':'black'})
            ax.set_xticklabels(ax.get_xticks(), {'family':'Cambria','size':'9','color':'white'})

            ax.tick_params(which='major', width=0.75, length=5, color='grey')
            ax.tick_params(which='minor', width=0.5, length=2.5, color='grey')

            for spine in ax.spines.values():
                spine.set_edgecolor('grey')

            ax.set_facecolor('#f4f2f1')

            ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
            ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
            ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
            ax.yaxis.set_major_formatter('{x} %')

            ax.plot(ys,linewidth=1,markersize=3,marker='o',color='#e66f00',zorder=0)
            if remark != None: 
                ax.scatter(remark,ys[remark],s=35,linewidth=0.5,edgecolors='black',color='#e66f00',zorder=1)
            
        def set_GraphWidget_2 (ys=[120,66,19,19,14,9,9,5,0,6]):
        
            self.figure = Figure(figsize=(3,2.5))
            self.Graph_2 = FigureCanvas(self.figure)
            ax = self.figure.add_subplot(111)
            self.figure.tight_layout()
            ax.clear()
            ax.grid(True,axis='both',linestyle=':')

            ax.set_yticklabels(ax.get_yticks(), {'family':'Cambria','size':'9','color':'black'}) #

            ax.tick_params(which='major', width=0.75, length=5, color='grey')
            ax.tick_params(which='minor', width=0.5, length=2.5, color='grey')

            for spine in ax.spines.values():
                spine.set_edgecolor('grey')

            ax.set_facecolor('#f4f2f1')

            ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
            ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
            ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
            ax.yaxis.set_major_formatter('{x}')
        
            ax.xaxis.tick_top()
            width = 0.08
            opacity = 0.85
            xs = range(1,len(ys)+1)
            ax.bar(xs,ys,width,color='#e66f00')

        set_GraphWidget_1()
        set_GraphWidget_2()

        self.Lay = QVBoxLayout()
        self.Lay.addWidget(self.Graph_1)
        self.Lay.addWidget(self.Graph_2)

        self.setLayout(self.Lay)

app = QApplication(sys.argv)
window = wS1()
window.show()
sys.exit(app.exec_())

if __name__ == '__main__':
    main()