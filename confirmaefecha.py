import tkinter as tk
import tkinter.messagebox as tkMessageBox


class MyDialog(tk.Toplevel):

  
    def __init__(self, parent, text):

        tk.Toplevel.__init__(self, parent)
        tk.Label(self, text=text).grid(row=0, column=0, columnspan=2, padx=60, pady=10)
        
        b_yes = tk.Button(self, text="Sim", command=self.yes, width=8)
        b_yes.grid(row=1, column=0, padx=10, pady=10)
        b_no = tk.Button(self, text="Não", command=self.no, width=8)
        b_no.grid(row=1, column=1, padx=10, pady=10)

        #self.answer = None
        self.protocol("WM_DELETE_WINDOW", self.no)

    def yes(self):
        self.answer = "Sim"
        self.destroy()

    def no(self):
        self.answer = "Não"
        self.destroy()

def popup():
    d = MyDialog(root, "Deseja Iniciar?")
    d.title('Caixa 1 ')
    root.after(5000, d.yes)
    root.wait_window(d)
    if d.answer == 'Sim':
        tkMessageBox.showinfo("Disse sim", message= "Realizado com Sim!")
    else:
        tkMessageBox.showinfo("Disse Não", message= "Realizado com Não!")
     
    print (d.answer)



root = tk.Tk()
tk.Button(root, text="Caixa", command=popup).pack()
#popup()
root.mainloop()


