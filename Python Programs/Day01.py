a = 100

#Scalar Operation

print(a+20)
print(5*12)

#Create Variable

a = 5
b = 10.5
c = '12'
d = 'rahul'

print(a+b,'\n')


#Data Type Conversion

a1 = float(a)
b1 = int(b)
c1 = int(c)
d1 = str(a)

print(a1,b1,c1,d1)

print(type(a1), type(b1), type(c1), type(d1))

print(a+int(c))
print(c+d)

#Input from User
'''
a = float(input('Enter value of a: '))
b = float(input('Enter value of b: '))
c = a+b
print(c)
'''

I = float(input('Enter value of Current: '))
R = float(input('Enter value of Resistance: '))
V = I*R
print('Voltage is = ',V)
