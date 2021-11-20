from Usuarios2 import Usuarios
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master, bg='Wheat')
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master, bg='Wheat')
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master, bg='Wheat')
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master, bg='Wheat')
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master, bg='Wheat')
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master, bg='Wheat')
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master, bg='Wheat')
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master, bg='Wheat')
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master, bg='Wheat')
        self.container9["pady"] = 15
        self.container9.pack()
        root.geometry("400x450+0+0")
        root.title("MBZ - SIS - Cadastrar Usuário")
        root.configure(background="Wheat")
        #root.iconbitmap("logo3.ico")

        self.titulo = Label(self.container1, text="Informe os dados :", bg='DarkSeaGreen3')
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblidusuario = Label(self.container2,
        text="Placa:" , bg='DarkSeaGreen3', font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtcpf = Entry(self.container2)
        self.txtcpf["width"] = 16
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", bg='DarkSeaGreen3',bd=2,
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Modelo:", bg='DarkSeaGreen3',
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Cor:", bg='DarkSeaGreen3',
        font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail= Label(self.container5, text="Ano:", bg='DarkSeaGreen3',
        font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        #self.lblusuario= Label(self.container6, text="Usuário:", bg='DarkSeaGreen3',
        #font=self.fonte, width=10)
        #self.lblusuario.pack(side=LEFT)

        #self.txtusuario = Entry(self.container6)
        #self.txtusuario["width"] = 25
        #self.txtusuario["font"] = self.fonte
        #self.txtusuario.pack(side=LEFT)

        #self.lblsenha= Label(self.container7, text="Senha:", bg='DarkSeaGreen3',
        #font=self.fonte, width=10)
        #self.lblsenha.pack(side=LEFT)

        #self.txtsenha = Entry(self.container7)
        #self.txtsenha["width"] = 25
        #self.txtsenha["show"] = "*"
        #self.txtsenha["font"] = self.fonte
        #self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", bg='DarkSeaGreen3',bd=4,
        font=self.fonte, width=10)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", bg='DarkSeaGreen3',bd=4,
        font=self.fonte, width=10)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", bg='DarkSeaGreen3',bd=4,
        font=self.fonte, width=10)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="", bg='Wheat')
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserirUsuario(self):
        user = Usuarios()

        user.placa = self.txtcpf.get()
        user.modelo = self.txtnome.get()
        user.cor = self.txttelefone.get()
        user.ano = self.txtemail.get()
        #user.usuario = self.txtusuario.get()
        #user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtcpf.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        #self.txtusuario.delete(0, END)
        #self.txtsenha.delete(0, END)



    def alterarUsuario(self):
        user = Usuarios()

        user.cpf = self.txtcpf.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtcpf.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)



    def excluirUsuario(self):
        user = Usuarios()

        user.placa = self.txtcpf.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtcpf.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        #self.txtusuario.delete(0, END)
        #self.txtsenha.delete(0, END)


    def buscarUsuario(self):
        user = Usuarios()

        placa = self.txtcpf.get()

        self.lblmsg["text"] = user.selectUser(placa)

        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT, user.placa)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.modelo)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT,user.cor)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.ano)

        #self.txtusuario.delete(0, END)
        #self.txtusuario.insert(INSERT, user.usuario)

        #self.txtsenha.delete(0, END)
        #self.txtsenha.insert(INSERT,user.senha)



root = Tk()
Application(root)
root.mainloop()
