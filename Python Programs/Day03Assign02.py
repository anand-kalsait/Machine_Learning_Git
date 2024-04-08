# Take character from user and check weaather it is a vowel or consonant.

c = input('Enter any alphabet you want to check: ')

try:
    d = float(c)
    print('The given input is a Number not an Alphabet.')
except ValueError:
    if c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
        print(c+' is a Vowel.')
    else:
        print(c+' is a Consonant.')   
print('--------------------------------------------------------------------------\n')

# Find largest number from 350, 250 and 300.

x = float(input('Enter the first number you want to compare: '))
y = float(input('Enter the second number you want to compare: '))
z = float(input('Enter the third number you want to compare: '))

if x > y and x > z:
    print('The Maximum number between '+str(x)+' , '+str(y)+' and '+str(z)+' is '+str(x))
elif y > x and y > z:
    print('The Maximum number between '+str(x)+' , '+str(y)+' and '+str(z)+' is '+str(y))
elif z > x and z > y:
    print('The Maximum number between '+str(x)+' , '+str(y)+' and '+str(z)+' is '+str(z))
else:
    print('All the given numbers are equal!')
print('--------------------------------------------------------------------------\n')

# Writte a code that will take input x from user and check for both conditions
# x must be less than 20 and larger than 4 
# x must be even number

a = float(input('Enter the number you want to check: '))

if a > 4 and a < 20:
    if a%2 == 0:
        print('The number '+str(a)+' meets all the conditions ie. 4 < x < 20, x is even.')
    else:
        print('The number '+str(a)+' meets one of the conditions ie. 4 < x < 20, x is odd.')
else:
    print('The number does not meet the 1st condition ie. 4 < x < 20.')
print('--------------------------------------------------------------------------\n')        

# Check weather input is divisible by 2, 3, 5.

a = float(input('Enter the number you want to check: '))

if a%2 == 0:
    print('The number is divisible by 2.')
elif a%3 == 0:
    print('The number is divisible by 3.')
elif a%5 == 0:
    print('The number is divisible by 5.')
else:
    print('The number is not divisible by 2, 3 or 5.')
print('--------------------------------------------------------------------------\n')

# Take a person's weight as input from user
# If it is larger than 80, then for each kg he have to pay 3 Rs fine. calculate total fine.

weight = float(input('Enter the weight: '))

if weight > 80:
    print('The total fine is:', weight*3, 'rupees.')
else:
    print('Good Work! You are under 80 KG weight.')
print('--------------------------------------------------------------------------\n')

# Write a code taht will take temperature as input from user and reccomend user kind of clothes to wear

temp = float(input('Enter the Environment Temperature: '))

if temp < -10:
    print('The temperature is below -10* Celcius. Exercise caution or you will freeze to death.')
elif temp > -10 and temp < 10:
    print('The temperature is very cold, wear very warm clothes.')
elif temp > 10 and temp < 20:
    print('The temperature is cold, wear warm clothes.')
elif temp > 20 and temp < 35:
    print('The temperature is normal, wear normal clothes.')
elif temp > 35 and temp < 45:
    print('The temperature is high, wear thin but full clothes.')
elif temp > 45:
    print('It is scorching hot out there. Exercise caution or you will get a heat stroke.')
print('--------------------------------------------------------------------------\n')

