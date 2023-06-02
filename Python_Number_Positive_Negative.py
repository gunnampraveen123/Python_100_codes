# write a program to identify of the number is postive or negative

''' take input from user'''
val=eval(input('Enter a number to check positive or negative : '))
if val > 0:
    print('{} is a positive Number'.format(val))
elif val < 0:
    print('{} is a Negative Number'.format(val))
else:
    print('Entered number is Zero')