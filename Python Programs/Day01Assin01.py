print('------------------------------------------------------------')

print('1. Voltage')
print('2. Current')
print('3. Resistance')
print('4. Conductance')
print('5. Power')
print('6. Capacitance')
print('7. Impedance')
print('8. Charge')
print('9. Frequency')
print('10. Time Period')
print('11. Inductance\n')

cal = int(input('Enter the No. ahead of the Calculation You want to perform: '))
print('------------------------------------------------------------')

if cal == 1:
    I = float(input('Enter the value of Current: '))
    R = float(input('Enter the value of Resistance: '))

    V = I*R
    print('The Voltage is:', V)
    
elif cal == 2:
    V = float(input('Enter the value of Voltage: '))
    R = float(input('Enter the value of Resistance: '))

    I = V/R
    print('The Current is:', I)
    
elif cal == 3:
    V = float(input('Enter the value of Voltage: '))
    I = float(input('Enter the value of Current: '))

    R = V/I
    print('The Resistance is:', R)
    
elif cal == 4:
    R = float(input('Enter the value of Resistance: '))

    G = 1/R
    print('The Conductance is:', G)
    
elif cal == 5:
    V = float(input('Enter the value of Voltage: '))
    I = float(input('Enter the value of Current: '))

    P = V*I
    print('The Power is:', P)

elif cal == 6:
    Q = float(input('Enter the value of Charge: '))
    V = float(input('Enter the value of Voltage: '))

    C = Q/V
    print('The Capacitance is:', C)

elif cal == 7:
    R = float(input('Enter the value of Resistance: '))
    X = float(input('Enter the value of XL-XC: '))

    Z = ((R**2)+(X**2))**0.5
    print('The Impedance is:', Z)

elif cal == 8:
    C = float(input('Enter the value of Capacitance: '))
    V = float(input('Enter the value of Voltage: '))

    Q = C*V
    print('The Charge is:', Q)

elif cal == 9:
    T = float(input('Enter the value of Time Period: '))

    f = 1/T
    print('The Frequency is:', f)

elif cal == 10:
    f = float(input('Enter the value of Frequency: '))

    T = 1/f
    print('The Time Period is:', T)

elif cal == 11:
    V = float(input('Enter the value of Voltage: '))
    di = float(input('Enter the value of 1st derivative of Current: '))
    dt = float(input('Enter the value of 1st derivative of Time: '))

    L = V*(dt/di)
    print('The Inductance is:', L)

else:
    print('Selected option is invalid!')
