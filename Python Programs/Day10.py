import pandas as pd
import numpy as np

### Step 01: Read file
df1 = pd.read_csv('Iris.csv')

### Step 02: Convert to matrix
df = np.matrix(df1)

### Step 03: Seperate X and Y
X = df[:,1:5]
X = np.asarray(X)
print(X)
#print(np.shape(X))
y = df[:,5]
y = np.ravel(y)
print(y)
#print(np.shape(y))

### Step 04: Convert strings/characters to numbers
y1 = np.zeros(150) # for label conversion for gaussian and tree classifier
for i in range(150):
    if(y[i]=='Iris-setosa'):
        y1[i] = 0    
    elif(y[i]=='Iris-versicolor'):
        y1[i] = 1
    elif(y[i]=='Iris-virginica'):
        y1[i] = 2

print(y1)

### Step 05: Training the model

#####Linear Regression Classifier
#from sklearn import linear_model
#mdl = linear_model.LinearRegression()

#####Naive Bayes GaussianNG Classifier
##from sklearn.naive_bayes import GaussianNB
##mdl = GaussianNB()

#####Decision tree Classifier
from sklearn import tree
mdl = tree.DecisionTreeClassifier()
mdl.fit(X,y1)
print(mdl.score(X,y1)*100,'%')

# Bonus Step: Visualiazation
# HW : s1, s2 ,p1 and p2 plot in graph with diff color
s1 = df[:,1]
s2 = df[:,2]
p1 = df[:,3]
p2 = df[:,4]

import matplotlib.pyplot as plt

plt.xlabel('Types')
plt.ylabel('Measurment')
plt.title('Iris Attributes')

plt.plot(s1, marker='s', color='red', linestyle=':',label='Sepal Lenght') 
plt.plot(s2, marker='s', color='blue', linestyle=':',label='Sepal Width') 
plt.plot(p1, marker='o', color='green', linestyle='--',label='Petal Lenght') 
plt.plot(p2, marker='o', color='violet', linestyle='--',label='Petal Width')
plt.legend(loc = 'upper right')
plt.show()

### Step 06: Testing
inp = [4.9,3.5 ,1.4 ,0.2]
inp = np.asarray(inp)
inp = inp.reshape(1, -1)
res1 = mdl.predict(inp)
res1 = np.abs(res1) #to make the value +ve
res1 = np.round(res1)
res1 = int(res1)
if(res1 == 0):
    print('Iris-setosa')
elif(res1 == 1):
    print('Iris-versicolor')
elif(res1 == 2):
    print('Iris-virginica')
