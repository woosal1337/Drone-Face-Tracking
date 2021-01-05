import cv2
import numpy as np

# Finding the face phase
def findFace(img):




cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)