from tkinter import *
import tkinter as tk
import threading
import time
import speech_recognition as sr
import pyaudio
import wave
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        tinicial = tk.Tk()
        tinicial.geometry("800x500+200+100")
        tinicial.title("Tela de testes - SIS")
        tinicial.resizable(width=False, height=False)
        tinicial['bg'] = '#49A'
        tinicial.iconphoto(True, PhotoImage(file='./arquivos/robo1.png'))
        image=PhotoImage(file='./arquivos/robo1.png')
        global robozinho
        global falinha
        robozinho = Label(tinicial, image = image,width=800, height=500,bg ='black')
        robozinho.grid(row=5,columnspan =9)
        falinha= Label(tinicial, width=40, height=2,bg ='black',text= 'Olá meu nome é Jegue',fg='white',font=('arial',14,'bold'))
        falinha.place(relx=0.33, rely = 0.16)




        tinicial.mainloop()


    

app = App()

def ouvir_microfone():
        jegue = "Sou todo ouvidos: "
        #Habilita o microfone para ouvir o usuario
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            #Chama a funcao de reducao de ruido disponivel na speech_recognition
                while True:
                    microfone.adjust_for_ambient_noise(source)
                    #Avisa ao usuario que esta pronto para ouvir
                    #print(jegue)
                    
                    image=PhotoImage(file='./arquivos/robo3.png')
                    robozinho.config(image=image)
                    robozinho.image = image
                    falinha.config(text=jegue)
                    #Armazena a informacao de audio na variavel
                    audio = microfone.listen(source)
                    
                    try:
                        #Passa o audio para o reconhecedor de padroes do speech_recognition
                        frase = microfone.recognize_google(audio,language='pt-BR')
                        #Após alguns segundos, retorna a frase falada
                        #print("Você disse: " + frase)

                        falinha.config(text="Você disse: " + frase)
                        image=PhotoImage(file='./arquivos/robo1.png')
                        robozinho.config(image=image)
                        robozinho.image = image
                        time.sleep(1)
                        google = 'Google' in frase
                        pesquisar = frase.find('pesquisa')
                        procura =frase[pesquisar+8:]
                        if google ==True:

                            falinha.config(text="Pesquisando por " + procura)

                            driver = webdriver.Chrome()
                            driver.get("https://www.google.com/")
                            caixalogin = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
                            time.sleep(1)
                            caixalogin.send_keys(procura)

                            botao = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
                            botao.click()
                            time.sleep(10)

                            driver.quit()

                        else:
                            pass
                    #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
                    except :
                        #print("Você falou algo?")
                        falinha.config(text="Você falou algo?")
                        image=PhotoImage(file='./arquivos/robo2.png')
                        robozinho.config(image=image)
                        robozinho.image = image
                #return frase
        return ouvir_microfone


ouvir_microfone()
