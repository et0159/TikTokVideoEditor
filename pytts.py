import pyttsx3
import tempfile
from moviepy.editor import *
from pydub import AudioSegment
from pathlib import Path
from mutagen.mp3 import MP3
import os
import re
from pymediainfo import MediaInfo


def textToSpeech(textList):
    dirpath = tempfile.mkdtemp()
    print(dirpath)
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")[1] 
    engine.setProperty('voice', voices)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 20)
    for index, text in enumerate(textList, 1):
        #print(text)
        engine.save_to_file(text, 'temp/audios/audio' + str(index) + '.wav')
        engine.runAndWait()

def createSilenceAudio():
    video = AudioFileClip("temp/audios/audio0.mp3")
    silencedVideo = video.without_audio()
    silencedVideo = silencedVideo.subclip(0, 1)
    silencedVideo.write_videofile("temp/audios/silence.mp4")

#https://stackoverflow.com/questions/65502022/how-do-i-find-the-length-of-a-sound-generated-by-pyttsx3
#https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
def getVideoLength():
    lengthOfVideo = 0
    for index in range(len(os.listdir('temp/audios'))):
        file_to_open = os.listdir('temp/audios')[index]
        audio = AudioSegment.from_file('temp/audios/' + file_to_open)
        lengthOfVideo += audio.duration_seconds + 1
    return lengthOfVideo

