import cv2
import numpy as np

videoFile = cv2.VideoCapture("video.mp4")  # For a video file

# Reading video file
while videoFile.isOpened():
    ret, frame = videoFile.read()  # frame is an image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame is gray", gray)
    key = cv2.waitKey(1)
    if key == ord("A") or key == ord("a"):
        break

videoFile.release()  # Break capturing frames
cv2.destroyAllWindows()

