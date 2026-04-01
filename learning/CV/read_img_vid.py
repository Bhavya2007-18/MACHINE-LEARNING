import cv2
import mediapipe as mp
import time
# to see an image
img = cv2.imread("/home/bhavyaporwal007/work and study/MACHINE-LEARNING/learning/CV/resources/hand.jpg")

cv2.imshow("hand" , img)
cv2.waitKey(0)

#to run the webcam

#1. define the frame size
framewidth = 640
frameheight = 360  

cap=cv2.VideoCapture(0)
while True:
    success, img = cap.read()

    cv2.imshow("webcam" , img)
    # press q to exit   

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
