import numpy as np
import pandas as pd
import cv2
import statistics as st
import scipy.stats as sp

import warnings
warnings.filterwarnings("ignore")

count = 0
df = np.zeros((360,65))
##print(df)

for i in range(9):
    for j in range(40):
        fn = str(i+1)+' ('+str(j+1)+').jpg'
##        print(fn)
    
        yolo = cv2.imread(fn)
        A = cv2.resize(yolo,(64,64),3)
    ##    cv2.imshow('resized_img',A)

        b = cv2.cvtColor(A,cv2.COLOR_BGR2GRAY)
    ##    cv2.imshow('greyed_img',b)
        from sklearn.decomposition import PCA
        pca = PCA(n_components = 64)
        pca.fit(b)
        f = pca.singular_values_
##        b = np.ravel(b)
##        
##        f1 = np.mean(b)
##        f2 = st.mode(b)
##        ##print(st.stdev(b))
##        ##print(st.variance(b))
##        ##print(sp.skew(sp.skew(b)))
##        f3 = sp.kurtosis(b)
##        ##f4 = sp.gstd(b)
##
##        f = [f1, f2, f3]
##
##        print(f)
        
        for j in range(64):
            df[count,j] = f[j]
        df[count,64] = i + 1
        count = count + 1
##        print(count)
       

df = np.float32(df)  
##print(df)
##DF = pd.DataFrame(df)
##DF.to_csv('fruits.csv')

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

test = cv2.imread('7 (23).jpg')
print('for test subject 04-------------------------------------')
T = cv2.resize(test,(64,64),3)
cv2.imshow('resized_img',T)

t = cv2.cvtColor(T,cv2.COLOR_BGR2GRAY)
##cv2.imshow('greyed_img',b)
    
##t = np.ravel(t)
##    
##f1 = np.mean(t)
##f2 = st.mode(t)
####print(st.stdev(t))
####print(st.variance(t))
####print(sp.skew(sp.skew(t)))
##f3 = sp.kurtosis(t)
####f4 = sp.gstd(t)
##inp = [f1, f2, f3]

from sklearn.decomposition import PCA
pcat = PCA(n_components = 64)
pcat.fit(t)
inp = pcat.singular_values_

##print(inp)
##inp = [213.4625,251,1.1755874,1.6572266]
inp = np.asarray(inp)
##print(np.shape(inp))
inp = inp.reshape(1,-1)

res1 = mdl1.predict(inp)
res1 = np.abs(res1) 
res1 = np.round(res1)
res1 = int(res1)
print(res1)

res2 = mdl2.predict(inp)
res2 = np.abs(res2) 
res2 = np.round(res2)
res2 = int(res2)
print(res2)

res3 = mdl3.predict(inp)
res3 = np.abs(res3) 
res3 = np.round(res3)
res3 = int(res3)
print(res3)

res4 = mdl4.predict(inp)
res4 = np.abs(res4) 
res4 = np.round(res4)
res4 = int(res4)
print(res4)

res5 = mdl5.predict(inp)
res5 = np.abs(res5) 
res5 = np.round(res5)
res5 = int(res5)
print(res5)

'''
if(res1 == 0):
    print('Mango\n')
elif(res1 == 1):
    print('Pineapple\n')

if(res2 == 0):
    print('Mango\n')
elif(res2 == 1):
    print('Pineapple\n')

if(res3 == 0):
    print('Mango\n')
elif(res3 == 1):
    print('Pineapple\n')

if(res4 == 0):
    print('Mango\n')
elif(res4 == 1):
    print('Pineapple\n')

if(res5 == 0):
    print('Mango\n')
elif(res5 == 1):
    print('Pineapple\n')
'''
