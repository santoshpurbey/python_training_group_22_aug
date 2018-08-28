mark = int(input('Enter your mark:'))

if mark > 100:
    print('Invalid Input, Please enter valid mark below 100')

elif mark >= 80:
    print('Congratulation! you got distionction')
elif mark >= 65:
    print('Congratulation! you got first divison ')
elif mark >= 50:
    print('Congratulation! you got second divison ')
elif mark >= 40:
    print('Congratulation! you got just pass')
else:
    print('Sorry you fail! better luck next time')
    
