import face_recognition
import os
from shutil import copyfile
#
#   Face_Recognition module sucks big donkey wang for getting datasets, often it will miss
#   entire video's worth of faces, you're better off manually parsing faces
#   You also need to run it on linux or jump through a bunch of bullshit to get it working on Win 10
#


persons_list = []
index = {}
potraits = {}
faces_in_image = {}
FACES_DIR = 'unprocessed_faces/' # Path to the sub-directory which contains the images
SORTED_DIR = "./sorted_faces/"
SAMPLE_DIR = "face_samples/"
SCAN_TOLERANCE = 0.25

def Create_Dir(path):
    if not os.path.exists(path):
        print("New directory created")
        os.makedirs(path)

Create_Dir(SORTED_DIR)

def Get_Files():
    files = []
    with os.scandir(FACES_DIR) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.name)
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    return files

print("Sorting Faces")
# Sort Faces
known_jermas = []
for sample in Get_Files(SAMPLE_DIR):
    j = face_recognition.load_image_file(SAMPLE_DIR + sample)
    known_jermas.append(face_recognition.face_encodings(j)[0])

files = Get_Files(FACES_DIR)
# Iterate through all the 10,460 pictures
for f in files:
    # Construct the picture name and print it
    file_path = FACES_DIR + f
    print(file_path)

    # Load this picture
    new_picture = face_recognition.load_image_file(file_path)

    # Iterate through every face detected in the new picture
    for face_encoding in face_recognition.face_encodings(new_picture):

        # Run the algorithm of face comaprison for the detected face, with SCAN_TOLERANCE tolerance
        results = face_recognition.compare_faces(known_jermas, face_encoding, SCAN_TOLERANCE)

        # Save the image to a seperate folder if there is a match
        if results[0] == True:
            print("saving as " + file_path)
            copyfile(file_path, SORTED_DIR + f)
        # Remove File
    try:
        os.remove(file_path)
    except Exception as e:
        print(e)

