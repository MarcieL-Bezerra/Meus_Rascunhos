#from main import App
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import pandas as pd
import tkinter.filedialog as fdlg





conexao = sqlite3.connect('bancoUsuario.db')
c = conexao.cursor()


c.execute("""create table if not exists usuarios (
	cpf text unique,
	nome text,
	email text,
	fone text,
	senha text,
	idusuario integer primary key autoincrement)""")
conexao.commit()
c.close()

def insertUser(cpf, nome, email, fone,senha):
	#cria = createTableUsuarios()
	try:
		conexao = sqlite3.connect('bancoUsuario.db')
		c = conexao.cursor()
		c.execute("INSERT INTO usuarios (cpf, nome, email, fone,senha) VALUES('" + cpf + "','" + nome + "','" + email + "','" + fone + "','" + senha +"')")
		conexao.commit()
		c.close()
		
		return "Usuário cadastrado com sucesso!"
		
	except:
		return "Atenção: Ocorreu um erro na inserção do usuário"
		
def deleteUser(cpf):
	try:
		conexao = sqlite3.connect('bancoUsuario.db')
		c = conexao.cursor()
		c.execute("delete from usuarios where cpf = '" + cpf + "' ")
		conexao.commit()
		c.close()
		
		return "Usuário deletado com sucesso!"
		
	except:
		
		return "Atenção: Ocorreu um erro"


def selectUser(cpfa):
	
	caminhoinicial = '.\\arquivos'
	#path = '.\\arquivos'
	#df = pd.DataFrame()
	#filesarquivo =[path + '\\' + 'acessos.xlsx']
	conexao = sqlite3.connect('bancoUsuario.db')
	c = conexao.cursor()
	c.execute("SELECT * FROM morador WHERE cpf= '" + cpfa + "'")

	df=pd.read_sql_query("""SELECT * FROM morador""",conexao)
	opcoes = {}                # as opções são definidas em um dicionário
	opcoes['initialdir'] = ''    # será o diretório atual
	opcoes['parent'] = tlogin
	opcoes['title'] = 'Escolha um local para salvar'
	caminhoinicial = fdlg.askdirectory(**opcoes)
	df.to_excel(caminhoinicial +'/Relatorio-Usuarios-.xlsx', index=False)


	#df = df.append(data)	
	for linha in c:
		global cpf_buscado
		global senha_buscado
		global tipo_buscado
		global nome_buscado
		global email_buscado
		cpf_buscado = linha[0]
		cpf_mudado = cpf_buscado.replace(cpf_buscado[0:5],"*****")
		nome_buscado = linha[1]
		email_buscado = linha[9]
		tipo_buscado = linha[2]
		senha_buscado = linha[8]
		tb_movimento.insert("","end",values=(cpf_mudado,nome_buscado,email_buscado,senha_buscado))
		'''print(cpf_buscado)
		print(nome_buscado)
		print(email_buscado)
		print(fone_buscado)
		print(senha_buscado)'''


	#aqui seleciona a pasta a ser colocada o novo arquivo
	'''opcoes = {}                # as opções são definidas em um dicionário
	opcoes['initialdir'] = ''    # será o diretório atual
	opcoes['parent'] = ''
	opcoes['title'] = 'Diálogo que retorna o nome do diretório selecionado'
	caminhoinicial = fdlg.askdirectory(**opcoes)'''

	

	print("Junção Finalizada Realizado com sucesso!")
	
	
		

def verifica():
	select = selectUser('07429259430')
	'''tentativas = int(lbl_cliques.cget("text"))
	try:
		usuariosel = text_usuario.get()
		senhasel = text_senha.get()
		if usuariosel == "ADM" and senhasel == "07429259430":
			adiciona = insertUser('07429259430','Marciel Bezerra','marciel@gmail','ADM','lua1106')
			tk.messagebox.showinfo("ADM", "Adm Marciel cadastrado!")
			text_usuario.delete(0,END)
			text_senha.delete(0,END)
		elif usuariosel == "" or senhasel == "":
			text_usuario.delete(0,END)
			text_senha.delete(0,END)
			tentativas += 1
			lbl_cliques.config(text=str(tentativas))
			tk.messagebox.showerror("Erro", "Favor verifique suas credenciais, " + str(tentativas) + " tentativas de 3")
			if tentativas >= 3:
					tlogin.destroy()
		else:
			select = selectUser(usuariosel)
			
			if usuariosel == cpf_buscado and senhasel == senha_buscado:
				tlogin.destroy()
				app = App()
				
			else:				
				text_usuario.delete(0,END)
				text_senha.delete(0,END)
				tentativas = tentativas + 1
				lbl_cliques.config(text=str(tentativas))
				tk.messagebox.showerror("Erro", "Favor verifique suas credenciais, " + str(tentativas) + " tentativas de 3")
				if tentativas >= 3:
					tlogin.destroy()
	except:
		text_usuario.delete(0,END)
		text_senha.delete(0,END)
		tentativas += 1
		tk.messagebox.showerror("Erro", "Favor verifique suas credenciais, " + str(tentativas) + " tentativas de 3")
		if tentativas >= 3:
			tlogin.destroy()'''

	

def cancelando():
	os._exit(1)



def enter_apert(event):
	verifica()

def relatorio():
	caminhoinicial = '.\\arquivos'
	conexao = sqlite3.connect('bancoUsuario.db')
	df=pd.read_sql_query("""SELECT * FROM usuarios""",conexao)
	df.to_excel(caminhoinicial +'/Relatorio-Usuarios-.xlsx', index=False)
	c.close()



tlogin = tk.Tk()
tlogin.geometry("1500x900+100+150")
tlogin.title("MB - PORTARIA ")
tlogin['bg'] = 'DodgerBlue'
tlogin.iconphoto(True, PhotoImage(file='./arquivos/MB.png'))
image3=PhotoImage(file='./arquivos/MB.png')




lbl_bemvindo= Label(tlogin, bg ='DodgerBlue',image=image3,compound = TOP,text= 'Favor entre com suas credenciais!',fg='black',font=('arial',25,'bold'))
lbl_bemvindo.place(relx=0.05, rely = 0.0)
bullet = "*"
text_usuario=Entry(tlogin, bg='White',justify="center",show=bullet,text="Usuário", fg='black',font=('arial',14,'bold'))
text_usuario.place(relx=0.3, rely = 0.8)
text_usuario.focus()
lbl_usuario=Label(tlogin, bg='DodgerBlue',text="Usuário", fg='black',font=('arial',14,'bold'))
lbl_usuario.place(relx=0.1, rely = 0.4)
'''
text_senha=Entry(tlogin, bg='White',show="*", fg='black',font=('arial',14,'bold'))
text_senha.place(relx=0.3, rely = 0.5)
text_senha.bind('<Return>', enter_apert)
lbl_senha=Label(tlogin, bg='DodgerBlue',text="Senha", fg='black',font=('arial',14,'bold'))
lbl_senha.place(relx=0.1, rely = 0.5)

lbl_cliques=Label(tlogin, bg='DodgerBlue',text="0", fg='black',font=('arial',14,'bold'))'''

#tabela tb_movimento
global tb_movimento

frame = Frame(tlogin,bg='SkyBlue')
frame.place(relx=0.05, rely = 0.1)
titu_dep=Label(frame,width=25,bd=4,bg='SkyBlue', height=2,text= 'Entradas e Saidas do dia ',fg='black',font=('arial',14,'bold'))
titu_dep.pack(side=TOP)
tb_movimento = ttk.Treeview(frame, column=(1,2,3,4), show='headings', height=10)
tb_movimento.pack(side=LEFT)
#tb_movimento.heading('#0', text='', anchor=CENTER)
tb_movimento.heading(1, text='Cpf')
tb_movimento.heading(2, text='Nome')
tb_movimento.heading(3, text='RG')
tb_movimento.heading(4, text='CPF Responsavel')
sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)
tb_movimento.config(yscrollcommand=sb.set)
sb.config(command=tb_movimento.yview)
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")


btn_cadastro = Button(tlogin,bg='DodgerBlue',bd=8,compound = TOP, text="   Entrar  ", fg='black',font=('arial',14,'bold'),command=verifica)
btn_cadastro.place(relx=0.1, rely = 0.8)

btn_cancelar = Button(tlogin,bg='DodgerBlue',bd=8,compound = TOP, text="   Cancelar  ", fg='black',font=('arial',14,'bold'),command=cancelando)
btn_cancelar.place(relx=0.6, rely = 0.8)

#cria = createTableUsuarios()
#adiciona = selectUser('07429259430')
tlogin.mainloop()

#adiciona = relatorio()