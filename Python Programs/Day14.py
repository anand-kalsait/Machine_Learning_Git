import numpy as np
import cv2

I = cv2.imread('A1.png')
##print(I)
##cv2.imshow('input_img', I)

print(np.shape(I))
I1 = I[:,:,0]
print(np.shape(I1))

## Resizing the Image
A = cv2.resize(I,(100,100),3)
cv2.imshow('Resized_img', A)
print(np.shape(A))

## Filtering the image with blur
B = cv2.medianBlur(I, 11)
cv2.imshow('Blured_img',B)

## Cropping the image
C = I[52:150,50:150,:]
cv2.imshow('Cropped_img', C)
