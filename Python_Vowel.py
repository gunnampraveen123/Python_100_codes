# Write a program to identify if the character is a vowel or consonant

# logic 1
'''take input from user'''
char = input('Enter a character to check Whether it is vowel or consonant :')
if char.isalpha():
    ''' check the character vowel or consonant'''
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        print('{} it is a vowel character '.format(char))
    else:
        print('{} it is a consonant Character'.format(char))
else:
    print('invalid input')

# logic 2
'''take input from user'''
char = input('Enter a character to check Whether it is vowel or consonant :')
if char.isalpha():
    ''' check the character vowel or consonant'''
    if char in 'aeiouAEIOU':
        print('{} it is a vowel character '.format(char))
    else:
        print('{} it is a consonant Character'.format(char))
else:
    print('invalid input')