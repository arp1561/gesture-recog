import cv2
import numpy as np 
import glob
import pygame
from pygame.locals import *

cap = cv2.VideoCapture(0)
count =0 
frame_count=0
storing_data=True

layer_size = np.int32([76800,64,32,4])

neural = cv2.ANN_MLP()
neural.create(layer_size)
neural.load('mlp.xml')


pygame.init()
display = pygame.display.set_mode((300,200))
display.fill((0,0,0))
counterForFrameSize=0

while storing_data:
	ret,videoFrame=cap.read()
	img = cv2.resize(videoFrame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
	h,w,c = img.shape
	if counterForFrameSize==0:
		print h," ",w
		counterForFrameSize+=1
	
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	unroll = gray.reshape(1,76800).astype(np.float32)
	cv2.imshow('frame',img)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		storing_data=False
		break

	#for event in pygame.event.get():
	#	if event.type == pygame.KEYDOWN:
	#		key_input = pygame.key.get_pressed()

	#		if(key_input[pygame.K_r]):
	ret,resp = neural.predict(unroll)
	print resp 
	prediction = resp.argmax(-1)
	print "Predicted value = " , prediction
			#elif(key_input[pygame.K_q]):
			#	storing_data=False
			#	pygame.display.quit()
			#	break
	
print "Over"
cv2.destroyAllWindows()
cap.release()

