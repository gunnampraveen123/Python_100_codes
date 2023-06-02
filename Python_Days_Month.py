# write a program to find Number of days in a given month of a given year

'''take input no of days from user'''
month=eval(input('Enter Month :'))
year=eval(input('Enter Year:'))
if (month==2 and year%400==0 ) or (month==2 and year%4==0):
    print('No of Days 29')
elif month in(1,3,5,7,8,10,12) and year:
    print('No of Days 31 ' )
elif month in (4,6,9,11):
    print('No of Days 30')
else:
    print('No of Days 28')
