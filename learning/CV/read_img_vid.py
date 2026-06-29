import cv2
import mediapipe as mp
import time

# Load an image
img = cv2.imread("D:/WORK AND STUDY/projects/MACHINE-LEARNING/learning/CV/assets/hand.jpg")

if img is None:
    print("Image not found. Check the path spelling!")
else:
    cv2.imshow("hand", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the webcam
framewidth = 640
frameheight = 360  

cap = cv2.VideoCapture(0)
cap.set(3, framewidth)   # set width
cap.set(4, frameheight)  # set height

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    cv2.imshow("webcam", img)

    # press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
