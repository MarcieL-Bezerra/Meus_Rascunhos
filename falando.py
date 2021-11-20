from gtts import gTTS
import subprocess as s
import sys
import vlc
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer







voz = gTTS("oi, sou Jegue! Posso ajudar?", lang="pt")
voz.save("voz.mp3")
falar = "voz.mp3"
tocar = vlc.MediaPlayer(falar)
tocar.play()  

bot = ChatBot('Jegue')
bot = ChatBot(
    'Jegue',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )
    
conversa = ListTrainer(bot)
conversa.train([
    'Oi?',
    'Eae',
    'Qual o seu nome?',
    'Meu nome é Jegue',
    'Prazer em te conhecer',
    'Igualmente meu patrão',
    'lindo','conhece'
])
while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Jegue: ", resposta)
            resp = gTTS(str(resposta), lang="pt")
            resp.save("responde.mp3")
            falar = "responde.mp3"
            tocar = vlc.MediaPlayer(falar)
            tocar.play()
        else:
            print("Eu não entendi :(")
            voz = gTTS("Dificilmente entenderia, a final, sou Jegue!", lang="pt")
            voz.save("voz.mp3")
            falar = "voz.mp3"
            tocar = vlc.MediaPlayer(falar)
            tocar.play()            
            
    except(KeyboardInterrupt, EOFError, SystemExit):
        break




