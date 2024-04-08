import numpy as np
from numpy import random as rd

# Convert even no in 0 and odd no in 1 in a random matrix

x  = rd.randint(20,size=(4,4))
print('\n',x)
for i in range(4):
    for j in range(4):
        if(x[i,j]%2 == 0):
            x[i,j] = 0
        elif(x[i,j]%2 == 1):
            x[i,j] = 1
print('\n',x)

# Generate a random 10x10 matrix, seperate 10th column in a seperate variable
# Replace 0 in the 10th column

y = rd.randint(100,size=(10,10))
print('\n',y)
y1 = rd.randint(0,1,10)

for i in range(10):
    y1[i] = y[i,9]
    y[i,9] = 0

print('\n',y)
print('\n',y1)

# Random matrix with inf value and verify if there is a inf in the matrix ########
a = rd.randint(4,10)
b = rd.randint(4,10)
c = np.inf
z = rd.randint(100, size=(a,b))
z[rd.randint(5),rd.randint(5)] = np.inf
print('\n',z)


# Random matrix, find mean of the matrix and
# substract the mean from all the values in the matrix

m1 = rd.randint(4,10)
m2 = rd.randint(4,10)
mean = 0
k = rd.randint(100, size=(m1,m2))
print('\n',k)

for i in range(m1):
    for j in range(m2):
        mean = mean + k[i,j]

mean = mean/(m1*m2)
print('\nThe Mean of the martix is',mean)
for i in range(m1):
    for j in range(m2):
        k[i,j] = k[i,j] - mean
print('\n',k)
