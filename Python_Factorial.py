# write a program to find factorial of a number

# logic 1
'''take input from user'''
val=eval(input('Enter a number to find factorial of a number:'))
factorial=1
for i in range(1,val+1):
    factorial=factorial*i
print('Factorial of a {} is '.format(val),factorial)


# logic 2
'''take input from user'''
val=eval(input('Enter a number to find factorial of a number:'))
factorial=1
i=1
while val>=i:
    factorial=factorial*i
    i=i+1
print('Factorial of a {} is '.format(val),factorial)
