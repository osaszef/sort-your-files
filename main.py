import time
import os
from shutil import move
import json

file = open("./config.json", "r")
data = json.load(file)

for img in data["image"]:
    getEnabledIMG = img["enabled"]
    imageDir = img["imageDirectory"]
    imageExtensions = img["imageExtension"]

for vid in data["video"]:
    getEnabledVID = vid["enabled"]
    videoDir = vid["videoDirectory"]
    videoExtensions = vid["videoExtension"]

desktop = data["baseDirectory"]

#---

if not os.path.exists(imageDir):
    os.mkdir(imageDir)
if not os.path.exists(videoDir):
    os.mkdir(videoDir)


def checkForImage(fileName):
        for extension in imageExtensions:
            if fileName.endswith("." + extension):
                move(desktop + fileName, imageDir)

def checkForVideo(fileName):
    for extension in videoExtensions:
        if fileName.endswith("." + extension):
            move(desktop + fileName, videoDir)

if not imageDir:
    print("[ERROR] Please enter a IMAGE directory in config file")
if not videoDir:
    print("[ERROR] Please enter a VIDEO directory in config file")

else:
    while True:
        if os.path.exists(desktop):
            for file in os.listdir(desktop):
                if getEnabledIMG == 1:
                    checkForImage(file)
                if getEnabledVID == 1:
                    checkForVideo(file)
        else:
            print("[ERROR] Could not find base directory! Please enter a BASE DIRECTORY in config file")
            break
            
        time.sleep(1)