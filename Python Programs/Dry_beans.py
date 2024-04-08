import pandas as pd
import numpy as np

##### Step 01: Read file
df1 = pd.read_csv('Dry_Bean_Dataset.csv')

##### Step 02: Convert to matrix
df = np.matrix(df1)

##### Step 03: Seperate X and Y
X = df[:,0:16]
X = np.asarray(X)
#print(X)
#print(np.shape(X))

y1 = df[:,16]
y1 = np.ravel(y1)
#print(y)
#print(np.shape(y))

##### Step 04: Convert strings/characters to numbers
from sklearn import preprocessing ##data encoder for the str or obj values to suitable values
LE = preprocessing.LabelEncoder()
y = LE.fit_transform(y1)
print(np.unique(y))

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
##### Step 05: Training the model

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

##### Step 06: Testing
res1 = mdl1.predict(X2)

for r in range(4084):
    z = np.abs(res1[r]) 
    z = np.round(z)
    z = int(z)
    res1[r] = z
print(res1)

res2 = mdl2.predict(X2)
print(res2)

res3 = mdl3.predict(X2)
print(res3)

from sklearn import metrics

print(metrics.classification_report(Y2,res1))
print(metrics.classification_report(Y2,res2))
print(metrics.classification_report(Y2,res3))
