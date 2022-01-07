print('welcome')
height = int(input('what is your height?'))

if height>120:
    print('you can ride the rollercoster')
    age = int(input('enter your age?'))
    if age < 12:
        bill = 5
        print('you must pay 5 dollars')
    elif age <= 18: 
        bill =12
        print('yout must pay 12 dollars')
    else:
        bill=17
        print('you must pay 17 dollars')

    what_photo = input('Do you want a photo taken? Y or N')
    if what_photo == 'Y':
        bill += 3

    print(f'you bill is {bill}')

else:
    print('Sorry, you have to grow taller before you can ride ')


