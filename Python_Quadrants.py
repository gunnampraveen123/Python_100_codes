# write a program to find the quandrants in which coordinates lie

'''take x and y values as input from user'''
x=eval(input('Enter X-coordinate value:'))
y=eval(input('Enter Y-coordinate value:'))
if x>0 and y>0:
    print('This point lies in first Quadrant')
elif x<0 and y>0:
    print('This point lies in second Quadrant') 
elif x<0 and y<0:
    print('This point lies in Third Quadrant')  
elif x>0 and y<0:
    print('This point lies in fourth Quadrant')
else:
    print('This point lies at origin ')