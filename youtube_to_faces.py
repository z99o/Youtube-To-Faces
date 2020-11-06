from __future__ import unicode_literals
from shutil import copyfile
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
VIDEOS_DIR = str(input("Video Output Directory: ") or "videos") + "/"
FRAMES_DIR = str(input("Frame Output Directory: ") or "frames") + "/"
FACES_DIR = str(input("Faces Output Directory: ") or "unsorted_faces") + "/"
SCAN_TOLERANCE = 0.15
VIDEO_FRAME_SKIP = 5  # Number of frames to skip for video scanning

video_list = []
with open("urls.txt") as l:
    video_list = l.readlines()

for i in video_list:
    i.replace('\n', '')
print(video_list)
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
                ydl_opts = {'outtmpl': video_path + video_title + ".mp4"}
                youtube_dl.YoutubeDL(ydl_opts).download([url])
                retry = 0
        except youtube_dl.utils.DownloadError as e:  # Replace exception with the error that happens ocassionally
            print("Youtube errored: ", e)
            retry = 1

    print("Converting Video to Frames")
    # Video To Frames
    Create_Dir(FRAMES_DIR)
    vid_cap = cv2.VideoCapture(video_path + video_title + ".mp4")
    success, image = vid_cap.read()
    count = 0
    numFrame = VIDEO_FRAME_SKIP
    # Send one frame for every 5 to FRAMES DIR
    while success:
        success, image = vid_cap.read()
        if count % numFrame == 0:
            out = FRAMES_DIR + video_title + "_frame%d.jpg" % count
            print("saving as " + out)
            try:
                cv2.imwrite(out, image)  # save frame as JPEG file
            except cv2.error as e:
                print("Went too many frames over maybe? " + str(e))
            print('Read a new frame: ' + str(count) + " ", success)
        count += 1

    # Process Faces
    Create_Dir(FACES_DIR)
    print("Processing Faces...")
    for file in os.listdir(FRAMES_DIR):
        name = file
        image = cv2.imread(FRAMES_DIR + file)
        # print(name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Set Parameters here
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        # Tweak these parameters, and look up what this function takes if you want to fine tune the faces you get
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=3,
            minSize=(110, 110),
        )
        for (x, y, w, h) in faces:
            roi_color = image[y:y + h, x:x + w]
            output_name = FACES_DIR + "_" + name
            print("saving as " + output_name)
            cv2.imwrite(output_name, roi_color)
        # Remove File
        try:
            os.remove(FRAMES_DIR + file)
        except Exception as e:  # Sometimes it gets boned so I did this horrible catch all
            print(e)
        if not os.listdir(FRAMES_DIR):
            print("If this part of the script stops processing faces and freezes, that means its done\n" +
                  "I cant figure out for the life of me why it does that since it only does it on Win 10")