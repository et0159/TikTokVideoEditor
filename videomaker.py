import os
from os.path import exists
from moviepy.editor import VideoFileClip
from moviepy.editor import *

oneSecondPause = AudioFileClip("assets/1-second-of-silence.mp3")
pause = oneSecondPause.subclip(0, 0.7)
numberOfThreads = 8
audios = []


def concatenateAudios():
    counter = 1 
    while os.path.exists("temp/audios/audio" + str(counter) +".wav"):
        audio = AudioFileClip("temp/audios/audio" + str(counter) + ".wav")
        audios.append(audio)
        audios.append(pause)
        counter += 1
    
    concatenatedAudios = concatenate_audioclips([audio for audio in audios])
    return concatenatedAudios

def addAudioToVideo(backgroundVideo, ttsAudio):
    backgroundVideo.audio = CompositeAudioClip([ttsAudio])
    return backgroundVideo 

def createVideo(video):

    finalVideo = video

    videoHeight = video.h
    videoWidth = video.w

    print("Video height: " + str(videoHeight))
    print("Video Width: " + str(videoWidth))

    counter = 1
    time = 0
    while os.path.exists("images/image" + str(counter) + ".png") and os.path.exists("temp/audios/audio" + str(counter) +".wav"):

        audio = AudioFileClip("temp/audios/audio" + str(counter) + ".wav")

        image1 = (ImageClip("images/image" + str(counter) + ".png"))
        print()
        print("Image" + str(counter) + "height: " + str(image1.h))
        print("Image" + str(counter) + "width: " + str(image1.w))
        
        image = (ImageClip("images/image" + str(counter) + ".png")
            .set_duration(audio.duration)
            .resize(width = videoWidth * 0.70) 
            .margin(right=12, left=63, opacity=0) 
            .set_pos((0, 0.20), relative = True)
            .set_start(time)
            .set_end(time + audio.duration))

        print("Resized Image " + str(counter) + "height: " + str(image.h))
        print("Resized Image " + str(counter) + "width: " + str(image.w))
        
        finalVideo = CompositeVideoClip([finalVideo, image])

        time += pause.duration + audio.duration
        counter += 1

    finalVideo.write_videofile("temp/finishedvideo/finalVideo.mp4", codec='libx264', bitrate="15000k", threads=numberOfThreads)


