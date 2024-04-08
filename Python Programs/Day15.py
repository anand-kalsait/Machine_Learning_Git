import numpy as np
import cv2
 
yolo = cv2.imread('cricket.jpg')
A = cv2.resize(yolo,(50,50),3)
cv2.imshow('resized_img',A)

b = cv2.cvtColor(A,cv2.COLOR_BGR2GRAY)

cv2.imshow('greyed_img',b)
print(np.shape(b))

f1 = np.mean(b)
print(f1)
b = np.ravel(b)
import statistics as st
f2 = st.mode(b)
##print(st.stdev(b))
##print(st.variance(b))


import scipy.stats as sp
##print(sp.skew(sp.skew(b)))
f3 = sp.kurtosis(b)
f4 = sp.gstd(b)

f = [f1, f2, f3, f4]
print(f)
