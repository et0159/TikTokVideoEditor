from cmath import e, nan
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from math import nan, isnan
import pandas as pd
import time

from tempfolder import *
from pytts import *
from background import *
from videomaker import * 

excel_file = 'redditpost.xlsx'
url = "https://www.youtube.com/watch?v=kJawWyRUOBM&ab_channel=GameSpot"
PATH = ""


def main(): 

    df = pd.read_excel(excel_file, header = 0)

    l1 = []
    textList = []

    for index, row in df.iterrows():
        l1 = row.to_list()
        for i in l1:
            #print(i)
            if isinstance(i, str):
                textList.append(i)
    
    createTempFolders()
    textToSpeech(textList)

    #adding 1 second for the length of each video to account for the pause
    lengthOfVideo = getVideoLength()
    print("Length of Video: " + str(lengthOfVideo))

    backgroundVideo = downloadBackgroundVideo(url)
    print(backgroundVideo)
    print("Downloaded background video")

    #middle parameter takes in which minute you want the video to start at
    shortenedVideo = shortenLengthOfVideo(backgroundVideo, 1, lengthOfVideo)
    print(shortenedVideo)
    print("Shortened Video")

    resizedVideo = resizeVideo(shortenedVideo)
    print("Resized Video")

    concatenatedAudios = concatenateAudios()
    print("Concatenated Audios")

    videoWithAudio = addAudioToVideo(resizedVideo, concatenatedAudios)
    print("Added audio to videos")

    createVideo(videoWithAudio)
    print("Created final video")

main()