# Write a program to identify if the number is even or odd

# case 1
''' take input from user'''
val=eval(input('Enter a number to check even or odd : '))
if val%2==0:
    print('%d is an even number'%val)
elif val%2!=0:
    print('%d is an odd number'%val)
else:
    print('Entered number is Zero')


# case 2
''' take input from user'''
val=eval(input('Enter a number to check even or odd : '))
if val>0:
    if val%2==0:
        print('%d is an even number'%val)
    elif val%2!=0:
        print('%d is an odd number'%val)
elif val==0:
    print('Entered number is Zero')
else:
    print('Entered number is negative')
