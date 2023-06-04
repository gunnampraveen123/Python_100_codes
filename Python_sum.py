# write a program to find sum of digits of a number 

# logic 1
'''take input from user'''
val=input('Enter a number to sum the digits of a number:')
sum=0
for i in val:
    j=int(i)
    sum=sum+j
print('The sum of {} is'.format(val),sum)

# logic 2
'''take input from user'''
val=int(input('Enter a number to sum the digits of a number:'))
sum=0
while val!=0:
    sum=sum+val%10
    val=val//10
print('The sum of the enter digit is',sum)
