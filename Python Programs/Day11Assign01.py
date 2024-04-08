import numpy as np
import pandas as pd

df = pd.read_csv('lung-cancer.data')
df.info()
df = np.matrix(df)
##print(df)
##print(np.shape(df))

y = df[:,0]
y = np.ravel(y)
print(np.shape(y))
y1 = np.zeros(31)
for i in range(31):
    y1[i] = y[i]

y = y1
##print(y)

X1 = df[:,1:57]
X = np.asarray(X1)
##print(X[0,:])

for i in range(31):
    for j in range(56):
        if(X[i,j] == '?'):
            X[i,j] = -1
        X[i,j]=float(X[i,j])
##print(df)
            
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

inp = [0,3,2,2,0,2,2,2,1,1,2,0,2,2,2,1,2,3,2,2,2,2,1,0,2,2,2,2,2,2,1,1,0,2,1,1,3,1,3,0,3,2,3,2,2,2,2,2,2,3,1,2,2,2,2,2]
inp = np.asarray(inp)
##print(np.shape(inp))
inp = inp.reshape(1,-1)

res1 = mdl1.predict(inp)
res1 = np.abs(res1) 
res1 = np.round(res1)
res1 = int(res1)

res2 = mdl2.predict(inp)
res2 = np.abs(res2) 
res2 = np.round(res2)
res2 = int(res2)

res3 = mdl1.predict(inp)
res3 = np.abs(res3) 
res3 = np.round(res3)
res3 = int(res3)

if(res1 == 1):
    print('The Cancer is 1st Stage')
elif(res1 == 2):
    print('The Cancer is 2nd Stage')
elif(res1 == 3):
    print('The Cancer is 3rd Stage')

if(res2 == 1):
    print('The Cancer is 1st Stage')
elif(res2 == 2):
    print('The Cancer is 2nd Stage')
elif(res2 == 3):
    print('The Cancer is 3rd Stage')

if(res3 == 1):
    print('The Cancer is 1st Stage')
elif(res3 == 2):
    print('The Cancer is 2nd Stage')
elif(res3 == 3):
    print('The Cancer is 3rd Stage')

