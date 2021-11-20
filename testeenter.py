from tkinter import *
from tkinter import messagebox

class EntryTeste( Frame ):
 def __init__( self ):
  # Inicializando configurações do frame
  Frame.__init__(self)
  self.pack()
  self.master.title( "<Return> teste" )
  self.master.geometry( "300x50" )
  self.frame = Frame( self )
  self.frame.pack( pady = 5 )
  
  # Criando a caixa de entrada
  self.caixa = Entry( self.frame, name = "caixa1" )
  
  # Fazendo o bind dela com o event handler exibe() 
  self.caixa.bind( "<Return>", self.exibe )
  self.caixa.pack( side = LEFT, padx = 5 )
  
  # Looping pra rodar a GUI
  self.mainloop()
  
 # Event handler
 def exibe(self, event):
  nomeCaixa = event.widget.winfo_name()
  conteudoCaixa = event.widget.get()
  messagebox.showinfo( "Texto na caixa", "Nome do widget: " + nomeCaixa + "\nConteúdo: " + conteudoCaixa )
  
# Criando um objeto
minhaGui = EntryTeste()
