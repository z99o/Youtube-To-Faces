from __future__ import unicode_literals
from shutil import copyfile
import face_recognition
import youtube_dl
import cv2
import os


def Create_Dir(path):
    if not os.path.exists(path):
        print("New directory created")
        os.makedirs(path)


def Get_Files(input_path):
    files = []
    with os.scandir(input_path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.name)
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    return files


# VARIABLES
VIDEOS_DIR = "videos/"
FACES_DIR = "unsorted_faces/"
SAMPLE_DIR = "face_samples/"
SORTED_DIR = "sorted_faces/"
SCAN_TOLERANCE = 0.15
VIDEO_FRAME_SKIP = 5 #Number of frames to skip for video scanning

video_list = []
with open("urls.txt") as l:
    video_list = l.readlines()

for i in video_list:
    i.replace('\n','')

for video in video_list:
    VIDEO_URL = video
    print("Downloading Video...")
    # Downloader
    ydl_opts = {}
    url = VIDEO_URL
    video_path = ""
    video_title = ""
    retry = 1
    while retry:
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                video_title = info_dict.get('title', None)
                video_path = VIDEOS_DIR
                ydl_opts = {'outtmpl': video_path + video_title}
                youtube_dl.YoutubeDL(ydl_opts).download([url])
                retry = 0
        except youtube_dl.utils.DownloadError as e: #Replace exception with the error that happens ocassionally
            print("Youtube errored: ",e)
            retry = 1


    print("Converting Video to Frames")
    print("Processing Faces...")
    # Video To Frames
    Create_Dir(FACES_DIR)
    vid_cap = cv2.VideoCapture(video_path + video_title)
    success, image = vid_cap.read()
    count = 0
    numFrame = VIDEO_FRAME_SKIP
    # Send one frame for every 5 to FRAMES DIR
    while success:
        success, image = vid_cap.read()
        if count % numFrame == 0:
            out = FACES_DIR + video_title + "frame%d.jpg" % count
            print("saving as " + out)
            try:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # Set Parameters here
                faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.05,
                    minNeighbors=3,
                    minSize=(110, 110),
                )
                # print("Found {0} Faces!".format(len(faces)))
                for (x, y, w, h) in faces:
                    roi_color = image[y:y + h, x:x + w]
                    # print("[INFO] Object found. Saving locally.")
                    print("saving as " + out)
                    cv2.imwrite(out, roi_color)
                # Remove File
            except cv2.error as e:
                print("Went too many frames over maybe? " + str(e))
            print('Read a new frame: ' + str(count) + " ", success)
        count += 1




