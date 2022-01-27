import random

word_list = ['mouse', 'cat', 'dog', 'came', 'house']

rando_world = random.choice(word_list)

choisen_world = input('guess a letter: ').lower()

for letter in rando_world:
    if letter == choisen_world:
        print('right')
    else:
        print('fail')
