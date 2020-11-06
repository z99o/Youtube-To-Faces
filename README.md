# Youtube To Faces
 Takes youtube links and extracts the faces


PRE-REQUISITES
-
Have python 3.7 or higher installed

INSTRUCTIONS FOR RUNNING:
-
1. Navigate to the source directory

2. Open urls.txt

3. Enter the urls you want to extract faces from, seperated by a new line

4. Save urls.txt

5. Run:
    ```bash
    pip install -r requirements.txt
    python youtube_to_faces
    ```
6. Follow the prompts

SCRIPT FUNCTIONS 
-
**youtube_to_faces:**

youtube_to_faces takes youtube links from urls.txt and extracts faces from them

The script is a combinations of the following included scripts which can be run standalone:

*   youtube_downloader
*   video_to_frames
*   frames_to_faces

Other scripts:
*   face_sorter (really inconsistant)
*   renamer (fun tool to create 50k+ unique jerma names)
*   resize_tool (tool to resize a directory of images to given dimensions, useful for preparing ML batches)

To use any of these scripts simply run them in a command line after installing the required packages

The face_recognition module barely works for this use case dont use it unless you know how to use it (I don't), you also will need to run

it on linux or do some wacky windows stuff to get it working. My recommendation is to find a script that sorts images by similarity. 

I used https://github.com/victorqribeiro/groupImg, which worked ok, but if you can find a really good one, make an Issue so others know

Support
-

All of this was tested local on my computer so it might just not work on other pooters so just make a github issue if you're having problems and I'll try to help you



