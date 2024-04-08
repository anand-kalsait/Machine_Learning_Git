import numpy as np
import pandas as pd

df = pd.read_csv('city_day.csv')
##df = df.replace(np.nan,0)
##print(df)
##df.info()

df.drop(['AQI_Bucket','City','Date'],axis = 1,inplace = True) # dropping column by labels
##df.drop(df.index[312:544],inplace = True) #dropping rows by index
##df.drop(df.index[674:1028],inplace = True)
df = df.dropna()
##df = df.reset_index(drop=True) # To reset the indices
##df['Date'] = pd.to_datetime(df['Date'], format = '%Y-%m-%d')
##df['Month'] = df['Date'].dt.month
##df.drop('Date',axis = 1,inplace =True)
##col = df.pop('Month')
##df.insert(0, col.name, col)

##df['Time'] = pd.to_datetime(df['Time'], format = '%H.%M.%S')
##df['Hour'] = df['Time'].dt.hour
##df.drop('Time',axis = 1,inplace =True)
##col = df.pop('Hour')
##df.insert(1, col.name, col)
df.info()
df = np.matrix(df)
##print(df)
##print(np.shape(df))

y = df[:,12]
y = np.ravel(y)
X1 = df[:,0:12]
X = np.asarray(X1)

##### LR

from sklearn import linear_model
mdl1 = linear_model.LinearRegression()
mdl1.fit(X,y)

print('\nThe LR Score:',mdl1.score(X,y)*100,'%')

##### Naive Bayes

from sklearn.naive_bayes import GaussianNB
mdl2 = GaussianNB()
mdl2.fit(X,y)

print('\nThe Naive Bayes Score:',mdl2.score(X,y)*100,'%')

##### Decision Tree

from sklearn import tree
mdl3 = tree.DecisionTreeClassifier()
mdl3.fit(X,y)
print('\nThe Decision Tree Score:',mdl3.score(X,y)*100,'%')

##### SVM

from sklearn.svm import SVC
mdl4 = SVC()
mdl4.fit(X,y)
print('\nThe SVM Score:',mdl4.score(X,y)*100,'%')

##### MLP
from sklearn.neural_network import MLPClassifier
mdl5 = MLPClassifier()
mdl5.fit(X,y)
print('\nThe MLP Score:',mdl5.score(X,y)*100,'%')

inp = [71.13,191.27,19.23,40.37,59.6,56.56,1.03,4.28,11.79,2.37,6.8,24.64]
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

print('\n')
print(res1)
if(res1 > 0 and res1 <= 50):
    print('Good Air Quality\n')
elif(res1 >50 and res1 <= 100):
    print('Satisfactory Air Quality\n')
elif(res1 >100 and res1 <= 200):
    print('Moderate Air Quality\n')
elif(res1 >200 and res1 <= 300):
    print('Poor Air Quality\n')
elif(res1 >300 and res1 <= 400):
    print('Very Poor Air Quality\n')
elif(res1 >400 and res1 <= 500):
    print('Severe Air Quality\n')

print(res2)
if(res2 > 0 and res2 <= 50):
    print('Good Air Quality\n')
elif(res2 >50 and res2 <= 100):
    print('Satisfactory Air Quality\n')
elif(res2 >100 and res2 <= 200):
    print('Moderate Air Quality\n')
elif(res2 >200 and res2 <= 300):
    print('Poor Air Quality\n')
elif(res2 >300 and res2 <= 400):
    print('Very Poor Air Quality\n')
elif(res2 >400 and res2 <= 500):
    print('Severe Air Quality\n')

print(res3)
if(res3 > 0 and res3 <= 50):
    print('Good Air Quality\n')
elif(res3 >50 and res3 <= 100):
    print('Satisfactory Air Quality\n')
elif(res3 >100 and res3 <= 200):
    print('Moderate Air Quality\n')
elif(res3 >200 and res3 <= 300):
    print('Poor Air Quality\n')
elif(res3 >300 and res3 <= 400):
    print('Very Poor Air Quality\n')
elif(res3 >400 and res3 <= 500):
    print('Severe Air Quality\n')

print(res4)
if(res4 > 0 and res4 <= 50):
    print('Good Air Quality\n')
elif(res4 >50 and res4 <= 100):
    print('Satisfactory Air Quality\n')
elif(res4 >100 and res4 <= 200):
    print('Moderate Air Quality\n')
elif(res4 >200 and res4 <= 300):
    print('Poor Air Quality\n')
elif(res4 >300 and res4 <= 400):
    print('Very Poor Air Quality\n')
elif(res4 >400 and res4 <= 500):
    print('Severe Air Quality\n')

print(res5)
if(res5 > 0 and res5 <= 50):
    print('Good Air Quality\n')
elif(res5 >50 and res5 <= 100):
    print('Satisfactory Air Quality\n')
elif(res5 >100 and res5 <= 200):
    print('Moderate Air Quality\n')
elif(res5 >200 and res5 <= 300):
    print('Poor Air Quality\n')
elif(res5 >300 and res5 <= 400):
    print('Very Poor Air Quality\n')
elif(res5 >400 and res5 <= 500):
    print('Severe Air Quality\n')

