import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret,img = cap.read()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
unroll  = img.reshape(1,307200).astype(np.float32)
cap.release()