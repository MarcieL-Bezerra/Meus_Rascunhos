import tkinter as tk
import tkinter.filedialog as fdlg
import tkinter.scrolledtext as tkst
from tkinter.constants import END,HORIZONTAL, VERTICAL, NW, N, E, W, S, SUNKEN, LEFT, RIGHT, TOP, BOTH, YES, NE, X, RAISED, SUNKEN, DISABLED, NORMAL, CENTER
import csv
class TesteDialogs(object):
	appname= "Demonstrador de diálogos no Tkinter"
	frameWidth      = 800
	frameHeight     = 600
	padx            = 5
	pady            = 5


	def __init__(self, **kw):

		self.root = tk.Tk()

		self.root.title(self.appname)

		self.root.geometry('%dx%d' % (self.frameWidth, self.frameHeight))

		self.createMenuBar()

		#self.minhaTela = tk.Frame(self.root)
		#self.minhaTela.pack( padx= "5", pady="5",expand=1, fill="both")

		#self.editor = tkst.ScrolledText(master = self.minhaTela,wrap= tk.WORD,width  = 20,height = 10)
		#self.editor.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
		#self.editor.insert(tk.INSERT, "Esta é uma linha no editor")



	def createMenuBar(self):

		menubar = tk.Menu(self.root)

		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Sair", command=self.root.quit)
		menubar.add_cascade(label="Arquivo", menu=filemenu)
		showFileDialogsmenu = tk.Menu(menubar, tearoff=0)
		showFileDialogsmenu.add_command(label="ABRIR ARQUIVO", command=self. testeaskdirectory)
		menubar.add_cascade(label="DiálogosArquivos", menu=showFileDialogsmenu)


		self.root.config(menu=menubar)

	


	def testeaskdirectory(self):
	    #primeiro definimos as opções

		opcoes = {}                 # as opções são definidas em um dicionário
		opcoes['defaultextension'] = '.txt'
		opcoes['filetypes'] = [('Todos arquivos', '.*'), ('arquivos texto', '.txt')]
		opcoes['initialdir'] = ''    # será o diretório atual
		opcoes['initialfile'] = '' #apresenta todos os arquivos no diretorio
		opcoes['parent'] = self.root
		opcoes['title'] = 'Diálogo que retorna um objeto arquivo'

		#retorna um arquivo aberto no modo leitura

		arquivo= fdlg.askopenfile(mode='r', **opcoes)
		next (arquivo)

		for contato in arquivo:
			print(contato)
			#arquivo.close()    # não iremos fazer nada agora com o arquivo. fechamos

	def execute(self):
	    self.root.mainloop()



def main(args):

	appProc=  TesteDialogs()
	appProc.execute()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
