import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

mpHands = mp.solution.hands
hands = mpHands.Hands()


while True:



    success, img = cap.read()




    cv2.imshow("image" , img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()   
