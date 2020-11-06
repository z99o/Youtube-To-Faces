from __future__ import unicode_literals
import youtube_dl
import cv2
import os

#
#
#      Standalone Video To Frame Converter
#
#

ydl_opts = {}

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
url = input("Youtube URL: ")

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

output_dir = input("Output Path: ")
if not os.path.exists(output_dir):
    print("New directory created")
    os.makedirs(output_dir)

vid_cap = cv2.VideoCapture(url)
success, image = vid_cap.read()
count = 0

numFrame = input("Frames To Skip (3 - 5 Recommended): ")
while success:
    success, image = vid_cap.read()
    if count % numFrame == 0:
        cv2.imwrite(output_dir + "/" + url + "frame%d.jpg" % count, image)  # save frame as JPEG file
        print('Read a new frame: ' + str(count) + " ", success)
    count += 1

