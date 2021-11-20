from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "bom dia esse é um teste do meu robozinho!"
        self.grupos_ou_pessoas = ["Grupo Teste", "Meus Arquivos"]
        options = webdriver.ChromeOptions()
        #options.add.argument('lang=pt-br')
        self.driver = webdriver.Chrome("F:\Meus Python\Robozinho Whats\chromedriver.exe")

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30) 
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_13mgZ')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)

            #botao
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)
             
bot = WhatsappBot()
bot.EnviarMensagens()
        
        
