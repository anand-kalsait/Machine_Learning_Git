import numpy as np
import pandas as pd
import cv2
import statistics as st
import scipy.stats as sp

import warnings
warnings.filterwarnings("ignore")

df1 = pd.read_csv('train.csv')
df1 = np.matrix(df1)

y1 = df1[:,1]
y1 = np.ravel(y1)
from sklearn import preprocessing 
LE = preprocessing.LabelEncoder()
y = LE.fit_transform(y1)
##print(y,np.shape(y))

df = np.zeros((990,66))
print(np.shape(df))

for i in range(990):
    df[i,0] = df1[i,0]
    df[i,65] = y[i]
    fn = str(int(df[i,0]))+'.jpg'
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
        
    for j in range(64):
        df[i,j+1] = f[j]


##df = np.float32(df)  
##print(df)
##DF = pd.DataFrame(df)
##DF.to_csv('leaf.csv')

X = df[:,1:65]
##print(X)

y = df[:,65]
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

test = cv2.imread('463.jpg')
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
