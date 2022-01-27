import random

word_list = ['mouse', 'cat', 'dog', 'came', 'house']

rando_world = random.choice(word_list)
world_showed = []
for letter in rando_world:
    world_showed.append("_")

print(world_showed)
end_of_game=False
while not end_of_game:
    choisen_world = input('guess a letter: ').lower()
    for pos in range(len(rando_world)):
        if rando_world[pos] == choisen_world:
            world_showed[pos]=choisen_world


    print(world_showed)
    if "_" not in world_showed:
        end_of_game = True

print('end of the game')
