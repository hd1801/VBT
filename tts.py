from gtts import gTTS
import os
import playsound
def texttospeech(word):
    if os.path.exists(word+".mp3"):
        p =os.path.abspath(word+".mp3")
        playsound.playsound(p,True)
    else:
        pronunciation=gTTS(text=word, lang='en',slow=True)
        pronunciation.save(word+".mp3")
        texttospeech(word)