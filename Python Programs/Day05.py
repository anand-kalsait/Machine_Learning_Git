#for installing libraries -> py -m pip install library-name

import numpy as np 

a = [22,3,4,5,36,7,78,9,10]
x = [10,20,30,40,50,60,70,80,90]
c = [44,57,89]
d = ['alex', 'rahul', 'sachin']
a1 = np.array(a)
print(type(a1))

import matplotlib.pyplot as plt

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample Plot')

plt.plot(d, c, marker='s', color='orange', linestyle='dashed') #line graph
plt.show()

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample Plot')

plt.bar(d, c) #bar graph
plt.show()

plt.title('Sample Plot')

plt.pie(c, labels=d) #pie chart
plt.show()

from numpy import random

x = random.rand() #generating random number between 0-1
print(x)

y = random.rand(3,5) #grenerating matrix of 3x5 between 0-1
print(y, type(y))

z = np.matrix(y)
print(z, type(z))


a = random.randint(100,size=(3,5)) #integer matrix of array type with integer upto 100
print(a, type(a))

b =random.randint(0,10,20) #generating list of 20 numbers from 0-10 
print(b, type(b))

