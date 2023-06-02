# write a program to find roots of a quadratic equation

import math as m
'''ax^2+bx+c it is a quadratic equation'''
'''take a,b,c values from user''' 
a,b,c=eval(input('Enter the value a,b and c:'))
''' root=((-b)+/-sqrt((-b)^2-4ac))/2a'''
if a==0:
    print(' a cannot be zero ')
else:
    d=b**2-4*a*c
    root=m.sqrt(abs(d))
    if d>0:
        print('Two real roots')
        root1=(-b+root)/2*a
        print(root1)
        root2=(-b-root)/2*a
        print(root2)
    elif d == 0:
        print('Roots are equal')
        rt=(-b)/2*a
        print(rt)
    else:
        print('No real root')
        iroot=(-b)/(2*a)
        print(iroot,'+i',root)
        print(iroot,'-i',root)