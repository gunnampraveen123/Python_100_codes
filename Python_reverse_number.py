# write a program to reverse a given number

val=int(input('Enter a number to reverse number:'))
rev=0
while val>0:
    rem=val%10
    rev=(rev*10)+rem
    val=val//10
print('Reversed number is :',rev)