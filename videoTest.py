import cv2

cap = cv2.VideoCapture(0)

ret,img = cap.read()

h,w,c = img.shape

res = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)

hn,wn,cn = res.shape

print h," ",w
print hn," ",wn

