from gtts import gTTS
import os
import playsound
def texttospeach(word):
    pronunciation=gTTS(text=word, lang='en',slow=True)
    pronunciation.save(word+".mp3")
    p =os.path.abspath(word+".mp3")
    playsound.playsound(p,True)

