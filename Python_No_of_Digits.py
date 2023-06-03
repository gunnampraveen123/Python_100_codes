# write a program to find Number of Digits in an integer

# logic 1
''' take input from user'''
val=input('Enter a number to count the no of digits:')
j=0
for i in val:
    j=j+1
print('The no of digits in an intger :', j)


# logic 2
val = str(input('Enter a number to count the no of digits:'))
print('The no of digits in an intger :',len(val))

# logic 3
val=eval(input('Enter a number to count the no of digits:'))
count=0
if val==0:
    print('the no of digits are : 1')
else:
    while val!=0:
        count=val//10
        count=count+1
print(count)

