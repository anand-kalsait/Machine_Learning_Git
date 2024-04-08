import numpy as np

a1=np.random.randint(100,size=(3,3))
print(a1)

print(type(a1))

b=[[1,2,3],[7,8,9],[0,5,8]]
b=np.matrix(b)
print(b)

print(type(b))

c=np.ravel(b)
print(c)

#indexing

#first row and first column
print(b[0,0])
print(b[1,2])

#b[2][0]=12
print(b)

for i in range(3):  #row indexing in matrix
    for j in range(3): #Columns
        if(b[i,j] > 5):
            b[i,j]=-1
print(b)
            

b = np.array([[1, 2, 3], [7, 8, 9], [0, 5, 8]])
print(b)
for i in range(3):  #row indexing in array 
    for j in range(3): #Column
        if(b[i][j] > 5):
            b[i][j]=-1
print(b)
