import pandas as pd
import numpy as np

df = pd.read_csv('Iris.csv')
#print(df, type(df))

df = np.matrix(df)
print(type(df))

print(np.shape(df))
k1 = np.zeros(150) #list of zeroes
k2 = np.zeros((150,6)) #matrix of zeroes 150x6
print(k1)
print(k2)

k3 = np.ones(150)
print(k3)

# Indexing

x1 = df[:,1]
print(np.shape(x1),'lol')
x1 = np.ravel(x1) #to convert martix in a list or array of 1D
print(x1)
print(np.shape(x1)) #prints the shape of given martix

print(df.head()) #prints first 5 rows of matrix or dataframe
print(df.tail()) #prints last 5 rows of matrix or dataframe
print(df.to_string()) #Converts all the data in df and prints it as string
