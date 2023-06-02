# write a program to find ASCII value of a character

'''take input from user'''
char=input('Enter a charcter to find ASCII value :')
if len(char)==1:
    print('ASCII value of entered character is :',ord(char))
else:
    print('Enter a single character')