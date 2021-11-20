import time
import tkinter.messagebox as tkMessageBox
from selenium import webdriver
import tkinter as tk
from datetime import date
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from sons import finalfim



root = tk.Tk()
root.geometry("800x500+500+0")
root.resizable(width=False, height=False)
root.iconphoto(True, tk.PhotoImage(file='./arquivos/Brasil.png'))
root.title("Sistema Download")
root.configure(background="SKyBlue1")
root.focus_force()
root.grab_set()
image=tk.PhotoImage(file='./arquivos/whats.png')
#datas atuais
data_atual = date.today()
data_dmenos = date.today() + timedelta(days=-1)
primeiro_mes_atual=datetime(data_atual.year,data_atual.month,1)

	#datas passadas
primeiro_mes_passado=datetime(data_atual.year,data_atual.month-1,1)
ultimo_mes_passado = primeiro_mes_atual + timedelta(days=-1)



def reltotaldatasysatual ():
	#options = webdriver.ChromeOptions()
	#options.add_argument('--headless')
	#driver = webdriver.Chrome(executable_path=r'F:\Meus Python\Meus rascunhos\chromedriver.exe', options=options)
	#driver = webdriver.Chrome(chrome_options=options)
	driver = webdriver.Chrome()
	driver.get("https://tim.datasys.online/")
	time.sleep(2)
	login = '01235496473'
	senha = '198113'
	loja = "FACELL"
	
	wait = WebDriverWait(driver, 10)
	caixalogin = driver.find_element_by_name("edLogin")
	time.sleep(1)
	caixalogin.send_keys(login)


	caixasenha = driver.find_element_by_name("edSenha")
	time.sleep(1)
	caixasenha.send_keys(senha)

	caixadeloja = driver.find_element_by_name("edIdentificacao")
	caixadeloja.send_keys(loja)

	botao = driver.find_element_by_name("btAcessar")
	botao.click()
	time.sleep(10)

	wait = WebDriverWait(driver, 10)
	modulotim = driver.find_element_by_xpath('//*[@id="lkGC"]/div/div[1]/p')
	modulotim.click()
	#time.sleep(10)

	wait = WebDriverWait(driver, 10)
	modulotimrelatorio = driver.find_element_by_xpath('//*[@id="cl-wrapper"]/div[1]/div[2]/div[1]/div/ul/li[7]/a')
	modulotimrelatorio.click()
	#time.sleep(10)

	wait = WebDriverWait(driver, 10)
	modtimreltotati = driver.find_element_by_xpath('//*[@id="ctl00_body_lkRelTotalAtivacoes"]/u/b')
	modtimreltotati.click()
	#time.sleep(3)

	#gera mes atual
	wait = WebDriverWait(driver, 10)
	inicio_mes_atual=primeiro_mes_atual.strftime('%d/%m/%Y')
	time.sleep(10)

	#wait = WebDriverWait(driver, 15)
	caixadtini = driver.find_element_by_name('ctl00$body$wucFiltrosRelTotalAtivacoes$edDataInicio')
	caixadtini.send_keys(inicio_mes_atual)

	dia_dmenos = data_dmenos.strftime('%d/%m/%Y')

	caixadtfim = driver.find_element_by_name('ctl00$body$wucFiltrosRelTotalAtivacoes$edDataFim')
	time.sleep(5)
	caixadtfim.send_keys(dia_dmenos)


	mgerar = driver.find_element_by_id('ctl00_body_wucFiltrosRelTotalAtivacoes_lkPlanilha')
	mgerar.click()
	time.sleep(240)
	driver.quit()
	time.sleep(60)
	reltotaldatasysapassado()

def reltotaldatasysapassado ():

	#driver2 = webdriver.Firefox()
	driver2 = webdriver.Chrome()
	driver2.get("https://tim.datasys.online/")
	time.sleep(2)
	login = '01235496473'
	senha = '198113'
	loja = "FACELL"
	
	wait = WebDriverWait(driver2, 10)
	caixalogin = driver2.find_element_by_name("edLogin")
	time.sleep(0.5)
	caixalogin.send_keys(login)


	caixasenha = driver2.find_element_by_name("edSenha")
	time.sleep(0.5)
	caixasenha.send_keys(senha)

	caixadeloja = driver2.find_element_by_name("edIdentificacao")
	caixadeloja.send_keys(loja)

	botao = driver2.find_element_by_name("btAcessar")
	botao.click()
	time.sleep(5)

	wait = WebDriverWait(driver2, 10)
	modulotim = driver2.find_element_by_xpath('//*[@id="lkGC"]/div/div[1]/p')
	modulotim.click()
	time.sleep(5)

	wait = WebDriverWait(driver2, 10)
	modulotimrelatorio = driver2.find_element_by_xpath('//*[@id="cl-wrapper"]/div[1]/div[2]/div[1]/div/ul/li[7]/a')
	modulotimrelatorio.click()
	time.sleep(3)

	wait = WebDriverWait(driver2, 10)
	modtimreltotati = driver2.find_element_by_xpath('//*[@id="ctl00_body_lkRelTotalAtivacoes"]/u/b')
	modtimreltotati.click()
	

	#gera mes passado
	
	inicio_mes_passou = primeiro_mes_passado.strftime('%d/%m/%Y')
	time.sleep(10)
	caixadtini = driver2.find_element_by_name('ctl00$body$wucFiltrosRelTotalAtivacoes$edDataInicio')
	caixadtini.send_keys(inicio_mes_passou)

	fim_mes_passou = ultimo_mes_passado.strftime('%d/%m/%Y')
	time.sleep(1)
	caixadtfim = driver2.find_element_by_name('ctl00$body$wucFiltrosRelTotalAtivacoes$edDataFim')
	caixadtfim.send_keys(fim_mes_passou)
	time.sleep(1)

	mgerar2 = driver2.find_element_by_id('ctl00_body_wucFiltrosRelTotalAtivacoes_lkPlanilha')
	time.sleep(2)
	driver2.execute_script("arguments[0].click();", mgerar2)
	time.sleep(240)
	driver2.quit()
	time.sleep(60)
	relplanativdatasysatual()

	
	#tkMessageBox.showinfo("Busca Finalizada", message= "Realizado com sucesso!") 
	#driver.quit()
	
def relplanativdatasysatual ():
	#options = webdriver.ChromeOptions()
	#options.add_argument('--headless')
	#driver = webdriver.Chrome(executable_path=r'F:\Meus Python\Meus rascunhos\chromedriver.exe', options=options)
	#driver = webdriver.Chrome(chrome_options=options)
	driver = webdriver.Chrome()
	driver.get("https://tim.datasys.online/")
	time.sleep(2)
	login = '01235496473'
	senha = '198113'
	loja = "FACELL"
	
	wait = WebDriverWait(driver, 10)
	caixalogin = driver.find_element_by_name("edLogin")
	time.sleep(1)
	caixalogin.send_keys(login)


	caixasenha = driver.find_element_by_name("edSenha")
	time.sleep(1)
	caixasenha.send_keys(senha)

	caixadeloja = driver.find_element_by_name("edIdentificacao")
	caixadeloja.send_keys(loja)

	botao = driver.find_element_by_name("btAcessar")
	botao.click()
	time.sleep(10)

	wait = WebDriverWait(driver, 10)
	modulotim = driver.find_element_by_xpath('//*[@id="lkGC"]/div/div[1]/p')
	modulotim.click()
	#time.sleep(10)

	wait = WebDriverWait(driver, 10)
	modulotimrelatorio = driver.find_element_by_xpath('//*[@id="cl-wrapper"]/div[1]/div[2]/div[1]/div/ul/li[7]/a')
	modulotimrelatorio.click()
	#time.sleep(10)

	wait = WebDriverWait(driver, 10)
	modtimreltotati = driver.find_element_by_xpath('//*[@id="ctl00_body_lkRelPlanilhaAtivacoes"]/u/b')
	modtimreltotati.click()
	#time.sleep(3)

	#gera mes atual
	wait = WebDriverWait(driver, 10)
	inicio_mes_atual=primeiro_mes_atual.strftime('%d/%m/%Y')
	time.sleep(10)

	#wait = WebDriverWait(driver, 15)
	caixadtini = driver.find_element_by_name('ctl00$body$wucFiltrosRelPlanilhaAtivacoes$edDataInicio')
	caixadtini.send_keys(inicio_mes_atual)

	dia_dmenos = data_dmenos.strftime('%d/%m/%Y')

	caixadtfim = driver.find_element_by_name('ctl00$body$wucFiltrosRelPlanilhaAtivacoes$edDataFim')
	time.sleep(5)
	caixadtfim.send_keys(dia_dmenos)


	mgerar = driver.find_element_by_id('ctl00_body_wucFiltrosRelPlanilhaAtivacoes_lkPlanilha')
	mgerar.click()
	time.sleep(240)
	driver.quit()
	time.sleep(60)
	relplanativdatasysapassado()


def relplanativdatasysapassado ():

	#driver2 = webdriver.Firefox()
	driver2 = webdriver.Chrome()
	driver2.get("https://tim.datasys.online/")
	time.sleep(2)
	login = '01235496473'
	senha = '198113'
	loja = "FACELL"
	
	wait = WebDriverWait(driver2, 10)
	caixalogin = driver2.find_element_by_name("edLogin")
	time.sleep(0.5)
	caixalogin.send_keys(login)


	caixasenha = driver2.find_element_by_name("edSenha")
	time.sleep(0.5)
	caixasenha.send_keys(senha)

	caixadeloja = driver2.find_element_by_name("edIdentificacao")
	caixadeloja.send_keys(loja)

	botao = driver2.find_element_by_name("btAcessar")
	botao.click()
	time.sleep(5)

	wait = WebDriverWait(driver2, 10)
	modulotim = driver2.find_element_by_xpath('//*[@id="lkGC"]/div/div[1]/p')
	modulotim.click()
	time.sleep(5)

	wait = WebDriverWait(driver2, 10)
	modulotimrelatorio = driver2.find_element_by_xpath('//*[@id="cl-wrapper"]/div[1]/div[2]/div[1]/div/ul/li[7]/a')
	modulotimrelatorio.click()
	time.sleep(3)

	wait = WebDriverWait(driver2, 10)
	modtimreltotati = driver2.find_element_by_xpath('//*[@id="ctl00_body_lkRelPlanilhaAtivacoes"]/u/b')
	modtimreltotati.click()
	

	#gera mes passado
	
	inicio_mes_passou = primeiro_mes_passado.strftime('%d/%m/%Y')
	time.sleep(10)
	caixadtini = driver2.find_element_by_name('ctl00$body$wucFiltrosRelPlanilhaAtivacoes$edDataInicio')
	caixadtini.send_keys(inicio_mes_passou)

	fim_mes_passou = ultimo_mes_passado.strftime('%d/%m/%Y')
	time.sleep(1)
	caixadtfim = driver2.find_element_by_name('ctl00$body$wucFiltrosRelPlanilhaAtivacoes$edDataFim')
	caixadtfim.send_keys(fim_mes_passou)
	time.sleep(1)

	mgerar2 = driver2.find_element_by_id('ctl00_body_wucFiltrosRelPlanilhaAtivacoes_lkPlanilha')
	time.sleep(2)
	driver2.execute_script("arguments[0].click();", mgerar2)
	time.sleep(240)
	driver2.quit()
	time.sleep(60)
	relplanvendatasysatual ()

def relplanvendatasysatual ():
	#options = webdriver.ChromeOptions()
	#options.add_argument('--headless')
	#driver = webdriver.Chrome(executable_path=r'F:\Meus Python\Meus rascunhos\chromedriver.exe', options=options)
	#driver = webdriver.Chrome(chrome_options=options)
	driver = webdriver.Chrome()
	driver.get("https://tim.datasys.online/")
	time.sleep(2)
	login = '01235496473'
	senha = '198113'
	loja = "FACELL"
	
	wait = WebDriverWait(driver, 10)
	caixalogin = driver.find_element_by_name("edLogin")
	time.sleep(1)
	caixalogin.send_keys(login)


	caixasenha = driver.find_element_by_name("edSenha")
	time.sleep(1)
	caixasenha.send_keys(senha)

	caixadeloja = driver.find_element_by_name("edIdentificacao")
	caixadeloja.send_keys(loja)

	botao = driver.find_element_by_name("btAcessar")
	botao.click()
	time.sleep(10)

	wait = WebDriverWait(driver, 10)
	moduloadm = driver.find_element_by_xpath('//*[@id="lkADM"]/div/div[1]/h1')
	moduloadm.click()
	#time.sleep(10)

	wait = WebDriverWait(driver, 10)
	moduloadmrelatorio = driver.find_element_by_xpath('//*[@id="cl-wrapper"]/div[1]/div[2]/div[1]/div/ul/li[7]/a')
	moduloadmrelatorio.click()
	#time.sleep(10)

	wait = WebDriverWait(driver, 10)
	moduloadmrelatoven = driver.find_element_by_xpath('//*[@id="cl-wrapper"]/div[1]/div[2]/div[1]/div/ul/li[7]/ul/li[1]/a')
	moduloadmrelatoven.click()
	

	wait = WebDriverWait(driver, 10)
	modplanativreltotati = driver.find_element_by_xpath('//*[@id="ctl00_body_lkRelPlanilhaVendas"]/u/b')
	modplanativreltotati.click()
	#time.sleep(3)

	#gera mes atual
	wait = WebDriverWait(driver, 10)
	inicio_mes_atual=primeiro_mes_atual.strftime('%d/%m/%Y')
	time.sleep(10)

	#wait = WebDriverWait(driver, 15)
	caixadtini = driver.find_element_by_name('ctl00$body$wucFiltrosRelPlanilhaVendas$edDataIni')
	caixadtini.send_keys(inicio_mes_atual)

	dia_dmenos = data_dmenos.strftime('%d/%m/%Y')

	caixadtfim = driver.find_element_by_name('ctl00$body$wucFiltrosRelPlanilhaVendas$edDataFim')
	time.sleep(5)
	caixadtfim.send_keys(dia_dmenos)


	mgerar = driver.find_element_by_id('ctl00_body_wucFiltrosRelPlanilhaVendas_lkPlanilha')
	mgerar.click()
	time.sleep(240)
	driver.quit()
	time.sleep(60)
	relplanvendatasysapassado ()


def relplanvendatasysapassado ():

	#driver2 = webdriver.Firefox()
	driver2 = webdriver.Chrome()
	driver2.get("https://tim.datasys.online/")
	time.sleep(2)
	login = '01235496473'
	senha = '198113'
	loja = "FACELL"
	
	wait = WebDriverWait(driver2, 10)
	caixalogin = driver2.find_element_by_name("edLogin")
	time.sleep(0.5)
	caixalogin.send_keys(login)


	caixasenha = driver2.find_element_by_name("edSenha")
	time.sleep(0.5)
	caixasenha.send_keys(senha)

	caixadeloja = driver2.find_element_by_name("edIdentificacao")
	caixadeloja.send_keys(loja)

	botao = driver2.find_element_by_name("btAcessar")
	botao.click()
	time.sleep(5)

	wait = WebDriverWait(driver2, 10)
	moduloadm = driver2.find_element_by_xpath('//*[@id="lkADM"]/div/div[1]/h1')
	moduloadm.click()
	time.sleep(5)

	wait = WebDriverWait(driver2, 10)
	moduloadmrelatorio = driver2.find_element_by_xpath('//*[@id="cl-wrapper"]/div[1]/div[2]/div[1]/div/ul/li[7]/a')
	moduloadmrelatorio.click()
	time.sleep(3)

	wait = WebDriverWait(driver2, 10)
	modadmeltotven = driver2.find_element_by_xpath('//*[@id="cl-wrapper"]/div[1]/div[2]/div[1]/div/ul/li[7]/ul/li[1]/a')
	modadmeltotven.click()

	wait = WebDriverWait(driver2, 10)
	modplanativreltotati = driver2.find_element_by_xpath('//*[@id="ctl00_body_lkRelPlanilhaVendas"]/u/b')
	modplanativreltotati.click()
	#time.sleep(3)
	

	#gera mes passado
	
	inicio_mes_passou = primeiro_mes_passado.strftime('%d/%m/%Y')
	time.sleep(10)
	caixadtini = driver2.find_element_by_name('ctl00$body$wucFiltrosRelPlanilhaVendas$edDataIni')
	caixadtini.send_keys(inicio_mes_passou)

	fim_mes_passou = ultimo_mes_passado.strftime('%d/%m/%Y')
	time.sleep(1)
	caixadtfim = driver2.find_element_by_name('ctl00$body$wucFiltrosRelPlanilhaVendas$edDataFim')
	caixadtfim.send_keys(fim_mes_passou)
	time.sleep(1)

	mgerar2 = driver2.find_element_by_id('ctl00_body_wucFiltrosRelPlanilhaVendas_lkPlanilha')
	time.sleep(2)
	driver2.execute_script("arguments[0].click();", mgerar2)
	time.sleep(240)
	driver2.quit()
	
	terminouu = finalfim.tocafim()
	tkMessageBox.showinfo("Busca Finalizada", message= "Realizado com sucesso!") 
	#driver.quit()

robozinho = tk.Label(root, image = image,width=800, height=500,bg ="DarkSeaGreen3")
robozinho.grid(row=10,columnspan =10)

botaodat = tk.Button(root, width=15, height=2,bd=4,text = "Entrar Datasys",font=('arial',12,'bold'),bg ="DarkSeaGreen3", command=reltotaldatasysatual)
botaodat.grid(row=10, column=2)

botaovert = tk.Button(root, width=15, height=2,bd=4,text = "Entrar Vertex",font=('arial',12,'bold'),bg ="DarkSeaGreen3")
botaovert.grid(row=10, column=7)



root.mainloop()