import cv2

path ="/home/bhavyaporwal007/work and study/MACHINE-LEARNING/learning/CV/resources/hand.jpg"

img = cv2.imread(path,0) #the zero turns image to greyscale


imgBlur= cv2.GaussianBlur(img,(9,9),0)

imgCanny = cv2.Canny(imgBlur,10,10)

cv2.imshow("Canny", imgBlur)
cv2.imshow("greyscale", img)
cv2.imshow("blur", imgBlur)
cv2.imshow("image" , img)
cv2.waitKey(0)