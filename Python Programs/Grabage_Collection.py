import numpy as np
import pandas as pd
import cv2
import statistics as st
import scipy.stats as sp

import warnings
warnings.filterwarnings("ignore")

photos = {'battery':945, 'biological':985,
          'brown-glass':607, 'cardboard':891,
          'clothes':5325, 'green-glass':629,
          'metal':769, 'paper':1050,
          'plastic':865, 'shoes':1977,
          'trash':697, 'white-glass':775}
keys = list(photos.keys())
values = list(photos.values())
count = 0


from sklearn import preprocessing 
LE = preprocessing.LabelEncoder()
key = LE.fit_transform(keys)
##print(key,np.shape(key))

df = np.zeros((15515,65))
##print(np.shape(df))

for i in range(len(keys)):
    for j in range(values[i]):
        fn = keys[i]+str(int(j+1))+'.jpg'
##    print(fn,df[i,0])
        yolo = cv2.imread(fn)
##    cv2.imshow('resized_img',yolo)
        A = cv2.resize(yolo,(64,64),3)

        b = cv2.cvtColor(A,cv2.COLOR_BGR2GRAY)
##    cv2.imshow('greyed_img',b)
        from sklearn.decomposition import PCA
        pca = PCA(n_components = 64)
        pca.fit(b)
        f = pca.singular_values_
        for k in range(64):
            df[count,k] = f[k]
        df[count,64] = key[i]  
        count += 1


df = np.float32(df)  
##print(df)
DF = pd.DataFrame(df)
##DF.to_csv('Garbage_Collection.csv')

X = df[:,0:64]
##print(X)

y = df[:,64]
##print(y)

##### LR

from sklearn import linear_model
mdl1 = linear_model.LinearRegression()
mdl1.fit(X,y)

print('The Score:',mdl1.score(X,y)*100,'%')

##### Naive Bayes

from sklearn.naive_bayes import GaussianNB
mdl2 = GaussianNB()
mdl2.fit(X,y)

print('The Score:',mdl2.score(X,y)*100,'%')

##### Decision Tree

from sklearn import tree
mdl3 = tree.DecisionTreeClassifier()
mdl3.fit(X,y)
print('The Score:',mdl3.score(X,y)*100,'%')

##### SVM

from sklearn.svm import SVC
mdl4 = SVC()
mdl4.fit(X,y)
print('The Score:',mdl4.score(X,y)*100,'%')

##### MLP
from sklearn.neural_network import MLPClassifier
mdl5 = MLPClassifier()
mdl5.fit(X,y)
print('The Score:',mdl5.score(X,y)*100,'%')

#####TESTING

test = cv2.imread('biological463.jpg')
print('-------------------------------------')
T = cv2.resize(test,(64,64),3)
cv2.imshow('resized_img',T)

t = cv2.cvtColor(T,cv2.COLOR_BGR2GRAY)
##cv2.imshow('greyed_img',b)

from sklearn.decomposition import PCA
pcat = PCA(n_components = 64)
pcat.fit(t)
inp = pcat.singular_values_

##print(inp)
inp = np.asarray(inp)
##print(np.shape(inp))
inp = inp.reshape(1,-1)

res1 = mdl1.predict(inp)
res1 = np.abs(res1) 
res1 = np.round(res1)
res1 = int(res1)
class1 = LE.inverse_transform([res1])
##print(res1)
print(class1)

res2 = mdl2.predict(inp)
res2 = np.abs(res2) 
res2 = np.round(res2)
res2 = int(res2)
class1 = LE.inverse_transform([res2])
##print(res2)
print(class1)

res3 = mdl3.predict(inp)
res3 = np.abs(res3) 
res3 = np.round(res3)
res3 = int(res3)
class1 = LE.inverse_transform([res3])
##print(res3)
print(class1)

res4 = mdl4.predict(inp)
res4 = np.abs(res4) 
res4 = np.round(res4)
res4 = int(res4)
class1 = LE.inverse_transform([res4])
##print(res4)
print(class1)

res5 = mdl5.predict(inp)
res5 = np.abs(res5) 
res5 = np.round(res5)
res5 = int(res5)
class1 = LE.inverse_transform([res5])
##print(res5)
print(class1)

