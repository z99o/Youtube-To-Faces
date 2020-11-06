import cv2
import os

#
#
#	Stand Alone Image Resizer
#
#


INPUT_DIR = input("Input Folder: ")
OUTPUT_DIR = input("Output Folder (Will be Created In Root If It Doesn't Exist): ") + "/"
X_DIMS = int(input("X Dimensions To Resize Images To: "))
Y_DIMS = int(input("Y Dimensions To Resize Images To: "))


def Create_Dir(path):
    if not os.path.exists(path):
        print("New directory created")
        os.makedirs(path)


Create_Dir(OUTPUT_DIR)
count = 0
for file in os.listdir(INPUT_DIR):
    image = cv2.imread(INPUT_DIR + "/" + file)
    output = cv2.resize(image, (X_DIMS, Y_DIMS))
    out = OUTPUT_DIR + "_resized_" + file
    cv2.imwrite(out, output)
    count += 1
