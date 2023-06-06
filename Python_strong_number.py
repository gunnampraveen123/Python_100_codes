# write a program to identify if the number is strong number or not

num=int(input('Enter a number to find a number is strong or not:'))
s=0
i=num
while i>0:
    n=i%10
    factorial=1
    for j in range(1,n+1):
        factorial=factorial*j
    s=s+factorial
    i=i//10
print(s)
if num==s:
    print('Entered number is strong')
else:
    print('Entered number is not strong')

