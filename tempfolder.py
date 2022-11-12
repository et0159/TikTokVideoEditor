from os import mkdir
from os import path
from shutil import rmtree

def createTempFolders():
    if path.exists('temp'):
        rmtree('temp')

    mkdir('temp')
    mkdir('temp/backgroundvideo')
    mkdir('temp/audios')
    mkdir('temp/finishedvideo')

def deleteTempFolders(path):
    if path.exist(path):
        rmtree(str)