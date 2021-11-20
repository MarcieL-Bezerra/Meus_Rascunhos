import speech_recognition as sr
import pyaudio
import wave
import os
import threading
import tkinter as tk
from tkinter import *

tinicial = tk.Tk()
tinicial.geometry("800x500+200+100")
tinicial.title("Tela de testes - SIS")
tinicial.resizable(width=False, height=False)
tinicial['bg'] = '#49A'
tinicial.iconphoto(True, PhotoImage(file='./arquivos/robo1.png'))
image=PhotoImage(file='./arquivos/robo1.png')

#Funcao responsavel por ouvir e reconhecer a fala
jegue = "Jegue diz: Sou todo ouvidos: "
tinicial.mainloop()
def ouvir_microfone():
  
        #Habilita o microfone para ouvir o usuario
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            #Chama a funcao de reducao de ruido disponivel na speech_recognition
                while True:
                    microfone.adjust_for_ambient_noise(source)
                    #Avisa ao usuario que esta pronto para ouvir
                    print(jegue)
                    #Armazena a informacao de audio na variavel
                    audio = microfone.listen(source)
                    
                    try:
                        #Passa o audio para o reconhecedor de padroes do speech_recognition
                        frase = microfone.recognize_google(audio,language='pt-BR')
                        #Após alguns segundos, retorna a frase falada
                        print("Você disse: " + frase)
                        procurada = 'começa' in frase
                        if procurada ==True:
                            print('começou')
                        else:
                            pass
                    #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
                    except :
                        print("Você falou algo?")
                      
                #return frase
        return ouvir_microfone


ouvir_microfone()


