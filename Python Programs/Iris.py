import pandas as pd
import numpy as np

### Step 01: Read file
df1 = pd.read_csv('Iris.csv')

### Step 02: Convert to matrix
df = np.matrix(df1)

### Step 03: Seperate X and Y
X = df[:,1:5]
X = np.asarray(X)
##print(X)
#print(np.shape(X))
y1 = df[:,5]
y1 = np.ravel(y1)
##print(y1)

from sklearn import preprocessing ##data encoder for the str or obj values to suitable values
LE = preprocessing.LabelEncoder()
y = LE.fit_transform(y1)
##print(y)

from sklearn.model_selection import train_test_split ## to make train and test data using sklearn.model
X1,X2,Y1,Y2 = train_test_split(X,y,test_size = 0.3 ,random_state = 1)
##30% data will be used to train and 1 random state will be used to test
##print(np.mean(X1))
##print(np.mean(Y1))
##print(np.mean(X2))
##print(np.mean(Y2))
##
##print(np.shape(X1))
##print(np.shape(Y1))
##print(np.shape(X2))
##print(np.shape(Y2))

### Step 05: Training the model

#####Linear Regression Classifier
from sklearn import linear_model
mdl1 = linear_model.LinearRegression()
mdl1.fit(X1,Y1)
print(mdl1.score(X1,Y1)*100,'%')
      
#####Naive Bayes GaussianNG Classifier
from sklearn.naive_bayes import GaussianNB
mdl2 = GaussianNB()
mdl2.fit(X1,Y1)
print(mdl2.score(X1,Y1)*100,'%')
      
#####Decision tree Classifier
from sklearn import tree
mdl3 = tree.DecisionTreeClassifier()
mdl3.fit(X1,Y1)
print(mdl3.score(X1,Y1)*100,'%')

res1 = mdl1.predict(X2)

for r in range(45):
    z = np.abs(res1[r]) 
    z = np.round(z)
    z = int(z)
    res1[r] = z
print(res1)

res2 = mdl2.predict(X2)
print(res2)

res3 = mdl3.predict(X2)
print(res3)
print(res2 == res3)
print('\nThis is Liner Regression Predictions')
for i in range(45):
    res = np.abs(res1[i]) #to make the value +ve
    res = np.round(res)
    res = int(res)
    class1 = LE.inverse_transform([res])
    ##data decoder from result to original obj or str data for desired results
    print(class1)

print('\nThis is Naive Bayes GaussianNG Classifier Predictions')

for i in range(45):
    class1 = LE.inverse_transform([res2[i]])
    ##data decoder from result to original obj or str data for desired results
    print(class1)

print('\nThis is Decision tree Classifier Predictions')
for i in range(45):
    class1 = LE.inverse_transform([res3[i]])
    ##data decoder from result to original obj or str data for desired results
    print(class1)                       

from sklearn import metrics
print(metrics.classification_report(Y2,res1))
print(metrics.classification_report(Y2,res2))
print(metrics.classification_report(Y2,res3))






