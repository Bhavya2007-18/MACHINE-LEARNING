import cv2
import mediapipe as mp
from mediapipe.python.solutions.hands import Hands
import time

cap=cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime=0
cTime=0





while True:



    success, img = cap.read()
    imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for _handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img , _handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255), 3)

    cv2.imshow("image" , img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()   
