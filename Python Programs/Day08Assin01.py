import pandas as pd
import numpy as np

# TASK 01
df1 = pd.read_csv('Iris.csv')
df1 = np.matrix(df1)

s1 = df1[:,1]
s1 = np.ravel(s1)
print('The extracted SepalLenght from Iris.csv are as follows\n',s1)

s2 = df1[:,2]
s2 = np.ravel(s2)
print('\nThe extracted SepalWidth from Iris.csv are as follows\n',s2)

p1 = df1[:,3]
p1 = np.ravel(p1)
print('\nThe extracted PetalLenght from Iris.csv are as follows\n',p1)

p2 = df1[:,4]
p2 = np.ravel(p2)
print('\nThe extracted PetalWidth from Iris.csv are as follows\n',p2)

# TASK 02
df2 = pd.read_csv('Iris.csv')
df2 = np.matrix(df2)

for i in range(150):
    if(df2[i,5]=='Iris-setosa'):
        df2[i,5] = 0    
    elif(df2[i,5]=='Iris-versicolor'):
        df2[i,5] = 1
    elif(df2[i,5]=='Iris-virginica'):
        df2[i,5] = 2
print('\n')
print('Changing Iris-setosa to 0.')
print('Changing Iris-versicolor to 1.')       
print('Changing Iris-virginica to 2.')
print(df2)
