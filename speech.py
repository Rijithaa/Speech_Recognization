from gtts import gTTS
import os
mytext = "Hi you are started learning AI/ML"
language = "en"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("Welcome.mp3")
os.system("Start welcome.mp3")