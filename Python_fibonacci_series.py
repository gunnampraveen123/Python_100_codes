# write a program to find fibonacci series up to a number

'''take input from user'''
val=eval(input('Enter a number to find fibonacci series:'))
a,b=0,1
print('Fibonacci Series:',a,b,end=',')
for i in range(2,val):
    c=a+b
    a=b
    b=c
    print(c,end=',')
