import random 

opt = int(input("Welcome select 1) scissors, 2) paper, 3) rock"))

opt_computer =  random.randint(1,3)

def name_selecte(opt):
    if opt == 1:
        return 'scissors'
    if opt == 2:
        return 'paper'
    if opt ==3:
        return 'rock'
    return 'loser'

name = name_selecte(opt)
name2 = name_selecte(opt_computer)

if opt == 1 and opt_computer == 2:
    print('you win')
elif opt == 3 and opt_computer == 2:
    print('Yout win')
elif opt == 2 and opt_computer==3:
    print('you win')
elif opt == opt_computer:
    print('is a draw')
else:
    print('you lose')

print(f"you {name}, computer {name2}")
