print('welcome')
height = int(input('what is your height?'))

if height>120:
    print('you can ride the rollercoster')
    age = int(input('enter your age?'))
    if age < 12:
        print('you must pay 5 dollars')
    elif age <= 18: 
        print('yout must pay 12 dollars')
    else:
        print('you must pay 17 dollars')
else:
    print('Sorry, you have to grow taller before you can ride ')


