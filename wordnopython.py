from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import speech_recognition as sr
import time
from selenium.webdriver.support.ui import Select


pergunta = 'A alteração dos dados por pessoa/software/processo não autorizado em um data center, por exemplo, pode ser considerada uma ameaça da:'
URL= 'https://brainly.com.br/app/ask?entry=hero&q='
global driver
option = Options()
option.headless = True

driver = webdriver.Chrome(options=option)
driver.get(URL+pergunta)
pergunta=pergunta.strip()
pergunta=pergunta.split()
pergunta=format(pergunta[len(pergunta)-1])

#botao = driver.find_element_by_css_selector("div.sg-text")
botao = driver.find_element_by_partial_link_text('autorizado')


#botao = select.select_by_visible_text('div/a/div')
driver.execute_script("arguments[0].click();", botao)
time.sleep(4)

respostaPri = driver.find_element_by_xpath('//*[@id="question-sg-layout-container"]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div/p[2]')
respostaseg = driver.find_element_by_xpath('//*[@id="question-sg-layout-container"]/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/div/div/p[2]')
respConfirmada = "resposta: "+respostaPri.text+" Confirmando a resposta: " + respostaseg.text

print(respConfirmada)
driver.quit()

'''
microfone.adjust_for_ambient_noise(source)
image=PhotoImage(file='./arquivos/robo3.png')
robozinho.config(image=image)
robozinho.image = image
audio = microfone.listen(source)




falinha.config(text="Fale a questão pausadamente ")


obterRespos = gTTS(str(respConfirmada), lang="pt")
obterRespos.save('./conversas/obterRespos'+ str(contandos) + '.mp3')
playsound('./conversas/obterRespos'+ str(contandos) + '.mp3')

ouvir_microfone()
break'''