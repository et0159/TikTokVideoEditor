import os
from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import crop

numberOfThreads = 4

def downloadBackgroundVideo(url):
    ytVideo = YouTube(url)
    #print(ytVideo)
    ytvideo1 = ytVideo.streams.filter(adaptive=True, file_extension='mp4', res="1080p", only_video=True).first().download('temp/backgroundvideo')
    return ytvideo1

#downloadBackgroundVideo handles removing audio
#writing the videofile reecodes the file resulting in loss of quality and performance.
def removeAudio(originalVideo):
    video = VideoFileClip(originalVideo)
    newVideo = video.without_audio()
    #newVideo.write_videofile('temp/backgroundvideo/newvideo.mp4', logger=None)
    return newVideo

#Finds the proper amount of seconds to have the background video
# startpfvideo * 60 = amount of minutes
def shortenLengthOfVideo(originalVideo, startOfVideo, lengthOfVideo):
    clip = VideoFileClip(originalVideo)
    startOfVideoInMinutes = startOfVideo * 60
    clip = clip.subclip(startOfVideoInMinutes, startOfVideoInMinutes + lengthOfVideo)
    #clip.write_videofile("temp/backgroundvideo/clip.mp4", codec='libx264', bitrate="15000k", threads=numberOfThreads)
    return clip

#crops the video to TikTok format
def resizeVideo(videoClip):
    clip = videoClip
    height = videoClip.h
    width = videoClip.w
    (w, h) = clip.size

    #https://www.reddit.com/r/moviepy/comments/7kervd/how_to_crop_a_centered_square_with_moviepy/
    cropClip = crop(clip, width=596, height=1060, x_center=w/2, y_center=h/2)
    
    return cropClip


