from playsound import playsound
from gtts import gTTS





voz = gTTS("oi, sou Jegues! eu novamente?", lang="pt")
voz.save("responde.mp3")
playsound('responde.mp3')