global pi
pi = 3.14159
print('--------------------------------------------------------------------------------------------------')

print('1. Perimeter')
print('2. Circumference')
print('3. Area')
print('4. Surface Area')
print('5. Volume')
print('6. Pythagorus Theorem ')
print('7. Distance Formula')
print('8. Slope of a Line')
print('9. Midpoint Formula\n')

cal = int(input('Enter the no. ahead of the option you want to perform: '))

if cal == 1:
    print('--------------------------------------------------------------------------------')
    print('Choose the shape you want to calculate perimeter of \n1. Square\n2. Rectangle')
    op = int(input('Enter the No. ahead of the chosen option: '))
    print('--------------------------------------------------------------------------------')
    if op == 1:
        a = float(input('Enter the side of the Square: '))

        P = 4*a
        print('The Perimeter of Square is:', P)

    elif op == 2:
        l = float(input('Enter the Length of the Rectangle: '))
        b = float(input('Enter the Breadth of the Rectangle: '))

        P = 2*(l+b)
        print('The Perimeter of Rectangle is:',P)
        
    else:
        print('Selected option is Invalid!')
        print('--------------------------------------------------------------------------------')

elif cal == 2:
    print('--------------------------------------------------------------------------------')
    r = float(input('Enter the Radius of the Circle: '))

    C = 2*pi*r
    print('The Circumference of the Circle is:', C)

elif cal == 3:
    print('--------------------------------------------------------------------------------')
    print('Choose the shape you want to calculate area of \n1. Square\n2. Rectangle\n3. Triangle\n4. Trapezoid\n5. Circle')
    op = int(input('Enter the No. ahead of the chosen option: '))
    print('--------------------------------------------------------------------------------')
    if op == 1:
        a = float(input('Enter the side of the Square: '))

        A = a**2
        print('The Area of Square is:', A)

    elif op == 2:
        l = float(input('Enter the Length of the Rectangle: '))
        b = float(input('Enter the Breadth of the Rectangle: '))

        A = l*b
        print('The Area of Rectangle is:',A)

    elif op == 3:
        b = float(input('Enter the Base of the Triangle: '))
        h = float(input('Enter the Height of the Triangle: '))

        A = (b*h)/2
        print('The Area of Triangle is:',A)

    elif op == 4:
        b1 = float(input('Enter the 1st Parallel Side of the Trapezoid: '))
        b2 = float(input('Enter the 2nd Parallel Side of the Trapezoid: '))
        h =  float(input('Enter the Height of the Trapezoid: '))

        A = ((b1+b2)*h)/2
        print('The Area of Trapezoid is:',A)

    elif op == 5:
        r = float(input('Enter the Radius of the Circle: '))

        A = pi*(r**2)
        print('The Area of Circle is:',A)

    else:
        print('Selected option is Invalid!')
        print('--------------------------------------------------------------------------------')

elif cal == 4:
    print('--------------------------------------------------------------------------------')
    print('Choose the shape you want to calculate volume of \n1. Cube\n2. Cylinder\n3. Cone\n4. Sphere')
    op = int(input('Enter the No. ahead of the chosen option: '))
    print('--------------------------------------------------------------------------------')
    if op == 1:
        a = float(input('Enter the side of the Cube: '))

        S = 6*(a**2)
        print('The Surface Area of Cube is:', S)

    elif op == 2:
        r = float(input('Enter the Radius of the Cylinder: '))
        h = float(input('Enter the Height of the Cylinder: '))

        S = 2*pi*r*h
        print('The Surface Area of Cylinder is:', S)

    elif op == 3:
        r = float(input('Enter the Radius of the Cone: '))
        l = float(input('Enter the Slant Height of the Cone: '))

        S = pi*r*l
        print('The Curved Surface Area if Cone is:', S)

    elif op == 4:
        r = float(input('Enter the Radius of the Sphere: '))

        S = 4*pi*(r**2)
        print('The Surface Area of Sphere is:', S)

    else:
        print('Selected option is Invalid!')
        print('--------------------------------------------------------------------------------')

elif cal == 5:
    print('--------------------------------------------------------------------------------')
    print('Choose the shape you want to calculate perimeter of \n1. Cylinder\n2. Cone\n3. Sphere')
    op = int(input('Enter the No. ahead of the chosen option: '))
    print('--------------------------------------------------------------------------------')
    if op == 1:
        r = float(input('Enter the Radius of the Cylinder: '))
        h = float(input('Enter the Height of the Cylinder: '))

        V = pi*h*(r**2)
        print('The Volume of Cylinder is:', V)

    elif op == 2:
        r = float(input('Enter the Radius of the Cone: '))
        h = float(input('Enter the Height of the Cone: '))

        V = (pi*h*(r**2))/3
        print('The Volume of Cone is:', V)

    elif op == 3:
        r = float(input('Enter the Radius of the Sphere: '))

        V = (4*pi*(r**3))/3
        print('The Volume of Sphere is:', V)

    else:
        print('Selected option is Invalid!')
        print('--------------------------------------------------------------------------------')
        
elif cal == 6:
    print('--------------------------------------------------------------------------------')
    print('Choose what you want to calculate \n1. Unknown Side\n2. Hypotenuse')
    op = int(input('Enter the No. ahead of the chosen option: '))
    print('--------------------------------------------------------------------------------')
    if op == 1:
        h = float(input('Enter the Hypotenuse of the Right angle triangle: '))
        s1 = float(input('Enter the Known Side of the Right angle triangle: '))

        s2 = ((h**2)-(s1**2))**0.5
        print('The Unknown Side of Right angle triangle is:', s2)
        
    elif op == 2:
        s1 = float(input('Enter the Side One of the Right angle triangle: '))
        s2 = float(input('Enter the Side Two of the Right angle triangle: '))

        h = ((s1**2)+(s2**2))**0.5
        print('The Hypotenuse of Right angle triangle is:', h)

    else:
        print('Selected option is Invalid!')
        print('--------------------------------------------------------------------------------')

elif cal == 7:
    print('--------------------------------------------------------------------------------')
    x1 = float(input('Enter the x1-coordinate of the Initial Point: '))
    y1 = float(input('Enter the y1-coordinate of the Initial Point: '))
    x2 = float(input('Enter the x2-coordinate of the Final Point: '))
    y2 = float(input('Enter the y2-coordinate of the Final Point: '))

    d = (((x2-x1)**2)+((y2-y1)**2))**0.5
    print('The Distance between Initial and Final point is:', d)

elif cal == 8:
    print('--------------------------------------------------------------------------------')
    x1 = float(input('Enter the x1-coordinate of the Initial Point: '))
    y1 = float(input('Enter the y1-coordinate of the Initial Point: '))
    x2 = float(input('Enter the x2-coordinate of the Final Point: '))
    y2 = float(input('Enter the y2-coordinate of the Final Point: '))

    m = (y2-y1)/(x2-x1)
    print('The Slope of Line is:', m)

elif cal == 9:
    print('--------------------------------------------------------------------------------')
    x1 = float(input('Enter the x1-coordinate of the 1st Point: '))
    y1 = float(input('Enter the y1-coordinate of the 1st Point: '))
    x2 = float(input('Enter the x2-coordinate of the 2nd Point: '))
    y2 = float(input('Enter the y2-coordinate of the 2nd Point: '))

    Mx = (x1+x2)/2
    My = (y1+y2)/2
    print('The Midpoint between 1st and 2nd point is:('+str(Mx)+','+str(My)+')')

else:
    print('--------------------------------------------------------------------------------')
    print('Selected option is Invalid!')
    print('--------------------------------------------------------------------------------')    

         
    
