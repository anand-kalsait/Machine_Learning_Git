o# Write a program to find maximum between two numbers.

a = float(input('Enter the first number you want to compare: '))
b = float(input('Enter the second number you want to compare: '))

if a > b:
    print('The Maximum number between '+str(a)+' and '+str(b)+' is '+str(a))
elif a < b:
    print('The Maximum number between '+str(a)+' and '+str(b)+' is '+str(b))
else:
    print('Both the numbers are equal!')
print('--------------------------------------------------------------------------\n')

# Write a program to find maximum between three numbers.

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

# Write a program to check whether a number is negative, positive or zero.

d = float(input('Enter the number you want to check: '))

if d < 0:
    print('The given number is a Negative Number.')
elif d > 0:
    print('The given number is a Positive Number.')
else:
    print('The given number is Zero.')
print('--------------------------------------------------------------------------\n')

# Write a program to check whether a number is divisible by 5 and 11 or not.

d = float(input('Enter the number you want to check: '))

if d%5 == 0 and d%11 == 0:
    print('The given number is divisible by 5 as well as 11.')
elif d%5 == 0 and d%11 != 0:
    print('The given number is divisible by 5 but not by 11.')
elif d%5 != 0 and d%11 == 0:
    print('The given number is divisible by 11 but not by 5.')
else:
    print('The given number is divisible by neither 5 nor 11.')

# Write a program to check whether a number is even or odd.

d = float(input('Enter the number you want to check: '))

if d%2 == 0:
    print('The given number is Even.')
elif d%2 == 1:
    print('The given number is Odd.')
else:
    print("The given number is neither Even nor Odd as it's not a Whole number.")
print('--------------------------------------------------------------------------\n')

# Write a program to input any alphabet and check whether it is vowel or consonant.

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

# Write a program to input angles of a triangle and check whether triangle is valid or not.

i = float(input('Enter the 1st angle of the Triangle: '))
j = float(input('Enter the 2nd angle of the Triangle: '))
k = float(input('Enter the 3rd angle of the Triangle: '))

if i+j+k == 180:
    print('The triangle is vaild.')
else:
    print('The triangle is not valid.')
print('--------------------------------------------------------------------------\n')

# Write a program to input all sides of a triangle and check whether triangle is valid or not.

i = float(input('Enter the 1st side of the Triangle: '))
j = float(input('Enter the 2nd side of the Triangle: '))
k = float(input('Enter the 3rd side of the Triangle: '))

if i+j > k and j+k > i and k+i >j:
    print('The given side can make a triangle, thus the traingle is valid.')
else:
    print('The given side cannot make a triangle, thus the traingle is not valid.')
print('--------------------------------------------------------------------------\n')

# Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.
# Calculate percentage and grade.

phy = float(input('Enter the marke in Physics out of 100: '))
chem = float(input('Enter the marke in Chemistry out of 100: '))
bio = float(input('Enter the marke in Biology out of 100: '))
math = float(input('Enter the marke in Mathematics out of 100: '))
comp =float(input('Enter the marke in Computer out of 100: '))

percent = ((phy+chem+bio+math+comp)/500)*100

if percent < 40:
    print('The Percentage is '+str(percent)+' with a Grade F')

elif percent >= 40 and percent <60:
    print('The Percentage is '+str(percent)+' with a Grade E')
elif percent >= 60 and percent <70:
    print('The Percentage is '+str(percent)+' with a Grade D')
elif percent >= 70 and percent <80:
    print('The Percentage is '+str(percent)+' with a Grade C')
elif percent >= 80 and percent <90:
    print('The Percentage is '+str(percent)+' with a Grade B')
elif percent >= 90:
    print('The Percentage is '+str(percent)+' with a Grade A')
print('--------------------------------------------------------------------------\n')

# Write a program to input electricity unit charges
# Calculate total electricity bill according to the given condition:

uc = float(input('Enter the Units shown on the Electricity Meter: '))
bill = 0

if uc > 50: # for units till 50
    rc = uc - 50
    bill = 50 *0.50
    if rc > 100: # for units till 150
        rc = rc - 100
        bill = bill + (100*0.75)
        if rc > 100: # for units till 250
            rc = rc - 100
            bill = bill + (100*1.20)
            if rc > 0: #for units above 250
                bill = bill + (rc*1.50)
        else: # for units below 250
            bill = bill + (rc*1.20)
    else: # for units below 150
        bill = bill + (rc*0.75)
else: # for units below 50
    bill = uc*0.5

total = bill + (bill*(20/100))

print('The total electricity bill is '+str(total)+' Rupees.')
print('--------------------------------------------------------------------------\n')



