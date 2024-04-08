import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')
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
from sklearn import preprocessing
LE = preprocessing.LabelEncoder()
y = LE.fit_transform(y1)

##for i in range(13611):
##    if(y[i]=='SEKER'):
##        y[i] = 0    
##    elif(y[i]=='BARBUNYA'):
##        y[i] = 1
##    elif(y[i]=='BOMBAY'):
##        y[i] = 2
##    elif(y[i]=='CALI'):
##        y[i] = 3
##    elif(y[i]=='HOROZ'):
##        y[i] = 4
##    elif(y[i]=='SIRA'):
##        y[i] = 5
##    elif(y[i]=='DERMASON'):
##        y[i] = 6
##print(y)

##### Step 05: Training the model   # Linear Regression
from sklearn import tree
mdl1 = tree.DecisionTreeClassifier()
##mdl = linear_model.LinearRegression()
mdl1.fit(X,y)
print(mdl1.score(X,y)*100,'%')

##### Bonus Step: Visualiazation

##### Step 06: Testing
inp = [208502,1770.466,674.4861852,401.0171551,1.681938482,0.804057113,212629,515.2407122,0.679936996,0.980590606,0.835881873,0.763901061,0.003234915,0.000679502,0.58354483,0.981486506]
inp = np.asarray(inp)
inp = inp.reshape(1, -1)
res1 = mdl1.predict(inp)
res1 = np.abs(res1) #to make the value +ve
res1 = np.round(res1)
res1 = int(res1)
print(res1)

result = LE.inverse_transform([res1])
print(result)

##if(res1==0):
##    print('SEKER')    
##elif(res1==1):
##    print('BARBUNYA') 
##elif(res1==2):
##    print('BOMBAY') 
##elif(res1==3):
##    print('CALI') 
##elif(res1==4):
##    print('HOROZ') 
##elif(res1==5):
##    print('SIRA') 
##elif(res1==6):
##    print('DERMASON') 

