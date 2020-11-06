import cv2
import os


FRAMES_DIR = input("Input Dir: ") + "/face"
FACES_DIR = input("Output Dir: ")

if not os.path.exists(FRAMES_DIR):
    print("New directory created")
    os.makedirs(FACES_DIR)

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