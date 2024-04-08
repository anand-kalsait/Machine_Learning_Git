import numpy as np
import cv2
 
yolo = cv2.imread('cricket.jpg')
golo = cv2.imread('cricket.jpg')
cv2.imshow('original_img',yolo)
##print(np.shape(yolo))

##A = cv2.resize(yolo,(1280,720),3)
##cv2.imshow('resized_img',A)
##print(A,np.ravel(A))

C1 = yolo[0:120,20:140,:]
##cv2.imshow('cropped01_img', C1)

C2 = yolo[10:130,310:430,:]
##cv2.imshow('cropped02_img', C2)
                      
C3 = yolo[0:120,600:720,:]
##cv2.imshow('cropped03_img', C3)


golo[0:120,30:150,:] = C3
golo[10:130,300:420,:] = C1
golo[0:120,600:720,:] = C2

cv2.imshow('altered_img',golo)
