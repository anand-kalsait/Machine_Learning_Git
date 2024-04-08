import numpy as np
import pandas as pd
import cv2
import statistics as st
import scipy.stats as sp

photos = {'battery':945, 'biological':985,
          'brown-glass':607, 'cardboard':891,
          'clothes':5325, 'green-glass':629,
          'metal':769, 'paper':1050,
          'plastic':865, 'shoes':1977,
          'trash':697, 'white-glass':775}

keys = list(photos.keys())
values = list(photos.values())
from sklearn import preprocessing 
LE = preprocessing.LabelEncoder()
key = LE.fit_transform(keys)
print(key,np.shape(key))

for i in range(len(keys)):
    for j in range(values[i]):
        fn = keys[i]+str(int(j+1))+'.jpg'
     

count = 0
print(count)
print()
for i in range(10):
    count += 1
    print(count)
