import numpy as np
import pandas as pd

df = pd.read_csv('heart.csv')
df.info()
df = np.matrix(df)
##print(df)
##print(np.shape(df))

y = df[:,13]
y = np.ravel(y)
##print(np.shape(y))

y1 = np.zeros(1025)
for i in range(1025):
    y1[i] = y[i]

y = y1
##print(y)

X1 = df[:,0:13]
X = np.asarray(X1)
##print(X[0,:])
'''
for i in range(1025):
    for j in range(13):
        if(X[i,j] == '?'):
            X[i,j] = -1
        X[i,j]=float(X[i,j])
##print(df)
'''
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


inp = [56,1,1,120,236,0,1,178,0,0.8,2,0,2]
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

res3 = mdl3.predict(inp)
res3 = np.abs(res3) 
res3 = np.round(res3)
res3 = int(res3)

res4 = mdl4.predict(inp)
res4 = np.abs(res4) 
res4 = np.round(res4)
res4 = int(res4)

res5 = mdl5.predict(inp)
res5 = np.abs(res5) 
res5 = np.round(res5)
res5 = int(res5)

if(res1 == 0):
    print('Heart Disease NOT Detected\n')
elif(res1 == 1):
    print('Heart Disease Detected\n')


if(res2 == 0):
    print('Heart Disease NOT Detected\n')
elif(res2 == 1):
    print('Heart Disease Detected\n')

/    
if(res3 == 0):
    print('Heart Disease NOT Detected\n')
elif(res3 == 1):
    print('Heart Disease Detected\n')

if(res4 == 0):
    print('Heart Disease NOT Detected\n')
elif(res4 == 1):
    print('Heart Disease Detected\n')

if(res5 == 0):
    print('Heart Disease NOT Detected\n')
elif(res5 == 1):
    print('Heart Disease Detected\n')

