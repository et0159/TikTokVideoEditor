from gtts import gTTS
import os
import tempfile


def textToSpeech(textList):
    dirpath = tempfile.mkdtemp()
    print(dirpath)
    counter = 0
    for index, i in enumerate(textList, 0):
        counter += 1
        audio = gTTS(text=i, lang="en", slow=False)
        audio.save("text_{0}.mp3".format(index))

        #print("text" + str(counter) + " here")
        #os.system("start " + "text" + str(counter) + ".mp3")
        #print("KSAFKJDASKJGFDAKHKF")