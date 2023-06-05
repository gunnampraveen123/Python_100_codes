# write a program to find sum of natural numbers

'''take input from user'''
val=int(input('Enter a number to find sum of natural numbers:'))
sum=0
if val>0:
    for i in range(val+1):
        sum=sum+i
    print(sum)
elif val<0:
    print('Please Enter a positive a value')
else:
    print('Entered value is zero')
