import cv2
import os

#
#
#      Standalone Video To Frame Converter
#
#

url = input("Video Path: ")
vid_cap = cv2.VideoCapture(url)
success, image = vid_cap.read()
count = 0
output_dir = input("Output Path (Will be created if doeesn't Exist): ")

if not os.path.exists(output_dir):
    print("New directory created")
    os.makedirs(output_dir)

#   High frame rate / Longer videos should have
numFrame = input("Frames To Skip (3 - 5 Recommended): ")
while success:
    success, image = vid_cap.read()
    if count % numFrame == 0:
        cv2.imwrite(output_dir + "/" + url + "frame%d.jpg" % count, image)  # save frame as JPEG file
        print('Read a new frame: ' + str(count) + " ", success)
    count += 1
